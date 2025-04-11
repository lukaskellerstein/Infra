terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
    random = {
      source = "hashicorp/random"
      version = "~> 3.1"
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
  default     = "mystorageaccount"
}

# Use existing resource group
data "azurerm_resource_group" "existing" {
  name = var.resource_group_name
}

# random string
resource "random_string" "suffix" {
  length  = 5
  upper   = false
  lower   = true
  special = false
}

resource "azurerm_storage_account" "storage" {
  name                     = "${var.storage_account_name}${random_string.suffix.result}"
  resource_group_name      = data.azurerm_resource_group.existing.name
  location                 = data.azurerm_resource_group.existing.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  shared_access_key_enabled = false

  tags = {
    environment = "example"
  }
}
