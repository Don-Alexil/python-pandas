# Manipulating Time Series Data in Python
# Create a time series of air quality data

import air_quality_data.utils as aqd
import pandas as pd 
import matplotlib.pyplot as plt 

data = pd.read_csv(aqd.NYC_PATH)

# Inspect data
print(data.info())

# Convert the date column to datetime64
data.date = pd.to_datetime(data.date)

# Set date column as index
data.set_index('date', inplace=True)

# Inspect data 
print(data.info())

# Plot data
data.plot(subplots=True)
plt.show()
