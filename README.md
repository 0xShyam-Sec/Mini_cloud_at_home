# Mini Cloud at Home

A lightweight cloud infrastructure simulation using Docker, demonstrating core cloud concepts on local hardware. Production-like stack with reverse proxy, monitoring, and centralized logging — without cloud provider costs.

## What It Does

Spins up a complete cloud environment on your machine with a single command:

1. **Web App** served behind an Nginx reverse proxy
2. **Metrics collection** with Prometheus + Node Exporter
3. **Dashboards** with Grafana for real-time visualization
4. **Centralized logging** via Elasticsearch + Filebeat + Kibana
5. **Container orchestration** with Docker Compose

```
User request
     ↓
┌──────────┐     ┌──────────┐
│  Nginx   │────▶│ Flask App│
│  (proxy) │     │ (:5000)  │
└──────────┘     └──────────┘

Monitoring:
┌───────────────┐     ┌──────────┐     ┌──────────┐
│ Node Exporter │────▶│Prometheus│────▶│ Grafana  │
│ (metrics)     │     │ (:9090)  │     │ (:3000)  │
└───────────────┘     └──────────┘     └──────────┘

Logging:
┌──────────┐     ┌───────────────┐     ┌──────────┐
│ Filebeat │────▶│ Elasticsearch │────▶│ Kibana   │
│ (shipper)│     │ (:9200)       │     │ (:5601)  │
└──────────┘     └───────────────┘     └──────────┘
```

## Architecture

| Component | Purpose | Technology |
|-----------|---------|------------|
| Reverse Proxy | Request routing and load balancing | Nginx |
| Web App | Sample application | Flask (Python) |
| Metrics | System and container metrics collection | Prometheus + Node Exporter |
| Dashboards | Real-time visualization | Grafana |
| Log Aggregation | Collect logs from all containers | Filebeat |
| Log Storage | Index and search logs | Elasticsearch |
| Log Visualization | Explore and query logs | Kibana |
| Orchestration | Container management | Docker Compose |

## Project Structure

```
Mini_cloud_at_home/
├── app/
│   ├── Dockerfile           # Flask app container
│   ├── app.py               # Flask application
│   └── requirements.txt     # Python dependencies
├── nginx/
│   ├── Dockerfile           # Nginx container
│   └── nginx.conf           # Reverse proxy configuration
├── prometheus/
│   └── prometheus.yml       # Metrics scrape targets
├── filebeat/
│   └── filebeat.yml         # Log shipping configuration
├── kibana_config/
│   └── kibana.yml           # Kibana settings
├── docker-compose.yml       # Full stack orchestration
└── .env                     # Environment variables
```

## Services and Ports

| Service | URL | Purpose |
|---------|-----|---------|
| Web App | `http://localhost:5000` | Flask application |
| Nginx | `http://localhost:80` | Reverse proxy |
| Grafana | `http://localhost:3000` | Monitoring dashboards |
| Prometheus | `http://localhost:9090` | Metrics collection |
| Kibana | `http://localhost:5601` | Log visualization |
| Elasticsearch | `http://localhost:9200` | Log storage and search |
| Node Exporter | `http://localhost:9100` | System metrics |

## Setup

### Prerequisites

- Docker Engine `v20.10+`
- Docker Compose `v2.5+`
- 4GB+ RAM (8GB recommended for full stack)

### Quick Start

```bash
git clone https://github.com/0xShyam-Sec/Mini_cloud_at_home.git
cd Mini_cloud_at_home

cp .env.example .env
# Edit .env with your passwords

docker-compose up -d --build
```

### Shut Down

```bash
docker-compose down
```

### Adding New Services

1. Add service definition in `docker-compose.yml`
2. Configure proxy rules in `nginx/nginx.conf`
3. Add monitoring targets in `prometheus/prometheus.yml`

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Containers won't start | Ensure Docker is running and ports aren't in use |
| Grafana not loading | Wait 30 seconds after startup for all services to initialize |
| Filebeat permission error | Reset file permissions: delete `filebeat.yml`, recreate it, and set read-only permissions for your user |
| Elasticsearch out of memory | Increase Docker memory limit to 8GB in Docker Desktop settings |

## License

MIT
