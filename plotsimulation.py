import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# Load the uploaded Excel file
file_path = 'simlutiondata.xlsx'
data = pd.read_excel(file_path, sheet_name='Sheet1')

# Define the first formula based on the provided image
def first_formula(W, P=60):
    return (1 / (6 * P)) * (W * (W**2 + 3*W + 2) / (W + 1)**2)

# Define the second formula based on the provided image
def second_formula(W):
    return 1 + (2 / (W + 1)) + (1 / (W**2 + W))

# Compute the values for W based on the data's x-axis values
W_values = data['Unnamed: 0']
P = 60
first_formula_values = first_formula(W_values, P)
second_formula_values = second_formula(W_values)

# Plotting the data with both formulas and adjusted y-axis and x-axis labels, without the inset
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot continousrangingfailure and second formula with left y-axis on the main plot
ax1.set_xlabel('W (Index)')
ax1.set_ylabel('continousrangingfailure / second formula', color='tab:blue')
ax1.plot(W_values, data['continousrangingfailure'], color='tab:blue', label='continousrangingfailure')
ax1.plot(W_values, second_formula_values, color='tab:orange', label='Second Formula')
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.set_yticks([0, 1, 2, 5, 10, 15, 20, 25, 30, 35, 40])

# Set x-ticks to even numbers only and limit W from 0 to 40 with some padding
ax1.set_xticks(range(0, 41, 2))
ax1.set_xlim([-2, 42])  # Add padding to the left and right of the x-axis

# Remove gridlines
ax1.grid(False)

# Create a second y-axis to plot tradeoffranging and first formula on the main plot
ax2 = ax1.twinx()
ax2.set_ylabel('tradeoffranging / first formula', color='tab:red')
ax2.plot(W_values, data['tradeoffranging'], color='tab:red', label='tradeoffranging')
ax2.plot(W_values, first_formula_values, color='tab:green', label='First Formula')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Ensure the scales start from the same point but have different ranges
ax1.set_ylim(0, 45)
ax2.set_ylim(0, 0.12)

# Remove gridlines for the second y-axis
ax2.grid(False)

# Add a title and legend
ax1.set_title('Continous Ranging Failure, Tradeoff Ranging, and Both Formulas')
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), bbox_transform=ax1.transAxes)

# Show the plot
plt.show()