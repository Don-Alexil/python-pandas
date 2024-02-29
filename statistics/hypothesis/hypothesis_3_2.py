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

# Perform a pairwise t-test on pack price, grouped by shipment mode
pairwise_results = anova_results = pingouin.pairwise_tests(data=late_shipments,               
                               dv="pack_price",
                               between="shipment_mode", 
                               padjust="none")    
 
# Print pairwise_results
print(pairwise_results)

# Modify the pairwise t-tests to use Bonferroni p-value adjustment
pairwise_results = pingouin.pairwise_tests(data=late_shipments, 
                                           dv="pack_price",
                                           between="shipment_mode",
                                           padjust="bonf")

# Print pairwise_results
print(pairwise_results)