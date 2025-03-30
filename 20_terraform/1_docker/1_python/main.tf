terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "my_python_timer" {
  name         = "my-python-timer"
  build {
    context    = "${path.module}"
    dockerfile = "${path.module}/Dockerfile"
  }
  keep_locally = true
}

resource "random_string" "suffix" {
  length  = 4
  upper   = false
  special = false
}

resource "docker_container" "my_timer" {
  image = docker_image.my_python_timer.image_id
  name  = "my-timer-${random_string.suffix.result}"

  must_run = true
  rm       = true # Auto-remove the container after it exits
}

output "container_name" {
  value = docker_container.my_timer.name
}
