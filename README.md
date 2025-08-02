# 🌿 OpsGarden   – A DevOps Playground on AWS

[![CI Build](https://github.com/GitCubeStella/ops-garden/actions/workflows/docker-build.yml/badge.svg)](https://github.com/GitCubeStella/ops-garden/actions)

**OpsGarden** is a real-world DevOps demo environment designed to build, deploy, and monitor microservices in a scalable AWS setup – starting locally with Docker Compose and growing toward EKS.

---

## 🧰 Tech Stack

- **FastAPI** – Python-based microservice (Notes)
- **PostgreSQL** – persistent backend database
- **Docker** & **Docker Compose** – local container orchestration
- **Terraform** – AWS infrastructure: VPC, EKS, Bastion
- **GitHub Actions** – CI/CD for container build and deployment
- *(Planned)* Prometheus, Grafana, Sealed Secrets, Helm

---

## 📦 Microservices (Phase 1: in progress)

| Service         | Status     | Beschreibung                   |
|-----------------|------------|--------------------------------|
| 📝 `notes-service` | ✅ live (locally) | REST-API für Notizen (FastAPI + Postgres) |
| 🔐 `auth-service`  | 🔜 geplant     | Benutzer-Auth mit JWT (Node.js) |
| 📊 `metrics-exporter` | 🔜 geplant | App-Metriken für Prometheus     |
| 🎨 `frontend`      | 🔜 optional   | Web-UI für CloudNotes           |

---

## 🧪 Local Setup

```bash
    docker compose up --build
```

Dann erreichbar unter: http://localhost:8000/docs

---

## 🧠 Next Steps
 Push Image to Amazon ECR

 Deploy to EKS via Helm or Kustomize

 Add CI/CD secrets & GitHub workflows

 Add monitoring & custom metrics
 
---

## 👩‍💻 About

Built by Stella Joubert as a public DevOps learning & reference project.


---

## ✨ Was du jetzt tun kannst:

1. Kopiere den Inhalt in dein `README.md`
2. Commit + push:

```bash
git add README.md
git commit -m "📝 Update README with badges and project overview"
git push
```
