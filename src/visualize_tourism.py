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
# Query monthly tourism
# =========================
query = """
SELECT 
    MONTH(visit_date) AS month,
    SUM(visitors) AS total_visitors
FROM tourism_visitors
GROUP BY MONTH(visit_date)
ORDER BY month;
"""

df = pd.read_sql(query, conn)

conn.close()

# =========================
# Plot
# =========================
plt.figure()
plt.plot(df["month"], df["total_visitors"], marker='o')

plt.title("Monthly Tourism Demand")
plt.xlabel("Month")
plt.ylabel("Visitors")

plt.savefig("G:/tourism_flow_analytics/outputs/monthly_tourism.png")
plt.show()

print("✅ Chart saved")