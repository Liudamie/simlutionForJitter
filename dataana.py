import pandas as pd

# Load the Excel file
file_path = 'liu_data_result_25/25_100ms_0j_500.0s_0.xlsx'
df = pd.read_excel(file_path)
excel_data = pd.ExcelFile(file_path)
# Drop the first two columns
df = df.drop(df.columns[:2], axis=1)

# Function to compute the desired value for each row
def compute_value(row):
    indices = range(1, len(row) + 1)  # Start indices from 1
    weighted_sum = sum(row * indices)
    sum_of_values = sum(row)
    return weighted_sum / sum_of_values if sum_of_values != 0 else 0

# Apply the function to each row
df['Computed Value'] = df.apply(compute_value, axis=1)
df = df.drop(0)
print(df['Computed Value'])

# Calculate the average of the computed values
average_computed_value = df['Computed Value'].mean()
average_computed_value
print("average",average_computed_value)

invalid_rate_data = excel_data.parse('invalidRate')

# Remove the rows where the index is 0
invalid_rate_data_cleaned = invalid_rate_data[invalid_rate_data['Unnamed: 0'] != 0].reset_index(drop=True)

# Calculate the mean for the cleaned 'invalidRate' data
invalid_rate_mean = invalid_rate_data_cleaned.mean()

print(invalid_rate_mean)
