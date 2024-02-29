import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

file_path = os.path.dirname(os.path.abspath(__file__))
late_shipments = pd.read_feather(file_path + '/late_shipments.feather')

# Print the late_shipments dataset
print(late_shipments)

# Calculate the mean pack_price for each shipment_mode
xbar_pack_by_mode = late_shipments.groupby("shipment_mode")['pack_price'].mean()

# Calculate the standard deviation of the pack_price for each shipment_mode
s_pack_by_mode = late_shipments.groupby("shipment_mode")['pack_price'].std()

# Boxplot of shipment_mode vs. pack_price
sns.boxplot(x='pack_price', y ='shipment_mode', data=late_shipments)
plt.show()