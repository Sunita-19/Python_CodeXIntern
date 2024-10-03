# Import necessary libraries
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('D:\\Python_Internship\\Python_CodeXIntern\\Python_CodeXIntern\\EV.csv')


# Display the first 5 rows of the data
print("First 5 rows of the dataset:")
print(df.head())

# Display column names
print("\nColumns in the dataset:")
print(df.columns)

# Get basic statistics for numeric columns
print("\nBasic statistics of the dataset:")
print(df.describe())

# Calculate the average (mean) of a specific column (replace 'column_name' with your actual column name)
average = df['Energy Consumed (kWh)'].mean()
print(f"\nThe average of the column 'column_name' is: {average}")

# Calculate the total sum of the column
total_sum = df['Energy Consumed (kWh)'].sum()
print(f"\nThe total sum of the column 'column_name' is: {total_sum}")

# Count the number of non-null entries in the column
count = df['Energy Consumed (kWh)'].count()
print(f"\nTotal non-null entries in the column 'column_name': {count}")

# Find the maximum and minimum values of the column
max_value = df['Energy Consumed (kWh)'].max()
min_value = df['Energy Consumed (kWh)'].min()
print(f"\nThe maximum value in the column 'column_name' is: {max_value}")
print(f"The minimum value in the column 'column_name' is: {min_value}")

# Filter rows where the values in 'column_name' are greater than 50
filtered_data = df[df['Energy Consumed (kWh)'] > 50]
print(f"\nRows where the 'column_name' is greater than 50:")
print(filtered_data)

# Group the data by another column (replace 'group_column' with your actual column) and find the mean of 'column_name'
grouped_data = df.groupby('Vehicle Model')['Energy Consumed (kWh)'].mean()
print(f"\nAverage of 'Energy Consumed (kWh)' grouped by 'Vehicle Model':")
print(grouped_data)

# Save the filtered data to a new CSV file
filtered_data.to_csv('Filtered_data.csv', index=False)
print("\nFiltered data saved to 'filtered_data.csv'.")
