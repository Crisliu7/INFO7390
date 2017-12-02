import math
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_validate

train = pd.read_csv("~/train.tsv",sep='\t',index_col=0)
y = trian[['price']]
X = train.drop('price',axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7)

# Linear regression
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

# Random forest
rf = RandomForestRegressor(n_estimators=100, criterion='mse', max_depth=10, random_state=10)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)

# Neural network
# nn = 
# nn.fit(X_train, y_train)
# nn_pred = nn.predict(X_test)