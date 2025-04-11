import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, ContainerClient
from dotenv import load_dotenv
load_dotenv()


print("Hello from Python script!")

# Replace with your Azure Storage Account name
STORAGE_ACCOUNT_NAME =  os.getenv("STORAGE_ACCOUNT_NAME", "aaa") 

IDENTITY = os.getenv("IDENTITY", "bbb")
print("IDENTITY", IDENTITY)


# Build the account URL
account_url = f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net"

# Use DefaultAzureCredential (can use environment credentials, VSCode, Azure CLI, etc.)
credential = DefaultAzureCredential(managed_identity_client_id=IDENTITY)

# Create the service client
blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)

def list_all_blobs():
    print(f"Listing all containers and blobs in storage account: {STORAGE_ACCOUNT_NAME}")

    containers = blob_service_client.list_containers()

    for container in containers:
        container_name = container['name']
        print(f"\n📦 Container: {container_name}")

        container_client = blob_service_client.get_container_client(container_name)
        blobs = container_client.list_blobs()

        for blob in blobs:
            print(f"  └─ 📄 {blob.name}")

if __name__ == "__main__":
    list_all_blobs()
