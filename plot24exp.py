import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the uploaded Excel file
file_path = 'realworldata.xlsx'
data = pd.read_excel(file_path)

# Enhanced version of the separate graphs for better aesthetics
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Consecutive plot
axs[0, 0].plot(data['W'], data['consecutive'], marker='o', linestyle='-', color='b', linewidth=2)

axs[0, 0].set_xlabel('W', fontsize=12)
axs[0, 0].set_ylabel('Average of Consecutive Ranging Failures ', fontsize=16)
axs[0, 0].grid(True)

# Max plot
axs[0, 1].plot(data['W'], data['max'], marker='s', linestyle='-', color='g', linewidth=2)

axs[0, 1].set_xlabel('W', fontsize=12)
axs[0, 1].set_ylabel('Maximum value of consecutive ranging failures', fontsize=16)
axs[0, 1].grid(True)

# Trade-off plot
axs[1, 0].plot(data['W'], data['trade-off'], marker='^', linestyle='-', color='r', linewidth=2)
axs[1, 0].set_xlabel('W', fontsize=12)
axs[1, 0].set_ylabel('Ratio Trade-off Ranging (%)', fontsize=16)
axs[1, 0].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0%}'))
axs[1, 0].grid(True)

# Loss Packet Rate plot
axs[1, 1].plot(data['W'], data['lossPacketRate'], marker='x', linestyle='-', color='m', linewidth=2)
axs[1, 1].set_xlabel('W', fontsize=12)
axs[1, 1].set_ylabel('Loss Packet Rate (%)', fontsize=16)
axs[1, 1].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.1%}'))
axs[1, 1].grid(True)

# Main title and layout adjustments
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
