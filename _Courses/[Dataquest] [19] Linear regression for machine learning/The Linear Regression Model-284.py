## 2. Introduction To The Data ##

import pandas as pd
data = pd.read_csv('AmesHousing.txt', sep='\t')
train = data[:1460]
test = data[1460:]
data.info()
target = 'SalePrice'

## 3. Simple Linear Regression ##

import matplotlib.pyplot as plt
# For prettier plots.
import seaborn
data.plot(kind='scatter', x='Garage Area', y='SalePrice')
plt.show()

data.plot(kind='scatter', x='Gr Liv Area', y='SalePrice')
plt.show()

data.plot(kind='scatter', x='Overall Cond', y='SalePrice')
plt.show()

## 5. Using Scikit-Learn To Train And Predict ##

from sklearn import linear_model
reg = linear_model.LinearRegression()

X = train[['Gr Liv Area']]
y = train['SalePrice']

reg.fit(X,y)

print(reg.coef_)
print(reg.intercept_)

a1 = reg.coef_
a0 = reg.intercept_

## 6. Making Predictions ##

import numpy as np

lr = LinearRegression()
lr.fit(train[['Gr Liv Area']], train['SalePrice'])

y_predict_train = lr.predict(train[['Gr Liv Area']])
y_predict_test = lr.predict(test[['Gr Liv Area']])

from sklearn.metrics import mean_squared_error
mse_train = mean_squared_error(y_predict_train, train['SalePrice'])
mse_test = mean_squared_error(y_predict_test, test['SalePrice'])

train_rmse = np.sqrt(mse_train)
test_rmse = np.sqrt(mse_test)



## 7. Multiple Linear Regression ##

cols = ['Overall Cond', 'Gr Liv Area']

reg.fit(train[cols], train['SalePrice'])
y_predict_train = reg.predict(train[cols])
y_predict_test = reg.predict(test[cols])

train_rmse_2 = np.sqrt(mean_squared_error(y_predict_train, train['SalePrice']))
test_rmse_2 = np.sqrt(mean_squared_error(y_predict_test, test['SalePrice']))