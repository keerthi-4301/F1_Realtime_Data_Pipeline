from kafka import KafkaProducer
import fastf1
import json
import time

# 🚀 Kafka Broker (Use your EC2 Public IP)
KAFKA_BROKER = "44.202.253.25:9092"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# 🔥 List of all F1 2024 races (modify if needed)
races = [
    "Bahrain", "Jeddah", "Australia", "Japan", "China",
    "Miami", "Imola", "Monaco", "Canada", "Spain",
    "Austria", "Silverstone", "Hungary", "Belgium", "Netherlands",
    "Monza", "Singapore", "USA", "Mexico", "Brazil", "Las Vegas",
    "Qatar", "Abu Dhabi"
]

def fetch_and_send_f1_data():
    print("📡 Fetching F1 race data for the entire 2024 season...")

    for race in races:
        print(f"\n🚀 Fetching race data for {race} GP...")
        session = fastf1.get_session(2024, race, "Race")
        session.load()

        for index, row in session.results.iterrows():
            race_data = {
                "race": race,  # Include race name
                "driver": row["Abbreviation"],
                "position": row["Position"],
                "points": row["Points"],
                "team": row["TeamName"]
            }

            producer.send("f1_race_data", race_data)
            print(f"✅ Sent to Kafka: {race_data}")

            time.sleep(1)  # Simulate real-time updates

if __name__ == "__main__":
    fetch_and_send_f1_data()
