import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

import os
file_path = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(file_path + '/datasets/insurance_premiums.csv')

# Create the same PairGrid but map a histogram on the diag
g = sns.PairGrid(df, vars=["fatal_collisions", "premiums"])
g2 = g.map_diag(plt.hist)
g3 = g2.map_offdiag(plt.scatter)


# Plot the same data but use a different color palette and color code by Region
sns.pairplot(data=df,
        vars=["fatal_collisions", "premiums"],
        kind='scatter',
        diag_kind='hist',
        hue='Region',
        palette='RdBu',
        diag_kws={'alpha':.5})

# Build a pairplot with different x and y variables
sns.pairplot(data=df,
        x_vars=["fatal_collisions_speeding", "fatal_collisions_alc"],
        y_vars=['premiums', 'insurance_losses'],
        kind='scatter',
        hue='Region',
        palette='husl')

# plot relationships between insurance_losses and premiums
sns.pairplot(data=df,
             vars=["insurance_losses", "premiums"],
             kind='reg',
             palette='BrBG',
             diag_kind = 'kde',
             hue='Region')
      
plt.show()
plt.clf()