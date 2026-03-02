# Production Docker Monitoring Setup

## Architecture

```
┌─────────────┐     ┌─────────────┐
│   FastAPI   │────▶│  Prometheus │
│   :8000     │     │   :9090     │
└─────────────┘     └──────┬──────┘
                           │
┌─────────────┐            │
│  Streamlit  │            ▼
│   :8501     │     ┌─────────────┐
└─────────────┘     │   Grafana   │
                    │   :3000     │
                    └─────────────┘
```

## Services

- **FastAPI**: Port 8000 - API with /metrics endpoint
- **Streamlit**: Port 8501 - Frontend dashboard
- **Prometheus**: Port 9090 - Metrics collection (scrapes every 5s)
- **Grafana**: Port 3000 - Visualization (admin/admin)

## Quick Start

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

## Access URLs

- FastAPI: http://localhost:8000
- FastAPI Metrics: http://localhost:8000/metrics
- Streamlit: http://localhost:8501
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (admin/admin)

## Folder Structure

```
.
├── docker-compose.yml
├── prometheus.yml
├── grafana/
│   └── provisioning/
│       ├── datasources/
│       │   └── prometheus.yml
│       └── dashboards/
│           ├── dashboard.yml
│           └── fastapi-dashboard.json
├── app/
│   └── api.py
├── model/
├── data/
└── requirements.txt
```

## Features

✅ Docker service names (no localhost)
✅ Prometheus scrapes FastAPI every 5s
✅ Grafana auto-connects to Prometheus
✅ Persistent volumes for data
✅ Restart policies (unless-stopped)
✅ Health checks for FastAPI
✅ Custom network for isolation
✅ Pre-configured FastAPI dashboard

## Monitoring Details

### Prometheus Configuration
- Scrape interval: 5 seconds
- Target: fastapi:8000/metrics
- Storage: prometheus_data volume

### Grafana Configuration
- Auto-provisioned Prometheus datasource
- Pre-loaded FastAPI dashboard
- Credentials: admin/admin
- Storage: grafana_data volume

## Troubleshooting

```bash
# Check service status
docker-compose ps

# View specific service logs
docker-compose logs fastapi
docker-compose logs prometheus
docker-compose logs grafana

# Restart a service
docker-compose restart fastapi

# Rebuild and restart
docker-compose up -d --build
```

## Metrics Available

- `http_requests_total` - Total HTTP requests
- `http_request_duration_seconds` - Request duration histogram
- `http_requests_created` - Request creation timestamp
- Custom metrics from prometheus-fastapi-instrumentator

## Production Notes

- Change Grafana admin password in docker-compose.yml
- Configure alerting rules in Prometheus
- Set up retention policies for metrics
- Use secrets management for sensitive data
- Consider adding nginx reverse proxy
- Implement backup strategy for volumes
