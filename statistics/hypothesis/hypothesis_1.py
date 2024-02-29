import pandas as pd 
import numpy as np
import os

file_path = os.path.dirname(os.path.abspath(__file__))
late_shipments = pd.read_feather(file_path + '/late_shipments.feather')

# Print the late_shipments dataset
print(late_shipments)

# Calculate the proportion of late shipments
late_prop_samp = (late_shipments['late'] == 'Yes').mean()

# Print the results
print(late_prop_samp)

late_shipments_boot_distn = []

for _ in range(5000): 
    late_shipments_boot_distn.append(
        (late_shipments.sample(frac=1, replace=True)['late']  == 'Yes').mean()
    )

# Hypothesize that the proportion is 6%
late_prop_hyp = 0.06

# Calculate the standard error
std_error = np.std(late_shipments_boot_distn, ddof=1)

# Find z-score of late_prop_samp
z_score = (late_prop_samp - late_prop_hyp) / std_error

# Print z_score
print(z_score)    