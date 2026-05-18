from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime

producer=KafkaProducer(
bootstrap_servers='localhost:9092',
value_serializer=lambda x:
json.dumps(x).encode('utf-8')
)

stocks=['AAPL','TSLA','MSFT','NVDA']

while True:

    event={
        'symbol':random.choice(stocks),
        'price':round(random.uniform(100,500),2),
        'timestamp':str(datetime.now())
    }

    producer.send(
        'stock-topic',
        value=event
    )

    print(event)

    time.sleep(2)
