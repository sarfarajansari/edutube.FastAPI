from azure.storage.blob import BlobServiceClient
import datetime
from random import randint
from io import BytesIO


def getvideoname(name):
    now = datetime.datetime.now()
    return f"{now.strftime('%Y%m%d%H')}/video{randint(1000, 9999)}/" + name


# Replace with your Azure Storage connection string
connect_str = "DefaultEndpointsProtocol=https;AccountName=generalalstorage;AccountKey=MdsdByMkrKCSU6yAsNS+fLfZdncK5t6Zqaq1kBHh3UPBY5PkEEC35MbAN+Ldd4QNgLO/sHyv3b2h+AStoGvoVA==;EndpointSuffix=core.windows.net"
container_name = "visualvoice"  # Replace with your container name

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Get a container client object
container_client = blob_service_client.get_container_client(container_name)


def save_video_azure(filepath, filename):
    with open(filepath, "rb") as data:
        name = getvideoname(filename)
        # bytes_io_object = BytesIO(content)
        # bytes_io_object.seek(0)]

        bytes_io_object = BytesIO(data.read())
        bytes_io_object.seek(0)
        print(filepath)
        container_client.upload_blob(
            name=name, data=bytes_io_object, overwrite=True)
        
        data.close()

        return 'https://generalalstorage.blob.core.windows.net/visualvoice/' + name
