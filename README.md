# compose-nginx-flask-redis

Docker Compose stack: **Flask** app + **Redis** + **Nginx** reverse proxy.

## Run

```bash
docker compose up --build
# App via Nginx:
#   http://localhost:8080/
# App direct:
#   http://localhost:8000/
```
