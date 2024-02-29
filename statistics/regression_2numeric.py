import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.formula.api import ols
import numpy as np
from itertools import product

import os
file_path = os.path.dirname(os.path.abspath(__file__))

taiwan_real_estate = pd.read_csv(file_path + '/regression/taiwan_real_estate2.csv')
taiwan_real_estate['house_age_years'] = taiwan_real_estate['house_age_years'].astype('category')

# Transform dist_to_mrt_m to sqrt_dist_to_mrt_m
taiwan_real_estate["sqrt_dist_to_mrt_m"] = np.sqrt(taiwan_real_estate["dist_to_mrt_m"])

# Draw a scatter plot of sqrt_dist_to_mrt_m vs. n_convenience colored by price_twd_msq
sns.scatterplot(x="n_convenience",
           y="sqrt_dist_to_mrt_m",
           data=taiwan_real_estate,
           hue="price_twd_msq",
           ci=None)

# Fit linear regression of price vs. no. of conv. stores and sqrt dist. to nearest MRT, no interaction
mdl_price_vs_conv_dist = ols("price_twd_msq ~ n_convenience + sqrt_dist_to_mrt_m", data=taiwan_real_estate).fit()

# Create n_convenience as an array of numbers from 0 to 10
n_convenience = np.arange(0, 11, 1)

# Create sqrt_dist_to_mrt_m as an array of numbers from 0 to 80 in steps of 10
sqrt_dist_to_mrt_m = np.arange(0, 81, 10)

# Create p as all combinations of values of n_convenience and sqrt_dist_to_mrt_m
p = product(n_convenience, sqrt_dist_to_mrt_m)

# Transform p to a DataFrame and name the columns
explanatory_data = pd.DataFrame(p, columns = ['n_convenience', 'sqrt_dist_to_mrt_m'])

# Add column of predictions
prediction_data = explanatory_data.assign(price_twd_msq = mdl_price_vs_conv_dist.predict(explanatory_data))

# See the result  
print(prediction_data)

# Create scatter plot of taiwan_real_estate
sns.scatterplot(x="n_convenience",
           y="sqrt_dist_to_mrt_m",
           data=taiwan_real_estate,
           hue="price_twd_msq",
           ci=None)

# Create scatter plot of prediction_data without legend
sns.scatterplot(x="n_convenience",
           y="sqrt_dist_to_mrt_m",
           data=prediction_data,
           hue="price_twd_msq",
           marker="s",
           ci=None,
     legend=False)

# Show the plot
plt.show()