# variable "location" {
#   description = "Azure region"
#   default     = "swec"
# }

variable "resource_group_name" {
  description = "Resource group name"
  default     = "test-rg-1"
}

variable "aks_cluster_name" {
  description = "AKS cluster name"
  default     = "test-k8s-1"
}
