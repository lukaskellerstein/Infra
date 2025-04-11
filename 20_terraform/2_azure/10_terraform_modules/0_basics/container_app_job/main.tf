
# ----------------
# Resources
# ----------------
# Create a Log Analytics Workspace (required for the Container App Environment)
resource "azurerm_log_analytics_workspace" "my_log_analytics" {
  name                = var.log_analytics
  location            = var.location
  resource_group_name = var.resource_group_name
  sku                 = "PerGB2018"
  retention_in_days   = 30
}

resource "azurerm_container_app_environment" "my_container_app_env" {
  name                       = var.container_env
  location                   = var.location
  resource_group_name        = var.resource_group_name
  log_analytics_workspace_id = azurerm_log_analytics_workspace.my_log_analytics.id
}

resource "azurerm_container_app_job" "my_app_job" {
  name                         = var.container_app_job
  location                     = var.location
  resource_group_name          = var.resource_group_name
  container_app_environment_id = azurerm_container_app_environment.my_container_app_env.id

  replica_timeout_in_seconds = 100

  identity {
    type         = "UserAssigned"
    identity_ids = [var.my_identity]
  }
  
  manual_trigger_config {
    parallelism              = 1
    replica_completion_count = 1
  }

  template {
    container {
      name  = var.container_name
      image = var.container_image

      cpu    = 0.5
      memory = "1Gi"
    }
  }
}

# ----------------
# Output variables
# ----------------
# none