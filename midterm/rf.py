import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import sklearn
import time
from sklearn.ensemble import RandomForestRegressor
pd.set_option('display.max_columns', None)
ts = pd.read_csv('features.csv')
y = ts[['logerror']]
x = ts.drop('logerror', axis=1)
# Random Forest with MAPE
start = time.time()
rf = RandomForestRegressor(n_estimators=5, criterion='mae', max_depth=4, random_state=10)
rf.fit(x, y)
p_rf_mape = rf.predict(x)
print(p_rf_mape)
print(rf.score)
end = time.time()
print(end-start)

