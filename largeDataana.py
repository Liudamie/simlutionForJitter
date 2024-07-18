import pandas as pd
import os

# Function to compute the desired value for each row
def compute_value(row):
    indices = range(1, len(row) + 1)  # Start indices from 1
    weighted_sum = sum(row * indices)
    sum_of_values = sum(row)
    return weighted_sum / sum_of_values if sum_of_values != 0 else 0

# Directory containing the Excel files
directory = 'liu_data_result_100/'

# List to hold the results
results = []

# Process each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(directory, filename)

        # Load the Excel file
        df = pd.read_excel(file_path)
        excel_data = pd.ExcelFile(file_path)

        # Drop the first two columns
        df = df.drop(df.columns[:2], axis=1)

        # Apply the function to each row
        df['Computed Value'] = df.apply(compute_value, axis=1)

        # Drop the first row if needed
        df = df.drop(0)

        # Calculate the average of the computed values
        average_computed_value = df['Computed Value'].mean()

        # Read the 'invalidRate' sheet
        invalid_rate_data = excel_data.parse('invalidRate')
        invalid_rate_data = invalid_rate_data.drop(invalid_rate_data.columns[0], axis=1)

# Remove the rows where the index is 0
        invalid_rate_data_cleaned = invalid_rate_data[invalid_rate_data.iloc[:, 0] != 0].reset_index(drop=True)

# Calculate the mean for the cleaned 'invalidRate' data
        invalid_rate_mean = invalid_rate_data_cleaned.mean().values[0]
        print(invalid_rate_mean)

        # Append the results to the list
        results.append({'Filename': filename, 'Average Computed Value': average_computed_value, 'Invalid Rate Mean': invalid_rate_mean})

# Convert the results to a DataFrame
results_df = pd.DataFrame(results)

# Output the results to a new Excel file
output_file_path = 'results_summary.xlsx'
results_df.to_excel(output_file_path, index=False)

# Display the results
print(results_df)
