# Visitor Counter (Docker + Docker Compose)

A small multi-container web app: a Python Flask server that counts page visits, with the count stored in a separate Redis container.

## What it demonstrates
- A custom image built from a `Dockerfile`
- Two services running together with `docker-compose.yml`
- Container-to-container networking (the app reaches the database by the service name `redis`)
- A named volume (`redis-data`) so the count survives `docker compose down` / `up`
- Configuration through an environment variable (`APP_NAME`)

## Run it
Requires [Docker Desktop](https://www.docker.com/products/docker-desktop/).

```
docker compose up --build
```

Then open http://localhost:5000 and refresh to watch the count go up. Stop it with `docker compose down`; the count is kept the next time you start it.
