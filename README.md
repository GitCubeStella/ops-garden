# 🌿 OpsGarden – A DevOps Playground on AWS

[![CI Build](https://github.com/GitCubeStella/ops-garden/actions/workflows/docker-build.yml/badge.svg)](https://github.com/GitCubeStella/ops-garden/actions)
[![Run Tests](https://github.com/GitCubeStella/ops-garden/actions/workflows/docker-test.yml/badge.svg)](https://github.com/GitCubeStella/ops-garden/actions)

**OpsGarden** ist ein hands-on DevOps-Demoprojekt, das zeigt, wie man Microservices lokal entwickelt und später in eine skalierbare AWS-Umgebung (EKS) deployt – mit Fokus auf CI/CD, Infrastructure as Code und Observability.

---

## 🧰 Tech Stack

- **FastAPI** – Python-basierter Notes-Microservice
- **SQLModel** + **PostgreSQL** – relationale Datenbank
- **Docker** & **Docker Compose** – lokale Container-Orchestrierung
- **Terraform** – Infrastruktur-Code für VPC, EKS & Bastion Host
- **GitHub Actions** – automatisierte Tests und Builds
- *(Geplant: Helm, Kustomize, Prometheus, Grafana, Sealed Secrets)*

---

## ⚙️ CI/CD Pipelines

> GitHub Actions führt automatisiert Tests bei jedem Push & PR gegen `main` aus.

```yaml
# .github/workflows/docker-test.yml
env:
  DATABASE_URL: "sqlite:///:memory:"

steps:
  - uses: actions/checkout@v3
  - uses: actions/setup-python@v4
    with:
      python-version: '3.11'

  - name: Install dependencies
    run: |
      python -m pip install --upgrade pip
      pip install -r app/notes-service/requirements.txt

  - name: Run tests
    run: |
      cd app/notes-service
      pytest
```

💡 Es wird eine **SQLite In-Memory-Datenbank** verwendet, um schnelle isolierte Tests durchzuführen.

---

## 📦 Microservices (Phase 1)

| Service               | Status        | Beschreibung                        |
|------------------------|---------------|-------------------------------------|
| 📝 `notes-service`     | ✅ lokal aktiv | REST-API (FastAPI + PostgreSQL)     |
| 🔐 `auth-service`      | 🔜 geplant     | JWT-basierte Auth (Node.js)         |
| 📊 `metrics-exporter`  | 🔜 geplant     | Prometheus Exporter                 |
| 🖼️ `frontend`          | 🔜 geplant     | Web-UI (z. B. Svelte)               |

---

## 🧪 Local Setup

```bash
docker compose up --build
📍 API erreichbar unter: http://localhost:8000/docs

🧠 Aktueller Stand & Nächste Schritte
✅ FastAPI mit Lifespan Events (statt deprecated on_event)

✅ SQLModel & SQLite-basierte Tests via GitHub Actions

⏳ Auth-Service & Frontend in Vorbereitung

🔜 ECR Push & Helm/Kustomize für EKS-Deployments

🔐 Secrets Management (z. B. via GitHub OIDC & Sealed Secrets)

📊 Monitoring (Prometheus + Grafana Dashboards)

🧬 Beispiel für Lifespan (FastAPI)
python
Kopieren
Bearbeiten
from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
👩‍💻 About
Erstellt von Stella Joubert als öffentliches Lern- & Portfolio-Projekt für moderne DevOps-Workflows und Microservice-Architekturen.