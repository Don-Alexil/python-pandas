import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.formula.api import logit
import numpy as np
from itertools import product

import os
file_path = os.path.dirname(os.path.abspath(__file__))

churn = pd.read_csv(file_path + '/regression/churn.csv')
