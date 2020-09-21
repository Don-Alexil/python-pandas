import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

import os
file_path = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(file_path + '/datasets/bike_share.csv')

# Build a JointGrid comparing humidity and total_rentals
sns.set_style("whitegrid")
g = sns.JointGrid(x="hum",
            y="total_rentals",
            data=df,
            xlim=(0.1, 1.0)) 

g.plot(sns.regplot, sns.distplot)

# Create a jointplot similar to the JointGrid 
sns.jointplot(x="hum",
        y="total_rentals",
        kind='reg',
        data=df)
      
plt.show()
plt.clf()