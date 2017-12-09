## 2. Introduction to the Data ##

import pandas as pd
all_ages = pd.read_csv('all-ages.csv')
recent_grads = pd.read_csv('recent-grads.csv')
all_ages.head(5)
recent_grads.head(5)

## 3. Summarizing Major Categories ##

# Unique values in Major_category column.
print(all_ages['Major_category'].unique())

aa_cat_counts = dict()
rg_cat_counts = dict()

for major in all_ages['Major_category'].unique():
    aa_cat_counts[major] = all_ages[all_ages['Major_category'] == major]['Total'].sum()
    
for major in recent_grads['Major_category'].unique():
    rg_cat_counts[major] = recent_grads[recent_grads['Major_category'] == major]['Total'].sum()

## 4. Low-Wage Job Rates ##

low_wage_percent = 0.0

low_wage_proportion = recent_grads['Low_wage_jobs'].sum() / recent_grads['Total'].sum()

## 5. Comparing Data Sets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0

for major in majors:
    rg_ur = recent_grads[recent_grads['Major'] == major]['Unemployment_rate'].sum()
    aa_ur = all_ages[all_ages['Major'] == major]['Unemployment_rate'].sum()
    if rg_ur < aa_ur:
        rg_lower_count += 1
        
print(rg_lower_count)