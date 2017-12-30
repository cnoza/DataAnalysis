## 3. Statistical significance ##

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
print(mean_group_a)

mean_group_b = np.mean(weight_lost_b)
print(mean_group_b)

plt.hist(weight_lost_a)
plt.show()

plt.hist(weight_lost_b)
plt.show()

## 4. Test statistic ##

mean_difference = mean_group_b - mean_group_a
print(mean_difference)

## 5. Permutation test ##

import numpy as np

mean_difference = 2.52
print(all_values)

mean_differences = []
for i in range(1000):
    group_a = []
    group_b = []
    for value in all_values:
        if np.random.rand() >= 0.5:
            group_a.append(value)
        else:
            group_b.append(value)
    iteration_mean_difference = np.mean(group_b) - np.mean(group_a)
    mean_differences.append(iteration_mean_difference)
    
plt.hist(mean_differences)
plt.show()

## 7. Dictionary representation of a distribution ##

sampling_distribution = {}
for each in mean_differences:
    if each in sampling_distribution:
        sampling_distribution[each] += 1
    else:
        sampling_distribution[each] = 1
        

## 8. P value ##

frequencies = []
for k,v in sampling_distribution.items():
    if k >= 2.52:
        frequencies.append(v)
p_value = sum(frequencies)/1000

# Another way
mean_diff = np.array(mean_differences)
p_value1 = sum(mean_diff >= 2.52)/1000

