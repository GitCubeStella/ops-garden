variable "aws_region" {
  description = "AWS region to deploy EKS cluster"
  type        = string
  default     = "eu-central-1"
}

variable "aws_profile" {
  description = "AWS CLI profile name"
  type        = string
  default     = "default"
}
