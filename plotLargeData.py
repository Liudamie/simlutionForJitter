import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Load the data from the uploaded Excel files
file_25 = 'simData25.xlsx'
file_50 = 'simData50.xlsx'
file_75 = 'simData75.xlsx'
file_100 = 'simData100.xlsx'

# Read the Excel files
df_25 = pd.read_excel(file_25)
df_50 = pd.read_excel(file_50)
df_75 = pd.read_excel(file_75)
df_100 = pd.read_excel(file_100)

# Combine all dataframes into one for easier plotting
df_combined = pd.concat([df_25, df_50, df_75, df_100], keys=['25', '50', '75', '100'], names=['Set'])
filename_indices = np.arange(len(df_25['Filename']))

# Create a figure and a set of subplots
fig, ax1 = plt.subplots(figsize=(14, 8))

# Adjust the position of bars to separate them and increase the width
bar_width = 0.4# Width of each bar
offset = {'25': -1.5*bar_width, '50': -0.5*bar_width, '75': 0.5*bar_width, '100': 1.5*bar_width}

# Plot bar chart for Average Computed Value with increased width and separation
colors = {'25': 'b', '50': 'g', '75': 'r', '100': 'c'}
for key, group in df_combined.groupby('Set'):
    ax1.bar(group['Filename'] + offset[key], group['Average Computed Value'], label=f'Average of Consecutive Ranging Failures from {key} robots', alpha=0.7, color=colors[key], width=bar_width)

# Set labels for the bar chart

ax1.set_xlabel('W',size=18)
ax1.set_ylabel('Average of Consecutive Ranging Failures', color='black', fontsize=20)
ax1.tick_params(axis='y', labelcolor='black',labelsize=18)
ax1.set_xticks(np.arange(0, 61, 2),size=16)
# Create a second y-axis to plot the line chart
ax2 = ax1.twinx()

# Plot line chart for Invalid Rate Mean with proper alignment
for key, group in df_combined.groupby('Set'):
    ax2.plot(group['Filename'], group['Invalid Rate Mean'] * 100, label=f'Ratio of trade-off ranging from {key} robots', linestyle='-', marker='o', color=colors[key])

# Set labels for the line chart(%)
ax2.set_ylabel('Ratio of trade-off ranging (%)', color='black', fontsize=20)

ax2.tick_params(axis='y', labelcolor='black',labelsize=18)

# Add legends
fig.legend(loc='upper left', bbox_to_anchor=(0.55,0.35), bbox_transform=ax1.transAxes)

# Show plot
plt.show()
