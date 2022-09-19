import json
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from config import config


class BlobService:
  def __init__(self, connection_str: str):
    self.blob_service_client = BlobServiceClient.from_connection_string(connection_str)

  def download_blob(self, container: str, blob_path: str) -> object:
    blob_client = self.blob_service_client.get_blob_client(container, blob_path)

    blob_data = blob_client.download_blob()
    data_str = blob_data.readall()

    data_json = json.loads(data_str)
    return data_json

  def upload_blob(self, container: str, blob_path: str, data: str):
    blob_client = self.blob_service_client.get_blob_client(container, blob_path)
    blob_client.upload_blob(data, overwrite=True)

_connection_string = config.get_blob_storage_connection_str()
blob_service = BlobService(_connection_string)

