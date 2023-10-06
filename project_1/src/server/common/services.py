import os
import glob
import datetime
from server import ASSETS_DIR

class FileServices:

    def listFiles(self):
        collection = []
        for filename in os.listdir(ASSETS_DIR):
            file_info = {}
            file_path = os.path.join(ASSETS_DIR, filename)

            if os.path.isfile(file_path):
                size = os.path.getsize(file_path)
                time = os.path.getmtime(file_path)
                timestamp = datetime.datetime.fromtimestamp(time)
                formatted_date = timestamp.strftime("%Y-%m-%d %H:%M:%S")

                file_info["name"] = filename
                file_info["size"] = size
                file_info["timestamp"] = formatted_date
                collection.append(file_info)
        return collection

    def findFiles(self, search: str) -> list:
        collection = []
        for filename in glob.glob(f"{ASSETS_DIR}/{search}"):
            file_info = {}

            size = os.path.getsize(filename)
            time = os.path.getmtime(filename)
            timestamp = datetime.datetime.fromtimestamp(time)
            formatted_date = timestamp.strftime("%Y-%m-%d %H:%M:%S")

            file_info["name"] = os.path.basename(filename)
            file_info["size"] = size
            file_info["timestamp"] = formatted_date
            collection.append(file_info)
        return collection

    def putFile(self, name: str, data: bytes) -> tuple:
        try:
            with open(os.path.join(ASSETS_DIR, name), 'wb') as f:
                f.write(data)
            return 200, 'File uploaded successfully', None
        except Exception as e:
            return 500, 'Internal Server Error', e

    def getFile(self, name: str) -> tuple:
        try:
            with open(os.path.join(ASSETS_DIR, name), 'rb') as f:
                data = f.read()
            return name, data, None
        except Exception as e:
            return '', b'', e

Service = FileServices()