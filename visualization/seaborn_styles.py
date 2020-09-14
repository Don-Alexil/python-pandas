import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

import os
file_path = os.path.dirname(os.path.abspath(__file__))


df = pd.read_csv(file_path + '/datasets/FY18_4050_FMRs.csv')

for style in ['white','dark','whitegrid','darkgrid','ticks']:    
    sns.set_style(style)    
    sns.distplot(df['Tuition'])    
    plt.show()

sns.distplot(df['fmr_2'])
plt.show()

print(df.head())