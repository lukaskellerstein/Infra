terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

variable "my_docker_image" {
  description = "The custom Docker image to deploy (e.g., 'nginx:latest' or your own image name)"
  type        = string
  default     = "lukaskellerstein/my_python_script:0.0.1"
}

resource "docker_image" "custom" {
  name         = var.my_docker_image
}

resource "docker_container" "custom" {
  name  = "my_custom_container"
  image = docker_image.custom.image_id
}

output "container_name" {
  value = docker_container.custom.name
}
