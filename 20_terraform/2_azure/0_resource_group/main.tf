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

resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}