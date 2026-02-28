import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

np.random.seed(42)

# -----------------------------
# Config
# -----------------------------
start_date = datetime(2024, 1, 1)
days = 365

attractions = [
    "Tokyo Tower",
    "Shibuya Crossing",
    "Fushimi Inari Shrine",
    "Arashiyama Bamboo Grove",
    "Osaka Castle",
    "Nara Park",
    "Sensoji Temple"
]

# -----------------------------
# Generate tourism demand
# -----------------------------
records = []

for i in range(days):
    date = start_date + timedelta(days=i)

    for attr in attractions:
        base = np.random.randint(200, 800)

        # seasonality boost
        if date.month in [3,4]:  # Sakura
            base += 300
        if date.month in [10,11]:
            base += 200

        visitors = max(50, int(np.random.normal(base, 80)))

        records.append([date, attr, visitors])

tourism_df = pd.DataFrame(records, columns=["date","attraction","visitors"])

# -----------------------------
# Generate weather
# -----------------------------
weather = []

for i in range(days):
    date = start_date + timedelta(days=i)

    temp = np.random.normal(18, 8)
    rain = max(0, np.random.normal(3, 5))

    weather.append([date, temp, rain])

weather_df = pd.DataFrame(weather, columns=["date","temperature","rainfall"])

# -----------------------------
# Save
# -----------------------------
os.makedirs("G:/tourism_flow_analytics/data", exist_ok=True)

tourism_df.to_csv("G:/tourism_flow_analytics/data/tourism_visitors.csv", index=False)
weather_df.to_csv("G:/tourism_flow_analytics/data/weather.csv", index=False)

print("✅ Data generated")