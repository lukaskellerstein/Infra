
variable "resource_group_name" {
  description = "The name of the resource group for the container app."
  type        = string
  default     = "my-resource-group"
}

variable "location" {
  description = "Azure location for the deployment."
  type        = string
  default     = "East US"
}
