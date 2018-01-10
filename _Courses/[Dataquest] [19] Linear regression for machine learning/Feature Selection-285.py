## 1. Missing Values ##

import pandas as pd
data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]
numerical_train = train.select_dtypes(include=['int', 'float'])
numerical_train = numerical_train.drop(['PID','Year Built', 'Year Remod/Add', 'Garage Yr Blt', 'Mo Sold', 'Yr Sold'],axis=1)

null_series = numerical_train.isnull().sum()
full_cols_series = null_series[null_series == 0]
print(full_cols_series)

## 2. Correlating Feature Columns With Target Column ##

train_subset = train[full_cols_series.index]
sorted_corrs = train_subset.corr()['SalePrice'].abs().sort_values()

## 3. Correlation Matrix Heatmap ##

import seaborn as sns
import matplotlib.pyplot as plt

strong_corrs = sorted_corrs[sorted_corrs > 0.3]
sns.heatmap(train[strong_corrs.index].corr())

## 4. Train And Test Model ##

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

final_corr_cols = strong_corrs.drop(['Garage Cars', 'TotRms AbvGrd'])
features = final_corr_cols.drop(['SalePrice']).index
target = 'SalePrice'

clean_test = test[final_corr_cols.index].dropna()

lr = LinearRegression()
lr.fit(train[features],train[target])
pred_train = lr.predict(train[features])
pred_test = lr.predict(clean_test[features])

train_rmse = (mean_squared_error(train[target],pred_train)) ** .5
test_rmse = (mean_squared_error(clean_test[target],pred_test)) ** .5

## 5. Removing Low Variance Features ##

train[features] = (train[features] - train[features].min())/(train[features].max() - train[features].min())
print(train[features].min())
print(train[features].max())
sorted_vars = train[features].var().sort_values()
print(sorted_vars)

## 6. Final Model ##

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

lr = LinearRegression()
lr.fit(train[sorted_vars.drop(['Open Porch SF']).index], train[target])
pred_train = lr.predict(train[sorted_vars.drop(['Open Porch SF']).index])
pred_test = lr.predict(clean_test[sorted_vars.drop(['Open Porch SF']).index])
train_rmse_2 = (mean_squared_error(train[target],pred_train)) ** .5
test_rmse_2 = (mean_squared_error(clean_test[target],pred_test)) ** .5

