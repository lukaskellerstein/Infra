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
}

variable "resource_group_name" {
  description = "The name of the resource group to create."
  type        = string
  default     = "my-resource-group"
}

variable "location" {
  description = "The Azure region in which to create resources."
  type        = string
  default     = "East US"
}

variable "storage_account_name" {
  description = "The name of the storage account. Must be globally unique, 3-24 characters, and lowercase."
  type        = string
  default     = "mystorageaccount4444"
}

# Use existing resource group
data "azurerm_resource_group" "existing" {
  name = var.resource_group_name
}

resource "azurerm_storage_account" "storage" {
  name                     = var.storage_account_name
  resource_group_name      = data.azurerm_resource_group.existing.name
  location                 = data.azurerm_resource_group.existing.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  tags = {
    environment = "example"
  }
}
