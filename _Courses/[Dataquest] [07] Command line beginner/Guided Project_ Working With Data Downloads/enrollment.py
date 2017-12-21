import pandas as pd
data = pd.read_csv('data/CRDC2013_14.csv', encoding='Latin-1')
data['total_enrollment'] = data['TOT_ENR_M'] + data['TOT_ENR_F']

import re
total_enr = {}
for each in list(data.columns):
    if re.match('^SCH_ENR', each):
        total_enr[each] = data[each].sum()
        
all_enrollment = data['total_enrollment'].sum()

for k,v in total_enr.items():
    total_enr[k] = v/all_enrollment
    print(k, ' perc: ', total_enr[k]) 