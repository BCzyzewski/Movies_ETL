from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

load_dotenv()

connection_string = os.environ.get('connection_string')
container_name = os.environ.get('container_name')


def uploadToBlobStorage(file_path,file_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
    with open(file_path, 'rb') as data:
        blob_client.upload_blob(data, overwrite = True)
        print(f'Uploaded {file_name}.')