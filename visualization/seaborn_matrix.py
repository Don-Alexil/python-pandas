import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

import os
file_path = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(file_path + '/datasets/daily_show_guests_cleaned.csv')

# Create the crosstab DataFrame
pd_crosstab = pd.crosstab(df["Group"], df["YEAR"])

# Plot a heatmap of the table with no color bar and using the BuGn palette
sns.heatmap(pd_crosstab, cbar=False, cmap="BuGn", linewidths=0.3)

# Rotate tick marks for visibility
plt.yticks(rotation=0)
plt.xticks(rotation=90)

#Show the plot
plt.show()
plt.clf()