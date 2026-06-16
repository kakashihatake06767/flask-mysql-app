# Flask MySQL CI/CD Project

A complete DevOps project demonstrating CI/CD automation using:

- GitHub
- Jenkins
- Docker
- Docker Compose
- Flask
- MySQL
- Linux
- SSH-based Deployment

---

## Architecture

```mermaid
flowchart TD

    DEV[Developer]

    GH[GitHub Repository]

    JENKINS[Jenkins Server]

    APP[Application Server]

    DOCKER[Docker Compose]

    FLASK[Flask Container]

    MYSQL[MySQL Container]

    DEV -->|git push| GH

    GH --> JENKINS

    JENKINS -->|SSH| APP

    APP -->|git pull| GH

    APP -->|docker compose up -d --build| DOCKER

    DOCKER --> FLASK
    DOCKER --> MYSQL
