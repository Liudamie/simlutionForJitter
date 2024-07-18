import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the uploaded Excel file
file_path = 'realworldata.xlsx'
data = pd.read_excel(file_path)

# Enhanced version of the separate graphs for better aesthetics, with percentage y-axis for third and fourth graphs
fig, axs = plt.subplots(1, 1, figsize=(12, 16))

# Plot 2: Max and Loss Packet Rate
ax3 = axs[1]
ax3.plot(data['W'], data['max'], marker='s', linestyle='-', color='g', linewidth=2, label='Max')
ax3.set_xlabel('W', fontsize=12)
ax3.set_ylabel('Maximum value of consecutive ranging failures', fontsize=18, color='g')
ax3.tick_params(axis='y', labelcolor='g',labelsize=16)
ax3.tick_params(axis='x', labelsize=16)
ax3.grid(True)

ax4 = ax3.twinx()
ax4.plot(data['W'], data['lossPacketRate'], marker='x', linestyle='-', color='m', linewidth=2, label='Loss Packet Rate')
ax4.set_ylabel('Loss Packet Rate (%)', fontsize=18, color='m')
ax4.tick_params(axis='y', labelcolor='m', labelsize=16)
ax4.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.1%}'))
ax4.yaxis.set_major_locator(plt.MultipleLocator(0.001))


# Main title and layout adjustments
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
