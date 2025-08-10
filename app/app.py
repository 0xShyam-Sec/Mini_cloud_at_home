from flask import Flask, request
from elasticsearch import Elasticsearch
import datetime
import os
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
es = Elasticsearch(os.getenv('ES_HOST', 'http://elasticsearch:9200'), basic_auth=('elastic', os.getenv('ES_PASSWORD')))
metrics = PrometheusMetrics(app)

@app.route('/')
def home():
    log_entry = {
        "@timestamp": datetime.timezone.utcnow().isoformat(),
        "message": "User accessed /",
        "level": "info",
        "client_ip": request.remote_addr
    }
    es.index(index="logs-flask", document=log_entry)
    return "Hello from Mini Cloud!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)