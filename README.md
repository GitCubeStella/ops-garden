# 🌿 OpsGarden – A DevOps Playground on AWS

[![CI Build](https://github.com/GitCubeStella/ops-garden/actions/workflows/docker-build.yml/badge.svg)](https://github.com/GitCubeStella/ops-garden/actions) [![Run Tests](https://github.com/GitCubeStella/ops-garden/actions/workflows/docker-test.yml/badge.svg)](https://github.com/GitCubeStella/ops-garden/actions)

**OpsGarden** ist ein hands-on DevOps-Demoprojekt, das zeigt, wie man Microservices lokal entwickelt und später in eine skalierbare AWS-Umgebung (EKS) deployt – mit Fokus auf CI/CD, Infrastructure as Code und Observability.

---

## 🧰 Tech Stack

- **FastAPI** – Python-basierter notes_service-Microservice
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
      pip install -r app/notes_service-service/requirements.txt

  - name: Run tests
    run: |
      cd app/notes_service-service
      pytest
```

💡 Es wird eine **file-basierte SQLite-Datenbank** (`sqlite:///./test.db`) verwendet, um schnelle isolierte Tests durchzuführen.

---

## 📦 Microservices (Phase 1)

| Service               | Status        | Beschreibung                        |
|------------------------|---------------|-------------------------------------|
| 📝 `notes_service-service`     | ✅ lokal aktiv | REST-API (FastAPI + PostgreSQL)     |
| 🔐 `auth-service`      | 🔜 geplant     | JWT-basierte Auth (Node.js)         |
| 📊 `metrics-exporter`  | 🔜 geplant     | Prometheus Exporter                 |
| 🖼️ `frontend`          | 🔜 geplant     | Web-UI (z. B. Svelte)               |

---

## 🧪 Local Setup

```bash
docker compose up --build
```

Dann erreichbar unter: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🚧 Next Steps

- Push Images nach Amazon ECR  
- Deployment auf EKS via Helm oder Kustomize  
- Secrets via Sealed Secrets  
- Prometheus / Grafana Monitoring  
- Auth-Service mit JWT  
- Frontend integrieren  

---

## 👩‍💻 Über das Projekt

> Erstellt von **Stella Joubert** als öffentliches DevOps-Lern- & Referenzprojekt.