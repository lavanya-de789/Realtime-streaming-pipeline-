# Real-Time Stock Streaming Platform

Architecture

Producer
↓
Kafka
↓
Spark Structured Streaming
↓
Bronze Layer
↓
Analytics

Tech Stack

Python
Kafka
Spark
Airflow
Docker

Features

Real-time stock data generation
Kafka streaming ingestion
Spark Structured Streaming
Parquet output
Airflow orchestration

How to run

Step 1

docker-compose up -d

Step 2

python producer/stock_producer.py

Step 3

spark-submit spark/stream_job.py

Step 4

airflow standalone

Future Improvements

AWS S3
Apache Iceberg
Snowflake
dbt
Great Expectations
Kubernetes
CI/CD
