# 🌿 OpsGarden – A DevOps Playground on AWS

**OpsGarden** is a real-world DevOps learning and demo environment, designed to provision, deploy and monitor modern applications using a full cloud-native toolchain on **AWS**.  
It's an evolving project that integrates **Terraform**, **EKS**, **GitHub Actions**, and observability tooling – built for experimentation, automation, and showcasing best practices.

---

## 🌱 Tech Stack

- **AWS Services**: EKS, IAM, EC2, VPC, S3
- **Infrastructure as Code**: Terraform (modular)
- **CI/CD**: GitHub Actions
- **Containers & Orchestration**: Docker + Kubernetes
- **Monitoring & Logging** *(coming soon)*: Prometheus, Grafana, Loki
- **Security & Secrets** *(planned)*: Trivy, Sealed Secrets

---

## 🚀 Project Milestones

| Status | Goal |
|--------|------|
| ✅     | Build and provision an EKS cluster via Terraform |
| 🛠️     | Add Bastion host for private API access |
| 🔜     | Deploy containerized app via GitHub Actions |
| 🔜     | Integrate Prometheus/Grafana monitoring stack |
| 🔜     | Add DevSecOps tooling (Trivy, Sealed Secrets) |

---

## 📁 Project Structure

ops-garden/
├── terraform/ # IaC for VPC, IAM, EKS, Bastion
│ ├── main.tf
│ ├── vpc.tf
│ ├── eks.tf
│ ├── bastion.tf
│ └── variables.tf
├── .gitignore
└── README.md

yaml
Kopieren
Bearbeiten

---

## 🧪 Currently Working On

> Infrastructure phase:
> - [x] VPC with public/private subnets
> - [x] EKS cluster setup
> - [x] Bastion host deployment
> - [ ] kubectl access from bastion  
> - [ ] Define secure CI/CD pipeline

---

## 📌 How to Contribute

This is a solo learning repo, but feel free to fork, star, or suggest improvements via Issues or Pull Requests.

---

## ✨ Inspiration

Building a DevOps lab environment as part of my journey toward mastering real-world infrastructure automation and GitOps workflows.  
*Currently deployed → Terraform Destroyed → CI/CD Pipeline Coming Next!*

---

🟢 _Repo last updated: `$(date)`_  
🔗 [LinkedIn][(https://www.linkedin.com/in/stella-joubert-58713a242/)] • [GitHub Profile](https://github.com/GitCubeStella)
