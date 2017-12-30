## 2. Calculating differences ##

female_diff = (10771 - 16280.5)/16280.5

male_diff = (21790 - 16280.5)/16280.5

## 3. Updating the formula ##

female_diff = ((10771 - 16280.5) ** 2)/16280.5

male_diff = ((21790 - 16280.5)** 2)/16280.5

gender_chisq = female_diff + male_diff

## 4. Generating a distribution ##

import numpy as np
chi_squared_values = []
for k in range(1000):
    vector = np.random.random((32561,))
    vector = [0 if each < .5 else 1 for each in vector]
    sum_1 = sum(vector)
    sum_0 = len(vector) - sum_1
    male_diff = ((sum_0 - 32561/2) ** 2)/(32561/2)
    female_diff = ((sum_1 - 32561/2) ** 2)/(32561/2)
    chi_squared_values.append(male_diff + female_diff)
    
plt.hist(chi_squared_values)
plt.show()
    

## 6. Smaller samples ##

female_diff = ((107.71 - 162.805) ** 2)/162.805
male_diff = ((217.9 - 162.805) ** 2)/162.805

gender_chisq = male_diff + female_diff

## 7. Sampling distribution equality ##

import numpy as np
chi_squared_values = []
for k in range(1000):
    vector = np.random.random((300,))
    vector = [0 if each < .5 else 1 for each in vector]
    sum_1 = sum(vector)
    sum_0 = len(vector) - sum_1
    male_diff = ((sum_0 - 150) ** 2)/150
    female_diff = ((sum_1 - 150) ** 2)/150
    chi_squared_values.append(male_diff + female_diff)
    
plt.hist(chi_squared_values)
plt.show()

## 9. Increasing degrees of freedom ##

import pandas as pd
income = pd.read_csv('income.csv')
race_obs = income['race'].value_counts()
race_exp = pd.Series([26146.5, 3939.9, 944.3, 260.5, 1269.8], index=race_obs.index)

race_chisq = 0
for each in race_obs.index:
    race_chisq += ((race_obs[each] - race_exp[each])**2)/race_exp[each]
    race_chisq = float(race_chisq)

## 10. Using SciPy ##

from scipy.stats import chisquare
import numpy as np
import pandas as pd
income = pd.read_csv('income.csv')
race_obs = income['race'].value_counts().values
race_exp = np.array([26146.5, 3939.9, 944.3, 260.5, 1269.8])
race_chisquare_value, race_pvalue = chisquare(race_obs, race_exp)
