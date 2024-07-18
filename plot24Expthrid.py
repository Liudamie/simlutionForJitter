import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the uploaded Excel file
file_path = 'realworldata.xlsx'
data = pd.read_excel(file_path)

fig, ax1 = plt.subplots(figsize=(14, 8))

# Bar width
bar_width = 0.4

# Positions of the bars on the x-axis
r1 = range(len(data['W']))
r2 = [x + bar_width for x in r1]

# Bar plot for 'consecutive' vs 'W'
bars1 = ax1.bar(r1, data['consecutive'], color='green', width=bar_width, label='Consecutive')

# Creating a second y-axis
ax2 = ax1.twinx()

# Bar plot for 'max' vs 'W' on the second y-axis
bars2 = ax2.bar(r2, data['max'], color='red', width=bar_width, label='Max', alpha=1)

# Setting titles and labels
ax1.set_xlabel('W',fontsize=18)
ax1.set_ylabel('Average of Consecutive Ranging Failures', color='green', fontsize=18)
ax2.set_ylabel('Maximum value of consecutive ranging failures', color='red', fontsize=18)
ax2.set_ylim(0, 126)
ax2.set_yticks([2, 5, 10, 20, 50, 100, 120])

# Adding legends
bars = [bars1[0], bars2[0]]
labels = ['Average of Consecutive Ranging Failures','Maximum value of consecutive ranging failures']
ax1.legend(bars, labels, loc='upper right', fontsize='18')

# Setting the x-axis ticks to the middle of the bars
ax1.set_xticks([r + bar_width / 2 for r in range(len(data['W']))])
ax1.set_xticklabels(data['W'])

# Setting the color of the y-axis labels to match the bar colors
ax1.tick_params(axis='y', labelcolor='green',labelsize=16)
ax2.tick_params(axis='y', labelcolor='red',labelsize=16)
ax1.tick_params(axis='x', labelsize=14)
# Enabling gridlines
ax1.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5)
ax2.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5)

plt.show()
