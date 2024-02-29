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

# Model price vs. no. of conv. stores, sqrt dist. to MRT station & house age, no global intercept, no interactions
mdl_price_vs_all_no_inter = ols("price_twd_msq ~ n_convenience + sqrt_dist_to_mrt_m + house_age_years + 0", data=taiwan_real_estate).fit()

# See the result
print(mdl_price_vs_all_no_inter.params)

# Model price vs. sqrt dist. to MRT station, no. of conv. stores & house age, no global intercept, 3-way interactions
mdl_price_vs_all_3_way_inter = ols("price_twd_msq ~ n_convenience + sqrt_dist_to_mrt_m + house_age_years + n_convenience:sqrt_dist_to_mrt_m + n_convenience:house_age_years + sqrt_dist_to_mrt_m:house_age_years + n_convenience:sqrt_dist_to_mrt_m:house_age_years + 0", data=taiwan_real_estate).fit()

# See the result
print(mdl_price_vs_all_3_way_inter.params)

# Model price vs. sqrt dist. to MRT station, no. of conv. stores & house age, no global intercept, 2-way interactions
mdl_price_vs_all_2_way_inter = ols("price_twd_msq ~ (n_convenience + sqrt_dist_to_mrt_m + house_age_years) ** 2 + 0", data=taiwan_real_estate).fit()

# See the result
print(mdl_price_vs_all_2_way_inter.params)

