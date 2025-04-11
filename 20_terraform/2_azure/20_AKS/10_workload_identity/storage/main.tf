terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}

  # Use Managed Identity when run Terraform commands.
  # Authenticate using the Azure CLI => `az login`
  use_msi = true
}


# Use existing resource group
data "azurerm_resource_group" "my_rg" {
  name = var.resource_group_name
}

resource "azurerm_storage_account" "storage" {
  name                     = var.storage_account_name
  resource_group_name      = data.azurerm_resource_group.my_rg.name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  shared_access_key_enabled = false
}
