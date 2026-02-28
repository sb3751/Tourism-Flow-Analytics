import pandas as pd
import numpy as np
import os

np.random.seed(42)

attractions = [
    "Tokyo Tower",
    "Shibuya Crossing",
    "Fushimi Inari Shrine",
    "Arashiyama Bamboo Grove",
    "Osaka Castle",
    "Nara Park",
    "Sensoji Temple"
]

flows = []

for _ in range(2000):
    src = np.random.choice(attractions)
    dst = np.random.choice(attractions)

    if src != dst:
        flows.append([src, dst])

df = pd.DataFrame(flows, columns=["source","destination"])

flow_counts = df.value_counts().reset_index(name="count")

os.makedirs("G:/tourism_flow_analytics/data", exist_ok=True)
flow_counts.to_csv("G:/tourism_flow_analytics/data/mobility_flows.csv", index=False)

print("✅ Mobility flows generated")