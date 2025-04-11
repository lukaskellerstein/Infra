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

# Resource group
resource "azurerm_resource_group" "my_rg" {
  name     = var.resource_group_name
  location = var.location
}

# Managed Identity
resource "azurerm_user_assigned_identity" "my_mi" {
  location            = var.location
  resource_group_name = var.resource_group_name
  name                = var.identity_name
}


# -------------------
# Storage Account
# -------------------
module "storage" {
  source               = "./storage"
  resource_group_name  = var.resource_group_name
  location             = var.location
  storage_account_name = var.storage_name
  my_identity = azurerm_user_assigned_identity.my_mi.principal_id
}


# -------------------
# Container App Job
# -------------------
module "container_app_job" {
  source               = "./container_app_job"
  resource_group_name  = var.resource_group_name
  location             = var.location
  log_analytics = var.log_analytics
  container_env = var.container_env
  container_app_job = var.container_app_job
  container_name = var.container_name
  container_image = var.container_image
  my_identity = azurerm_user_assigned_identity.my_mi.id
}