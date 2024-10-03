import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (update the file path if necessary)
file_path = 'D:/Python_Internship/EV.csv'  # Make sure this is the correct file path
data = pd.read_csv(file_path)

# Set plot style
sns.set(style="whitegrid")

# 1. Bar Chart: Average Energy Consumed by Vehicle Model
plt.figure(figsize=(10, 6))
avg_energy_consumed = data.groupby('Vehicle Model')['Energy Consumed (kWh)'].mean().sort_values()
sns.barplot(x=avg_energy_consumed.values, y=avg_energy_consumed.index, hue=avg_energy_consumed.index, palette="viridis", legend=False)
plt.title('Average Energy Consumed by Vehicle Model', fontsize=14)
plt.xlabel('Average Energy Consumed (kWh)')
plt.ylabel('Vehicle Model')
plt.show()

# 2. Scatter Plot: Battery Capacity vs Energy Consumed
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Battery Capacity (kWh)', y='Energy Consumed (kWh)', hue='Vehicle Model', data=data, palette="deep")
plt.title('Battery Capacity vs Energy Consumed', fontsize=14)
plt.xlabel('Battery Capacity (kWh)')
plt.ylabel('Energy Consumed (kWh)')
plt.legend(loc='best')
plt.show()

# 3. Heatmap: Correlation between numerical features
plt.figure(figsize=(12, 8))
corr = data[['Battery Capacity (kWh)', 'Charging Duration (hours)', 'Energy Consumed (kWh)', 
             'Charging Rate (kW)', 'Charging Cost (USD)', 'State of Charge (Start %)', 
             'State of Charge (End %)', 'Distance Driven (since last charge) (km)', 
             'Temperature (°C)', 'Vehicle Age (years)']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap of Numerical Features', fontsize=14)
plt.show()

# 4. Distribution Plot: Charging Cost and Charging Duration
plt.figure(figsize=(14, 6))

# Distribution of Charging Cost
plt.subplot(1, 2, 1)
sns.histplot(data['Charging Cost (USD)'], kde=True, color='blue')
plt.title('Distribution of Charging Cost (USD)', fontsize=14)
plt.xlabel('Charging Cost (USD)')

# Distribution of Charging Duration
plt.subplot(1, 2, 2)
sns.histplot(data['Charging Duration (hours)'], kde=True, color='green')
plt.title('Distribution of Charging Duration (hours)', fontsize=14)
plt.xlabel('Charging Duration (hours)')

plt.tight_layout()
plt.show()
