## 3. Condensing the Class Size Data Set ##

class_size = data['class_size']
class_size = class_size[(class_size['GRADE '] == '09-12') & (class_size['PROGRAM TYPE'] == 'GEN ED')]
class_size.head()
                                                             
                                                          

## 5. Computing Average Class Sizes ##

import numpy as np
class_size = class_size.groupby('DBN').agg(np.mean)
class_size.reset_index(inplace=True)
data['class_size'] = class_size
data['class_size'].head()

## 7. Condensing the Demographics Data Set ##

demographics = data['demographics']
demographics = demographics[demographics['schoolyear'] == 20112012]
data['demographics'] = demographics
data['demographics'].head()

## 9. Condensing the Graduation Data Set ##

graduation = data['graduation']
graduation = graduation[(graduation['Cohort'] == '2006') & (graduation['Demographic'] == 'Total Cohort')]
data['graduation'] = graduation
data['graduation'].head()

## 10. Converting AP Test Scores ##

cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']
for col in cols:
    data['ap_2010'][col] = pd.to_numeric(data['ap_2010'][col], errors='coerce')
    print(data['ap_2010'][col].dtypes)
    


## 12. Performing the Left Joins ##

combined = data["sat_results"]
combined = combined.merge(data['ap_2010'], on='DBN', how='left')
combined = combined.merge(data['graduation'], on='DBN', how='left')
print(combined.head())
print(combined.shape)

## 13. Performing the Inner Joins ##

for each in ['class_size','demographics', 'survey', 'hs_directory']:
    combined = combined.merge(data[each], on='DBN', how='inner')
    
print(combined.shape)
print(combined.head())

## 15. Filling in Missing Values ##

means = combined.mean()
combined = combined.fillna(means).fillna(0)
combined.head()

## 16. Adding a School District Column for Mapping ##

combined['school_dist'] = combined['DBN'].apply(lambda x: x[0:2])
combined.head()