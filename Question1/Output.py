Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: D:\Python_Internship\Python_CodeXIntern\Python_CodeXIntern\Question1\Question_1.py
First 5 rows of the dataset:
  User ID Vehicle Model  ...     Charger Type               User Type
0  User_1        BMW i3  ...  DC Fast Charger                Commuter
1  User_2  Hyundai Kona  ...          Level 1           Casual Driver
2  User_3    Chevy Bolt  ...          Level 2                Commuter
3  User_4  Hyundai Kona  ...          Level 1  Long-Distance Traveler
4  User_5  Hyundai Kona  ...          Level 1  Long-Distance Traveler

[5 rows x 18 columns]

Columns in the dataset:
Index(['User ID', 'Vehicle Model', 'Battery Capacity (kWh)',
       'Charging Station ID', 'Charging Station Location',
       'Energy Consumed (kWh)', 'Charging Duration (hours)',
       'Charging Rate (kW)', 'Charging Cost (USD)', 'Time of Day',
       'Day of Week', 'State of Charge (Start %)', 'State of Charge (End %)',
       'Distance Driven (since last charge) (km)', 'Temperature (°C)',
       'Vehicle Age (years)', 'Charger Type', 'User Type'],
      dtype='object')

Basic statistics of the dataset:
       Battery Capacity (kWh)  ...  Vehicle Age (years)
count             1320.000000  ...          1320.000000
mean                74.534692  ...             3.612843
std                 20.626914  ...             2.309824
min                  1.532807  ...             0.000000
25%                 62.000000  ...             2.000000
50%                 75.000000  ...             4.000000
75%                 85.000000  ...             6.000000
max                193.003074  ...            11.688592

[8 rows x 10 columns]

The average of the column 'column_name' is: 42.64289425432217

The total sum of the column 'column_name' is: 53474.18939492

Total non-null entries in the column 'column_name': 1254

The maximum value in the column 'column_name' is: 152.238758
The minimum value in the column 'column_name' is: 0.045771842

Rows where the 'column_name' is greater than 50:
        User ID  Vehicle Model  ...     Charger Type               User Type
0        User_1         BMW i3  ...  DC Fast Charger                Commuter
3        User_4   Hyundai Kona  ...          Level 1  Long-Distance Traveler
7        User_8     Chevy Bolt  ...          Level 2  Long-Distance Traveler
9       User_10   Hyundai Kona  ...  DC Fast Charger                Commuter
20      User_21    Nissan Leaf  ...          Level 2           Casual Driver
...         ...            ...  ...              ...                     ...
1310  User_1311  Tesla Model 3  ...          Level 2           Casual Driver
1311  User_1312   Hyundai Kona  ...          Level 2                Commuter
1313  User_1314  Tesla Model 3  ...          Level 2  Long-Distance Traveler
1316  User_1317         BMW i3  ...          Level 2           Casual Driver
1319  User_1320    Nissan Leaf  ...  DC Fast Charger                Commuter

[499 rows x 18 columns]

Average of 'Energy Consumed (kWh)' grouped by 'Vehicle Model':
Vehicle Model
BMW i3           42.450042
Chevy Bolt       40.739926
Hyundai Kona     42.834434
Nissan Leaf      42.505048
Tesla Model 3    44.518325
Name: Energy Consumed (kWh), dtype: float64

Filtered data saved to 'filtered_data.csv'.
