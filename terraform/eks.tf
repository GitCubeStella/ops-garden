module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "20.8.4" # aktuelle stabile Version

  cluster_name    = "ops-garden-cluster"
  cluster_version = "1.29"
  subnet_ids      = module.vpc.private_subnets
  vpc_id          = module.vpc.vpc_id

  enable_irsa = true  # für IAM-Rollen für Pods

  eks_managed_node_groups = {
    default = {
      instance_types = ["t3.medium"]
      desired_size   = 2
      max_size       = 3
      min_size       = 1

      capacity_type = "ON_DEMAND"
    }
  }

  tags = {
    Environment = "dev"
    Terraform   = "true"
    Project     = "ops-garden"
  }
}
