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

# Fit a linear regression of price_twd_msq vs. n_convenience plus house_age_years, no intercept
mdl_price_vs_both = ols("price_twd_msq ~ n_convenience + house_age_years + 0", data=taiwan_real_estate).fit()


# Create n_convenience as an array of numbers from 0 to 10
n_convenience = n_convenience = np.arange(0, 11, 1)

# Extract the unique values of house_age_years
house_age_years = taiwan_real_estate["house_age_years"].unique()

# Create p as all combinations of values of n_convenience and house_age_years
p = product(n_convenience, house_age_years)

# Transform p to a DataFrame and name the columns
explanatory_data = pd.DataFrame(p, columns = ['n_convenience', 'house_age_years'])

# Add predictions to the DataFrame
prediction_data = explanatory_data.assign(price_twd_msq = mdl_price_vs_both.predict(explanatory_data))

# Extract the model coefficients, coeffs
coeffs = mdl_price_vs_both.params

# Print coeffs
print(coeffs)

# Assign each of the coeffs
ic_0_15, ic_15_30, ic_30_45, slope = coeffs

# Define conditions
conditions = [
	explanatory_data['house_age_years'] == "0 to 15",
	explanatory_data['house_age_years'] == "15 to 30",
	explanatory_data['house_age_years'] == "30 to 45"		
]

# Define choices
choices = [ic_0_15, ic_15_30, ic_30_45]

# Create array of intercepts for each house_age_year category
intercept = np.select(conditions, choices)

# Create prediction_data with columns intercept and price_twd_msq
prediction_data = explanatory_data.assign(
			      intercept = intercept,
  			      price_twd_msq = intercept + slope * explanatory_data['n_convenience'])

print(prediction_data)