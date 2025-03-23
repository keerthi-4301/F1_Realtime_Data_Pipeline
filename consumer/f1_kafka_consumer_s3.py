from kafka import KafkaConsumer
import json
import boto3

# 🚀 AWS S3 Configuration
S3_BUCKET = "f1-realtime-data"  # Replace with your actual S3 bucket name
S3_FILE_NAME = "f1_race_data.json"
s3 = boto3.client("s3")

# 🚀 Kafka Configuration
KAFKA_BROKER = "44.202.253.25:9092"

consumer = KafkaConsumer(
    "f1_race_data",
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

collected_data = []

print("🎧 Listening for real-time F1 data...")

for message in consumer:
    print(f"✅ Received from Kafka: {message.value}")  # 🔥 Debugging Print Statement
    collected_data.append(message.value)

    if len(collected_data) >= 10:
        print("🚀 Attempting to save data to S3...")  # 🔥 Add this debug statement

        try:
            s3.put_object(
                Bucket=S3_BUCKET,
                Key=S3_FILE_NAME,
                Body=json.dumps(collected_data, indent=4)
            )
            print(f"✅ Data successfully saved to S3: {S3_BUCKET}/{S3_FILE_NAME}")
            collected_data = []
        except Exception as e:
            print(f"❌ Error saving to S3: {str(e)}")  # 🔥 Print any errors
