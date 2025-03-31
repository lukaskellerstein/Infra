variable "location" {
  description = "Azure region"
  default     = "westus2"
}

variable "resource_group_name" {
  description = "Resource group name"
  default     = "my-k8s-rg"
}

variable "aks_cluster_name" {
  description = "AKS cluster name"
  default     = "my-k8s"
}

variable "aks_dns_prefix" {
  description = "DNS prefix for AKS"
  default     = "my-dns"
}

variable "node_count" {
  description = "Number of nodes in the default node pool"
  default     = 3
}

variable "vm_size" {
  description = "VM size for AKS nodes"
  # For testing the deployment
  default     = "Standard_D1_v2"  
  # For real environment
  #default     = "Standard_D3_v2"
}
