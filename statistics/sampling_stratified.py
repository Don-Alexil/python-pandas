import pandas as pd 


import os
file_path = os.path.dirname(os.path.abspath(__file__))

attrition_pop = pd.read_feather(file_path + '/sampling/attrition.feather')

print(attrition_pop.dtypes)



# Get 30 employees from each Education group
attrition_eq = attrition_pop.groupby('Education')\
	.sample(n=30, random_state=2022)      

# Get the proportions from attrition_eq
education_counts_eq = attrition_eq['Education'].value_counts(normalize=True)

# Print the results
print(education_counts_eq)