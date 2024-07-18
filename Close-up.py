# Create a separate plot for the zoomed-in section
import pandas as pd
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

fig, ax = plt.subplots(figsize=(8, 6))

# Plot continousrangingfailure and second formula for the zoomed-in section
ax.plot(W_values, data['continousrangingfailure'], color='tab:blue')
ax.plot(W_values, second_formula_values, color='tab:orange')
ax.set_xlim(0, 10)
ax.set_ylim(0, 2)
ax.set_xticks(range(0, 11, 2))
ax.set_yticks([0, 0.5, 1, 1.5, 2])
ax.set_xlabel('W (Index)')
#ax.set_ylabel('continousrangingfailure / second formula', color='tab:blue')
ax.tick_params(axis='y', labelcolor='tab:blue')
ax.set_title('Zoomed Section')

# Add legend
ax.legend()

# Show the plot
plt.show()
