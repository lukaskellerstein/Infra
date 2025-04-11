
# ----------
# Resource group
# ----------
variable "resource_group_name" { default = "my-rg-1" }
variable "location" { default = "swedencentral" }

# ----------
# Identity
# ----------
variable "identity_name" { default = "test-identity" }

# ----------
# Storage
# ----------

# random string
resource "random_string" "suffix" {
  length  = 5
  upper   = false
  lower   = true
  special = false
}
variable "storage_name" { default = "storage${random_string.suffix.result}" }

# ----------
# Container App Job
# ----------
variable "log_analytics" { default = "my-log-analytics" }
variable "container_env" { default = "my-container-env" }
variable "container_app_job" { default = "my-app-job" }
variable "container_name" { default = "my-container-1" }
variable "container_image" { default = "lukaskellerstein/python-script-azure-1:0.0.3" }