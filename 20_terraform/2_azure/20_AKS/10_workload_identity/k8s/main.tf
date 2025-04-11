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

# A) Create a new resource group
# resource "azurerm_resource_group" "my_rg" {
#   name     = var.resource_group_name
#   location = var.location
# }

# B) Use existing resource group
data "azurerm_resource_group" "my_rg" {
  name = var.resource_group_name
}

resource "azurerm_kubernetes_cluster" "my_aks" {
  name                = var.aks_cluster_name
  location            = azurerm_resource_group.my_rg.location
  resource_group_name = azurerm_resource_group.my_rg.name

  identity {
    type = "SystemAssigned"
  }

  default_node_pool {
    name                = "systemnp"
    node_count          = 1
    vm_size             = "Standard_D2ls_v5"
  }
}
