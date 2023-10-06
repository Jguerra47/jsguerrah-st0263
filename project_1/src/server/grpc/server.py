from concurrent import futures
import grpc
import protobufs.python.FileServices_pb2 as FileServicesStub
import protobufs.python.FileServices_pb2_grpc as FileServices_pb2_grpc
from common.services import Service

HOST = '[::]:50051'

class FileService(FileServices_pb2_grpc.FileServiceServicer):

    def ListFiles(self, request, context):
        print("LIST request was received: " + str(request))
        response = []

        for f in Service.listFiles():
            fileInfo = FileServicesStub.FileMetadata(name=f['name'],
                                                size=f['size'],
                                                timestamp=f['timestamp'])
            response.append(fileInfo)

        return FileServicesStub.FileList(metadata=response)

    def FindFile(self, request, context):
        print("FIND request was received: " + str(request))
        response = []

        for f in Service.findFiles(request.name):
            fileInfo = FileServicesStub.FileMetadata(name=f['name'],
                                                size=f['size'],
                                                timestamp=f['timestamp'])
            response.append(fileInfo)

        return FileServicesStub.FileList(metadata=response)

    def GetFile(self, request, context):
        print("GET request was received: " + str(request))
        name, data, e = Service.getFile(request.name)

        if e is FileNotFoundError:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('File not found')
        elif e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))

        return FileServicesStub.FileContent(name=name, data=data)

    def PutFile(self, request, context):
        print("PUT request was received: " + str(request))
        code, message, e = Service.putFile(request.name, request.bytes)
        if e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
        return FileServicesStub.OperationStatus(code=code, message=message)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    FileServices_pb2_grpc.add_FileServiceServicer_to_server(
        FileService(), server)
    server.add_insecure_port(HOST)
    print("DataNode is running... ")
    server.start()
    server.wait_for_termination()

def run():
    serve()
