terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "local" {}  # optional: später zu S3 ändern
}

provider "aws" {
  region  = var.aws_region
  profile = var.aws_profile
}
