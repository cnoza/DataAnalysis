## 1. Recap ##

import pandas as pd

train_df = pd.read_csv('dc_airbnb_train.csv')
test_df = pd.read_csv('dc_airbnb_test.csv')

## 2. Hyperparameter optimization ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

hyper_params = [1,2,3,4,5]
mse_values = []

X_train = train_df[['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']]
y_train = train_df['price']

X_test = test_df[['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']]
y_test = test_df['price']

for each in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=each, algorithm='brute')
    knn.fit(X_train, y_train)
    predictions = knn.predict(X_test)
    mse_values.append(mean_squared_error(y_test, predictions))
    
print(mse_values)

## 3. Expanding grid search ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

hyper_params = list(range(1,21))
mse_values = []

X_train = train_df[['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']]
y_train = train_df['price']

X_test = test_df[['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']]
y_test = test_df['price']

for each in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=each, algorithm='brute')
    knn.fit(X_train, y_train)
    predictions = knn.predict(X_test)
    mse_values.append(mean_squared_error(y_test, predictions))
    
print(mse_values)


## 4. Visualizing hyperparameter values ##

import matplotlib.pyplot as plt
%matplotlib inline

features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
hyper_params = [x for x in range(1, 21)]
mse_values = list()

for hp in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=hp, algorithm='brute')
    knn.fit(train_df[features], train_df['price'])
    predictions = knn.predict(test_df[features])
    mse = mean_squared_error(test_df['price'], predictions)
    mse_values.append(mse)
    
plt.scatter(x=hyper_params, y=mse_values)
plt.show()

## 5. Varying features and hyperparameters ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

hyper_params = list(range(1,21))
mse_values = []

X_train = train_df.drop('price', axis=1)
y_train = train_df['price']

X_test = test_df.drop('price', axis=1)
y_test = test_df['price']

for each in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=each, algorithm='brute')
    knn.fit(X_train, y_train)
    predictions = knn.predict(X_test)
    mse_values.append(mean_squared_error(y_test, predictions))
    
plt.scatter(x=hyper_params, y=mse_values)
plt.show()

## 6. Practice the workflow ##

def knn_model(mse_values,features):
    X_train = train_df[features]
    y_train = train_df['price']

    X_test = test_df[features]
    y_test = test_df['price']

    for each in hyper_params:
        knn = KNeighborsRegressor(n_neighbors=each, algorithm='brute')
        knn.fit(X_train, y_train)
        predictions = knn.predict(X_test)
        mse_values.append(mean_squared_error(y_test, predictions))

two_features = ['accommodates', 'bathrooms']
three_features = ['accommodates', 'bathrooms', 'bedrooms']
hyper_params = [x for x in range(1,21)]

two_mse_values = list()
knn_model(two_mse_values, two_features)
two_hyp_mse = dict()
two_hyp_mse[two_mse_values.index(min(two_mse_values))+1] = min(two_mse_values)

three_mse_values = list()
knn_model(three_mse_values, three_features)
three_hyp_mse = dict()
three_hyp_mse[three_mse_values.index(min(three_mse_values))+1] = min(three_mse_values)

print(two_hyp_mse)
print(three_hyp_mse)