import pandas as pd
import os
file_path = os.path.dirname(os.path.abspath(__file__))

YAHOO_PATH = file_path + '/yahoo.csv'

yahoo = pd.read_csv(YAHOO_PATH)
yahoo['date'] = pd.to_datetime(yahoo['date'])
yahoo.set_index('date', inplace=True)

