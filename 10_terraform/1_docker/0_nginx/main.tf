# ------------------------
# PROVIDERS
# ------------------------
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.5"
    }
  }
}

provider "docker" {}
provider "random" {}

# ------------------------
# RESOURCES
# ------------------------
resource "random_string" "suffix" {
  length  = 3
  upper   = false
  special = false
}

resource "docker_image" "nginx" {
  name         = "nginx"
  keep_locally = false
}

resource "docker_container" "nginx" {
  image = docker_image.nginx.image_id
  name  = "tutorial-${random_string.suffix.result}"

  ports {
    internal = 80
    external = 8080
  }
}

# ------------------------
# OUTPUT
# ------------------------
output "container_name" {
  value = docker_container.nginx.name
}