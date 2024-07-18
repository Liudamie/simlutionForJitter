import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
data = {
    "W": [0, 2, 4, 6, 8, 10, 14, 20, 30, 40],
    "trade-off": [0.005, 0.007, 0.0147, 0.0198, 0.0241, 0.03333, 0.04198, 0.05843, 0.0867, 0.1178],
    "lossPacketRate": [0.145, 0.15, 0.15, 0.151, 0.1507, 0.1493, 0.1513, 0.1497, 0.1487, 0.1489]
}
df = pd.DataFrame(data)

# Create plot with both variables as line charts
fig, ax1 = plt.subplots()

# Plot trade-off as a line chart
ax1.plot(df['W'], df['trade-off'], color='b', marker='o', label='Trade-off')
ax1.set_xlabel('W')
ax1.set_ylabel('Trade-off', color='b')
ax1.tick_params('y', colors='b')
ax1.set_xticks(df['W'])  # Set x-ticks to only show data values
ax1.set_ylim(0, 0.13)  # Set y-axis range from 0 to 0.20

# Create another y-axis for lossPacketRate
ax2 = ax1.twinx()
ax2.plot(df['W'], df['lossPacketRate'], color='r', marker='o', label='Loss Packet Rate')
ax2.set_ylabel('Loss Packet Rate', color='r')
ax2.tick_params('y', colors='r')
ax2.set_ylim(0.1, 0.30)  # Set y-axis range from 0 to 0.20

fig.tight_layout()
plt.show()
