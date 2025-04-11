
variable "resource_group_name" {
  description = "The name of the resource group to create."
  type        = string
  default     = "test-rg-1"
}

variable "location" {
  description = "The Azure region in which to create resources."
  type        = string
  default     = "swec"
}

variable "storage_account_name" {
  description = "The name of the storage account. Must be globally unique, 3-24 characters, and lowercase."
  type        = string
  default     = "mystorageaccount323423423423"
}