from prometheus_client import start_http_server, Summary, Counter, Gauge
import time
import random

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
MY_COUNTER = Counter('my_counter',"Counter type metric", ["age"])
MY_GAUGE = Gauge('my_gauge',"Gauge type metric")

@REQUEST_TIME.time()
def process_request(t):
    MY_COUNTER.labels(age="20").inc(3)
    time.sleep(t);

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        random_var = random.random()
        process_request(random_var)
        MY_COUNTER.labels(age="20").inc()
        MY_GAUGE.set(random_var)
        MY_GAUGE.dec(4)
        MY_GAUGE.inc(5)

    print("Conclusion");
