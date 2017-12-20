## 3. Exploring the Data ##

import pandas as pd

avengers = pd.read_csv("avengers.csv")
avengers.head(5)

## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = avengers[avengers['Year']>= 1960]

avengers['Year'].hist()


## 5. Consolidating Deaths ##

def count_deaths(row):
    #print(row)
    counter = 0
    for each in ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']:
        if ~pd.isnull(row[each]) and row[each] == 'YES':
           counter += 1
    return counter
   
true_avengers['Deaths'] = true_avengers.apply(count_deaths, axis=1)
true_avengers['Deaths'].head()
    
    

## 6. Verifying Years Since Joining ##

joined_accuracy_count  = 0

def count(row):
    if row['Years since joining'] == 2015 - row['Year']:
        global joined_accuracy_count
        joined_accuracy_count += 1
        
true_avengers.apply(count, axis=1)