import pandas as pd 
import matplotlib.pyplot as plt
import os

file_path = os.path.dirname(os.path.abspath(__file__))

attrition_pop = pd.read_feather(file_path + '/sampling/attrition.feather')

mean_attrition_pop = attrition_pop['Attrition'].mean()

print(attrition_pop.dtypes)

# Create an empty list
mean_attritions = []
# Loop 500 times to create 500 sample means
for i in range(500):
	mean_attritions.append(
    	attrition_pop.sample(n=60)['Attrition'].mean()
	)

# Create a histogram of the 500 sample means
plt.hist(mean_attritions, bins=16)
plt.show()