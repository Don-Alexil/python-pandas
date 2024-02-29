import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
from itertools import product


import os
file_path = os.path.dirname(os.path.abspath(__file__))

taiwan_real_estate = pd.read_csv(file_path + '/regression/taiwan_real_estate2.csv')
taiwan_real_estate['house_age_years'] = taiwan_real_estate['house_age_years'].astype('category')

# Create n_convenience as an array of numbers from 0 to 10
n_convenience = np.arange(0, 11, 1)

# Extract the unique values of house_age_years
house_age_years = taiwan_real_estate["house_age_years"].unique()

# Create p as all combinations of values of n_convenience and house_age_years
p = product(n_convenience, house_age_years)

# Transform p to a DataFrame and name the columns
explanatory_data = pd.DataFrame(p, columns = ['n_convenience', 'house_age_years'])

mdl_price_vs_both_inter = ols("price_twd_msq ~ n_convenience + n_convenience:house_age_years + 0", data = taiwan_real_estate).fit()

print(mdl_price_vs_both_inter.params)

# Add column of predictions using "0 to 15" model and explanatory data 
prediction_data = explanatory_data.assign(price_twd_msq = mdl_price_vs_both_inter.predict(explanatory_data))

# Plot the trend lines of price_twd_msq vs. n_convenience for each house age category
sns.lmplot(x="n_convenience",
           y="price_twd_msq",
           data=taiwan_real_estate,
           hue="house_age_years",
           ci=None,
           legend_out=False)

# Add a scatter plot for prediction_data
sns.scatterplot(x="n_convenience",
           y="price_twd_msq",
           data=prediction_data,
           hue="house_age_years",
           ci=None,
     legend=False)

plt.show()