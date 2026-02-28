import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@123",
    database="tourism_flow"
)

query = """
SELECT attraction, SUM(visitors) AS total_visitors
FROM tourism_visitors
GROUP BY attraction
ORDER BY total_visitors DESC;
"""

df = pd.read_sql(query, conn)
conn.close()

plt.figure()
plt.bar(df["attraction"], df["total_visitors"])
plt.xticks(rotation=45)
plt.title("Attraction Popularity")
plt.ylabel("Visitors")

plt.savefig("G:/tourism_flow_analytics/outputs/attraction_popularity.png")
plt.show()

print("✅ Attraction chart saved")