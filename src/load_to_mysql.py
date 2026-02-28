import pandas as pd
import mysql.connector

# =========================
# MySQL connection
# =========================
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@123",
    database="tourism_flow"
)

cursor = conn.cursor()

# =========================
# Load CSV
# =========================
tourism_df = pd.read_csv("G:/tourism_flow_analytics/data/tourism_visitors.csv")
weather_df = pd.read_csv("G:/tourism_flow_analytics/data/weather.csv")

# Convert date
tourism_df["date"] = pd.to_datetime(tourism_df["date"]).dt.date
weather_df["date"] = pd.to_datetime(weather_df["date"]).dt.date

# =========================
# Insert tourism (chunked)
# =========================
tourism_sql = """
INSERT INTO tourism_visitors (visit_date, attraction, visitors)
VALUES (%s, %s, %s)
"""

chunk_size = 500
data = tourism_df.values.tolist()

for i in range(0, len(data), chunk_size):
    cursor.executemany(tourism_sql, data[i:i+chunk_size])
    conn.commit()

print("✅ Tourism inserted")

# =========================
# Insert weather
# =========================
weather_sql = """
INSERT INTO weather (weather_date, temperature, rainfall)
VALUES (%s, %s, %s)
"""

cursor.executemany(weather_sql, weather_df.values.tolist())
conn.commit()

print("✅ Weather inserted")

cursor.close()
conn.close()