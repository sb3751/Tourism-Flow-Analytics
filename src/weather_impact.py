import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# =========================
# MySQL connection
# =========================
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@123",
    database="tourism_flow"
)

# =========================
# Query joined data
# =========================
query = """
SELECT 
    t.visit_date,
    SUM(t.visitors) AS visitors,
    w.temperature,
    w.rainfall
FROM tourism_visitors t
JOIN weather w
ON t.visit_date = w.weather_date
GROUP BY t.visit_date, w.temperature, w.rainfall
ORDER BY t.visit_date;
"""

df = pd.read_sql(query, conn)
conn.close()

# =========================
# Correlation
# =========================
rain_corr = df["visitors"].corr(df["rainfall"])
temp_corr = df["visitors"].corr(df["temperature"])

print("Rainfall correlation:", round(rain_corr,3))
print("Temperature correlation:", round(temp_corr,3))

# =========================
# Scatter plots
# =========================
plt.figure()
plt.scatter(df["rainfall"], df["visitors"])
plt.xlabel("Rainfall")
plt.ylabel("Visitors")
plt.title("Rainfall vs Visitors")
plt.savefig("G:/tourism_flow_analytics/outputs/rain_vs_visitors.png")

plt.figure()
plt.scatter(df["temperature"], df["visitors"])
plt.xlabel("Temperature")
plt.ylabel("Visitors")
plt.title("Temperature vs Visitors")
plt.savefig("G:/tourism_flow_analytics/outputs/temp_vs_visitors.png")

plt.show()

print("✅ Weather impact charts saved")