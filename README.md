# 🌩️ Mini Cloud at Home – Scalable Cloud Environment Simulation

[![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Nginx](https://img.shields.io/badge/NGINX-269539?style=flat&logo=nginx&logoColor=white)](https://nginx.org)
[![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat&logo=prometheus&logoColor=white)](https://prometheus.io)
[![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat&logo=grafana&logoColor=white)](https://grafana.com)
[![ELK Stack](https://img.shields.io/badge/ELK%20Stack-005571?style=flat&logo=elasticstack&logoColor=white)](https://www.elastic.co/what-is/elk-stack)

A lightweight **cloud infrastructure simulation** using Docker, demonstrating core cloud concepts on local hardware. Perfect for learning cloud architecture, DevOps practices, and infrastructure monitoring without cloud provider costs.


## 🚀 Key Features

- **Production-like cloud stack** on a single machine
- **HTTPS reverse proxy** with Nginx
- **Multi-container isolation** with Docker Compose
- **Real-time monitoring** with Prometheus + Grafana
- **Centralized logging** via ELK Stack (Elasticsearch + Kibana)
- **Infrastructure-as-Code** configuration
- **Persistent storage** with volumes

## 🏗️ Architecture Components

|     Component     |       Purpose                    |     Technology     |
| ----------------- | -------------------------------- | ------------------ |
| **Reverse Proxy** | SSL termination & load balancing |      Nginx         |
| **Web App**       | Sample application               |      Flask         |
| **Monitoring**    | Metrics collection & dashboard   | Prometheus+Grafana |
| **Logging**       | Log aggregation & visualization  |      ELK Stack     |
| **Orchestration** | Container management             | Docker Compose     |

## 🛠️ Prerequisites

- Docker Engine `v20.10+`
- Docker Compose `v2.5+`
- 4GB+ RAM (8GB recommended for full stack)

## 🏁 Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mini-cloud-at-home.git
   cd mini-cloud-at-home
   ```
2. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env file as needed
   ```
3. Start the stack:
   ```bash
   docker-compose up -d --build
   ```
4. Access the services:
   - Web App: `http://localhost:5000`
   - Grafana: `http://localhost:3000`
   - Kibana: `http://localhost:5601`
   - Prometheus: `http://localhost:9090`
   - Elasticsearch: `http://localhost:9200`

## 🔧 Customization

### Adding New Services

    - Add service definition in `docker-compose.yml`
    - Configure proxy rules in `nginx/conf.d/`
    - Add monitoring targets in `prometheus/prometheus.yml`

### Using Your Own Web App

Replace the contents of `app/` with your application code.

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

NOTE: To successfully edit and save changes in the `filebeat.yml` file, you may need to adjust file permissions or use a text editor with elevated privileges.

Temporary solution:

1. Copy present contents of `filebeat.yml` to a new file.
2. Delete the original `filebeat.yml`.
3. Create a new `filebeat.yml` file and paste the copied contents.
4. Run following commands in command prompt to finalize the changes:
   ```bash
    cd F:\Projects\mini-cloud\filebeat
    icacls filebeat.yml /remove:g *S-1-1-0
    icacls filebeat.yml /inheritance:r
    icacls filebeat.yml /grant "%USERNAME%:R"
   ```
