# 🌿 OpsGarden – A DevOps Playground on AWS

[![CI Build](https://github.com/GitCubeStella/ops-garden/actions/workflows/docker-build.yml/badge.svg)](https://github.com/GitCubeStella/ops-garden/actions)
[![Run Tests](https://github.com/GitCubeStella/ops-garden/actions/workflows/docker-test.yml/badge.svg)](https://github.com/GitCubeStella/ops-garden/actions)

**ENGLISH**

**OpsGarden** is a hands-on DevOps learning project demonstrating how to locally build microservices and deploy them to a scalable AWS environment (EKS) – focusing on CI/CD, Infrastructure as Code, and Observability.

---

## 🧰 Tech Stack

- **FastAPI** – Python-based microservices (`notes_service`, `users_service`)
- **SQLModel** + **SQLite / PostgreSQL** – relational databases
- **Docker** & **Docker Compose** – local container orchestration
- **Terraform** – IaC for VPC, EKS & Bastion Host
- **GitHub Actions** – automated tests and builds
- *(Planned: Helm, Kustomize, Prometheus, Grafana, Sealed Secrets)*

---

## ⚙️ CI/CD Pipelines

> GitHub Actions run tests automatically on each push or pull request to `main`.

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
      pip install -r app/notes_service/requirements.txt

  - name: Run tests
    run: |
      cd app/notes_service
      pytest
```

💡 An in-memory SQLite database (`sqlite:///:memory:`) is used for fast isolated test runs.

---

## 📦 Microservices (Phase 1)

| Service          | Status       | Description                              |
|------------------|--------------|------------------------------------------|
| 📝 `notes_service` | ✅ active     | REST API for note-taking                 |
| 👤 `users_service` | ✅ active     | REST API for user management             |
| 🔐 `auth_service`  | 🔜 planned    | JWT-based authentication (Node.js)       |
| 📊 `metrics_exporter` | 🔜 planned | Prometheus exporter                      |
| 🖼️ `frontend`      | 🔜 planned    | Web UI (e.g. Svelte)                     |

---

## 🧪 Local Setup

```bash
docker compose up --build
```

Then available at:  
👉 `http://localhost:8000/docs` (notes_service)  
👉 `http://localhost:8001/docs` (users_service – if split by port)

---

## 🚧 Next Steps

- Push images to Amazon ECR  
- Deploy to EKS via Helm or Kustomize  
- Use Sealed Secrets for secure config  
- Integrate Prometheus + Grafana monitoring  
- Add JWT Auth Service  
- Connect frontend

---

## 👩‍💻 About the Project

> Created by **Stella Joubert** as a public DevOps learning and reference project.

---

**DEUTSCH**

**OpsGarden** ist ein praktisches DevOps-Lernprojekt, das zeigt, wie man Microservices lokal entwickelt und später in eine skalierbare AWS-Umgebung (EKS) deployt – mit Fokus auf CI/CD, Infrastructure as Code und Observability.

---

## 🧰 Tech Stack

- **FastAPI** – Python-basierte Microservices (`notes_service`, `users_service`)
- **SQLModel** + **SQLite / PostgreSQL** – relationale Datenbanken
- **Docker** & **Docker Compose** – lokale Container-Orchestrierung
- **Terraform** – Infrastruktur-Code für VPC, EKS & Bastion Host
- **GitHub Actions** – automatisierte Tests und Builds
- *(Geplant: Helm, Kustomize, Prometheus, Grafana, Sealed Secrets)*

---

## ⚙️ CI/CD Pipelines

> GitHub Actions führen automatisiert Tests bei jedem Push oder Pull Request gegen `main` aus.

```yaml
# .github/workflows/docker-test.yml
env:
  DATABASE_URL: "sqlite:///:memory:"

steps:
  - uses: actions/checkout@v3
  - uses: actions/setup-python@v4
    with:
      python-version: '3.11'

  - name: Installiere Abhängigkeiten
    run: |
      pip install -r app/notes_service/requirements.txt

  - name: Starte Tests
    run: |
      cd app/notes_service
      pytest
```

💡 Es wird eine In-Memory-SQLite-Datenbank (`sqlite:///:memory:`) für schnelle isolierte Tests verwendet.

---

## 📦 Microservices (Phase 1)

| Service          | Status       | Beschreibung                             |
|------------------|--------------|------------------------------------------|
| 📝 `notes_service` | ✅ aktiv      | REST-API für Notizen                     |
| 👤 `users_service` | ✅ aktiv      | REST-API für Benutzerverwaltung          |
| 🔐 `auth_service`  | 🔜 geplant    | JWT-basierte Authentifizierung (Node.js) |
| 📊 `metrics_exporter` | 🔜 geplant | Prometheus Exporter                      |
| 🖼️ `frontend`      | 🔜 geplant    | Web-UI (z. B. Svelte)                    |

---

## 🧪 Lokales Setup

```bash
docker compose up --build
```

Erreichbar unter:  
👉 `http://localhost:8000/docs` (notes_service)  
👉 `http://localhost:8001/docs` (users_service – falls getrennt)

---

## 🚧 Nächste Schritte

- Container-Images nach Amazon ECR pushen  
- Deployment auf EKS via Helm oder Kustomize  
- Konfiguration absichern via Sealed Secrets  
- Prometheus + Grafana integrieren  
- Auth-Service mit JWT einbauen  
- Frontend anbinden

---

## 👩‍💻 Über das Projekt

> Erstellt von **Stella Joubert** als öffentliches DevOps-Lern- & Referenzprojekt.