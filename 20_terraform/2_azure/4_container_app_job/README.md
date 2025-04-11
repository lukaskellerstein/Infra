https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/container_app_job

# Managed Identity

1. The script in docker container has to have correctly set evirovnment variables to use the `Managed identity`

2. The container app job has to ALSO has assigned correctly the managed identity

3. The managed identity itself has to have a permissions to the storage account (because the script is reading from a storage account)
