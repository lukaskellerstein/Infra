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

# Use existing resource group
data "azurerm_resource_group" "existing" {
  name = var.resource_group_name
}

# Create a Log Analytics Workspace (required for the Container App Environment)
resource "azurerm_log_analytics_workspace" "law" {
  name                = "containerapps-law"
  resource_group_name = data.azurerm_resource_group.existing.name
  location            = data.azurerm_resource_group.existing.location
  sku                 = "PerGB2018"
  retention_in_days   = 30
}

# Create a Container App Environment which provides the underlying infrastructure for container apps
resource "azurerm_container_app_environment" "my_containerapp_env" {
  name                        = "containerapps-env"
  resource_group_name         = data.azurerm_resource_group.existing.name
  location                    = data.azurerm_resource_group.existing.location

  log_analytics_workspace_id  = azurerm_log_analytics_workspace.law.id
}

# Create the Container App using your custom Docker image
resource "azurerm_container_app" "my_container_app" {
  name                         = "my-python-api-app"
  container_app_environment_id = azurerm_container_app_environment.my_containerapp_env.id
  resource_group_name          = data.azurerm_resource_group.existing.name
  revision_mode = "Single"

  ingress {
    external_enabled = true
    target_port      = 80
    traffic_weight {
      percentage = 100
      latest_revision = true
    }
  }

  template {
    container {
      name   = "python-api-container"
      image  = "lukaskellerstein/my_python_api:0.0.1"
      cpu    = 0.5
      memory = "1.0Gi"
    }
  }
}
