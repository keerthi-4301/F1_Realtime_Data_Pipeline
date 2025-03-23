# 🏎️ F1 Real-Time Data Pipeline (Kafka + AWS + Airflow + Snowflake)

🚀 A real-time data pipeline that streams Formula 1 race data using [FastF1](https://theoehrly.github.io/Fast-F1/), processes it with Apache Kafka, stores it in AWS S3, and loads it into Snowflake — all orchestrated using Apache Airflow. The entire pipeline is built and deployed on AWS EC2.

---

## 📊 Project Overview

This project simulates a real-time data engineering workflow using Formula 1 race data. It demonstrates how data flows from extraction to transformation to storage and analytics — using industry-standard tools.

---

## 🧱 Tech Stack

| Tool              | Purpose                                 |
|-------------------|------------------------------------------|
| 🐍 Python          | Core scripting                          |
| 🏎️ FastF1          | Fetching real-time race data            |
| 📨 Apache Kafka    | Real-time message streaming             |
| ☁️ AWS S3          | Cloud storage for JSON files            |
| ❄️ Snowflake       | Cloud data warehouse for querying       |
| 🪂 Apache Airflow  | Pipeline orchestration & automation     |
| 💻 EC2             | Host Kafka, Airflow, and Python scripts |

---

## 🔁 End-to-End Pipeline Flow

```text
FastF1 (Python API)
       |
       v
Kafka Producer → Kafka Topic → Kafka Consumer
                                 |
                                 v
                           AWS S3 (JSON)
                                 |
                                 v
                       Snowflake Table (f1_results)
```

---
## How It Works
🏁 1. Producer (f1_kafka_producer.py)
Uses FastF1 to fetch 2024 race results

Streams each driver’s data to a Kafka topic

📦 2. Consumer (f1_kafka_s3_consumer.py)
Listens to the Kafka topic

Batches every 10 messages and uploads to S3 as JSON

❄️ 3. Snowflake Loader (f1_snowflake_loader.py)
Loads the S3 JSON data into a Snowflake table (f1_results)

🪂 4. Airflow DAG (f1_pipeline_dag.py)
Automates the pipeline in 3 tasks:

Run producer

Run consumer

Load to Snowflake


