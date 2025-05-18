from prometheus_client import start_http_server, Counter, Gauge

# Метрики
MESSAGES_COUNT = Counter('bot_messages', 'Total messages processed')
ERRORS_COUNT = Counter('bot_errors', 'Total errors occurred')

def setup_metrics(port=8000):
    start_http_server(port)