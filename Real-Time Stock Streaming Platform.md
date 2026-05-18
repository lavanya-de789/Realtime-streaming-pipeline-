# Real-Time Stock Streaming Platform



This project demonstrates an end-to-end real-time data engineering pipeline built using Kafka, Spark Structured Streaming, Airflow, and Docker.



The system simulates live stock market events and processes streaming data through a scalable event-driven architecture. Data is ingested into Kafka topics, consumed and transformed by Spark Structured Streaming, and stored in a bronze layer for downstream analytics.



Architecture:



Data Producer

↓

Kafka

↓

Spark Structured Streaming

↓

Bronze Storage Layer

↓

Airflow Orchestration

↓

Analytics \& Future Processing



Tech Stack:



\- Python

\- Apache Kafka

\- PySpark

\- Apache Airflow

\- Docker

\- Parquet Storage



Key Features:



\- Real-time event generation

\- Kafka-based streaming ingestion

\- Stream processing using Spark Structured Streaming

\- Fault-tolerant architecture

\- Bronze layer storage design

\- Workflow orchestration with Airflow

\- Scalable pipeline design



Future Enhancements:



\- Apache Iceberg integration

\- AWS S3 data lake storage

\- Snowflake warehouse integration

\- dbt transformations

\- Great Expectations data quality checks

\- Kubernetes deployment

\- CI/CD automation

