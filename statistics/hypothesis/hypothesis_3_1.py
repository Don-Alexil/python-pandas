import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import pingouin


file_path = os.path.dirname(os.path.abspath(__file__))
late_shipments = pd.read_feather(file_path + '/late_shipments.feather')

# Print the late_shipments dataset
print(late_shipments)

# Run an ANOVA for pack_price across shipment_mode
anova_results = pingouin.anova(data=late_shipments,               
                               dv="pack_price",
                               between="shipment_mode")    

# Print anova_results
print(anova_results)