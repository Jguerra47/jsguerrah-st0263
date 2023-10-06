from concurrent import futures
import grpc
import logging
import protobufs.python.FileServices_pb2 as FileServicesStub
import protobufs.python.FileServices_pb2_grpc as FileServices_pb2_grpc
from common.services import Service

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

HOST = '[::]:50051'

class FileService(FileServices_pb2_grpc.FileServiceServicer):

    def ListFiles(self, request, context):
        logging.info("LIST request was received: %s", str(request))
        response = []

        for f in Service.listFiles():
            fileInfo = FileServicesStub.FileMetadata(name=f['name'],
                                                size=f['size'],
                                                timestamp=f['timestamp'])
            response.append(fileInfo)

        return FileServicesStub.FileList(metadata=response)

    def FindFile(self, request, context):
        logging.info("FIND request was received: %s", str(request))
        response = []

        for f in Service.findFiles(request.name):
            fileInfo = FileServicesStub.FileMetadata(name=f['name'],
                                                size=f['size'],
                                                timestamp=f['timestamp'])
            response.append(fileInfo)

        return FileServicesStub.FileList(metadata=response)

    def GetFile(self, request, context):
        logging.info("GET request was received: %s", str(request))
        name, data, e = Service.getFile(request.name)

        if e is FileNotFoundError:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('File not found')
            logging.warning("File not found: %s", request.name)
        elif e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            logging.error("Error getting file: %s. Error: %s", request.name, str(e))

        return FileServicesStub.FileContent(name=name, data=data)

    def PutFile(self, request, context):
        logging.info("PUT request was received: %s", str(request))
        code, message, e = Service.putFile(request.name, request.data)
        if e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            logging.error("Error putting file: %s. Error: %s", request.name, str(e))
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