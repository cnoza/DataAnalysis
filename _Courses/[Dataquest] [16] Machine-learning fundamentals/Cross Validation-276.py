## 1. Introduction ##

import numpy as np
import pandas as pd

dc_listings = pd.read_csv("dc_airbnb.csv")
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

dc_listings = dc_listings.reindex(np.random.permutation(dc_listings.index))
split_one = dc_listings.iloc[:1862]
split_two = dc_listings.iloc[1862:]

## 2. Holdout Validation ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

train_one = split_one
test_one = split_two
train_two = split_two
test_two = split_one

knn = KNeighborsRegressor()
knn.fit(train_one[['accommodates']],train_one['price'])
predict1 = knn.predict(test_one[['accommodates']])
iteration_one_rmse = (mean_squared_error(test_one['price'],predict1)) ** .5

knn = KNeighborsRegressor()
knn.fit(train_two[['accommodates']],train_two['price'])
predict2 = knn.predict(test_two[['accommodates']])
iteration_two_rmse = (mean_squared_error(test_two['price'],predict2)) ** .5

avg_rmse = (iteration_one_rmse + iteration_two_rmse)/2

print(avg_rmse)

## 3. K-Fold Cross Validation ##

dc_listings['fold'] = dc_listings['price']
dc_listings['fold'].iloc[:744] = 1
dc_listings['fold'].iloc[744:1488] = 2
dc_listings['fold'].iloc[1488:2232] = 3
dc_listings['fold'].iloc[2232:2976] = 4
dc_listings['fold'].iloc[2976:] = 5

print(dc_listings['fold'].value_counts())

## 4. First iteration ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

X_train = dc_listings[dc_listings['fold'] > 1][['accommodates']]
y_train = dc_listings[dc_listings['fold'] > 1]['price']

X_test = dc_listings[dc_listings['fold'] == 1][['accommodates']]
y_test = dc_listings[dc_listings['fold'] == 1]['price']

knn = KNeighborsRegressor()
knn.fit(X_train, y_train)
labels = knn.predict(X_test)
iteration_one_rmse = (mean_squared_error(y_test, labels)) ** .5



## 5. Function for training models ##

# Use np.mean to calculate the mean.
import numpy as np
fold_ids = [1,2,3,4,5]

def train_and_validate(df,folds):
    list_rmses = []
    for fold in folds:
        X_train = df[df['fold'] != fold][['accommodates']]
        y_train = df[df['fold'] != fold]['price']
        X_test = df[df['fold'] == fold][['accommodates']]
        y_test = df[df['fold'] == fold]['price']
        knn = KNeighborsRegressor()
        knn.fit(X_train, y_train)
        labels = knn.predict(X_test)
        list_rmses.append((mean_squared_error(y_test, labels)) ** .5)
    return list_rmses

rmses = train_and_validate(dc_listings,fold_ids)
avg_rmse = np.mean(rmses)

print(rmses)
print(avg_rmse)

## 6. Performing K-Fold Cross Validation Using Scikit-Learn ##

from sklearn.model_selection import cross_val_score, KFold

kf = KFold(5, shuffle=True, random_state=1)
knn = KNeighborsRegressor()
mses = cross_val_score(knn, dc_listings[['accommodates']], dc_listings['price'], scoring='neg_mean_squared_error', cv=kf)

avg_rmse = np.mean(abs(mses) ** .5) 

## 7. Exploring Different K Values ##

from sklearn.model_selection import cross_val_score, KFold

num_folds = [3, 5, 7, 9, 10, 11, 13, 15, 17, 19, 21, 23]

for fold in num_folds:
    kf = KFold(fold, shuffle=True, random_state=1)
    model = KNeighborsRegressor()
    mses = cross_val_score(model, dc_listings[["accommodates"]], dc_listings["price"], scoring="neg_mean_squared_error", cv=kf)
    rmses = np.sqrt(np.absolute(mses))
    avg_rmse = np.mean(rmses)
    std_rmse = np.std(rmses)
    
    print(str(fold), "folds: ", "avg RMSE: ", str(avg_rmse), "std RMSE: ", str(std_rmse))