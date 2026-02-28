import pandas as pd
import matplotlib.pyplot as plt

# =========================
# Load flows
# =========================
df = pd.read_csv("G:/tourism_flow_analytics/data/mobility_flows.csv")

# =========================
# Top flows
# =========================
top_flows = df.sort_values("count", ascending=False).head(10)

print("\nTop tourism flows:\n")
print(top_flows)

# =========================
# Plot
# =========================
labels = top_flows["source"] + " → " + top_flows["destination"]

plt.figure()
plt.barh(labels, top_flows["count"])
plt.title("Top Tourism Mobility Flows")
plt.xlabel("Movement Count")

plt.savefig("G:/tourism_flow_analytics/outputs/top_mobility_flows.png")
plt.show()

print("✅ Flow chart saved")