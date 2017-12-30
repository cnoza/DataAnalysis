## 2. Calculating expected values ##

males_over50k = .241 * .669 * 32561
males_under50k = .759 * .669 * 32561
females_over50k = .241 * .331 * 32561
females_under50k = .759 * .331 * 32561

## 3. Calculating chi-squared ##

def chisq(obs, exp):
    return (obs - exp) ** 2 / exp

# (0,0) = Male > 50k, (0,1) = Female > 50k, ...
exp_table = [5249.8, 2597.4, 16533.5, 8180.3]
obs_table = [6662, 1179, 15128, 9592]

chisq_gender_income = sum([chisq(obs_table[i],exp_table[i]) for i in range(4)])

## 4. Finding statistical significance ##

import numpy as np
from scipy.stats import chisquare

observed = np.array([6662, 1179, 15128, 9592])
expected = np.array([5249.8, 2597.4, 16533.5, 8180.3])
chisquare_value, pvalue_gender_income = chisquare(observed, expected)

## 5. Cross tables ##

import pandas

table = pandas.crosstab(income["sex"], [income["race"]])
print(table)

## 6. Finding expected values ##

import numpy as np
from scipy.stats import chi2_contingency
import pandas as pd

chisq_value, pvalue_gender_race, df, expected = chi2_contingency(pd.crosstab(income["sex"], [income["race"]]))