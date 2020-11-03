import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 

import os
file_path = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(file_path + '/datasets/female_literacy_fertility.csv')

fertility = df['fertility'].to_numpy() 
illiteracy = 100 - df['female literacy'].to_numpy()

# Plot the illiteracy rate versus fertility
_ = plt.plot(illiteracy, fertility, marker='.', linestyle='none')

# Set the margins and label axes
plt.margins(0.02)
_ = plt.xlabel('percent illiterate')
_ = plt.ylabel('fertility')

# Perform a linear regression using np.polyfit(): a, b
a, b = np.polyfit(illiteracy, fertility, 1)

# Print the results to the screen
print('slope =', a, 'children per woman / percent illiterate')
print('intercept =', b, 'children per woman')

# Make theoretical line to plot
x = np.array([0, 100])
y = a * x + b

# Add regression line to your plot
_ = plt.plot(x, y)

# Draw the plot
plt.show()

# Show the Pearson correlation coefficient
print(np.corrcoef(illiteracy, fertility))