from azure.storage.blob import BlobServiceClient

storage_account_key = "SFb/2eipnq37jyk15oc8Lt2lzSX+6ySkZB2baa/R1DpGhbjEBqbZL+HG405Go+cziWMbPRcn1Qd3+AStj3PcwQ=="
storage_account_name = "moviesfiles"
connection_string = "DefaultEndpointsProtocol=https;AccountName=moviesfiles;AccountKey=SFb/2eipnq37jyk15oc8Lt2lzSX+6ySkZB2baa/R1DpGhbjEBqbZL+HG405Go+cziWMbPRcn1Qd3+AStj3PcwQ==;EndpointSuffix=core.windows.net"
container_name = "movies-container"

def uploadToBlobStorage(file_path,file_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
    with open(file_path, 'rb') as data:
        blob_client.upload_blob(data, overwrite = True)
        print(f'Uploaded {file_name}.')

# calling a function to perform upload
uploadToBlobStorage('/home/user/Pobrane/ETL/result.csv', 'movies-data.csv')