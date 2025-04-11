# ----------------
# Input variables
# ----------------
variable "resource_group_name" {}
variable "location" {}
variable "storage_account_name" {}
variable "my_identity" {
  description = "Principal ID of the managed identity to assign to the storage account."
}
