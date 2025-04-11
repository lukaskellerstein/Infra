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

# use Existing resource group
data "azurerm_resource_group" "my_rg" {
  name = var.resource_group_name
}

# Create a Log Analytics Workspace (required for the Container App Environment)
resource "azurerm_log_analytics_workspace" "my_log_analytics" {
  name                = "my-example-log-analytics"
  location            = var.location
  resource_group_name = data.azurerm_resource_group.my_rg.name
  sku                 = "PerGB2018"
  retention_in_days   = 30
}

resource "azurerm_container_app_environment" "my_container_app_env" {
  name                       = "my-container-app-env"
  location                   = var.location
  resource_group_name        = data.azurerm_resource_group.my_rg.name
  log_analytics_workspace_id = azurerm_log_analytics_workspace.my_log_analytics.id
}

resource "azurerm_container_app_job" "my_app_job" {
  name                         = "my-container-app-job"
  location                     = var.location
  resource_group_name          = data.azurerm_resource_group.my_rg.name
  container_app_environment_id = azurerm_container_app_environment.my_container_app_env.id

  replica_timeout_in_seconds = 100
  
  manual_trigger_config {
    parallelism              = 1
    replica_completion_count = 1
  }

  template {
    container {
      image = "lukaskellerstein/python-script-azure-1:0.0.3"
      name  = "mycontainerappsjob0"

      cpu    = 0.5
      memory = "1Gi"
    }
  }
}