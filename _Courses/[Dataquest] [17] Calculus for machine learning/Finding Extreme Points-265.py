## 3. Differentiation ##

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,6,110)
y = -2*x + 3
plt.plot(x,y)
plt.show()

## 6. Power Rule ##

x = 2
slope_one = 5*x**4

slope_two = 0

## 7. Linearity Of Differentiation ##

x = 1
slope_three = 5*x**4 - 1

x = 2
slope_four = 3*x**2 - 2*x

## 8. Practicing Finding Extreme Values ##

import sympy 
rel_min = []
rel_max = []
x = sympy.symbols('x')
# limit for x -> -0.001
limit_zero_left = sympy.limit(3*x**2 - 2*x,x,-0.001)
# limit for x -> +0.001
limit_zero_right = sympy.limit(3*x**2 - 2*x,x,0.001)
if limit_zero_left > 0 and limit_zero_right < 0:
    rel_max.append(int(0))
elif limit_zero_left < 0 and limit_zero_right > 0:
    rel_min.append(int(0))
    
limit_two_third_left = sympy.limit(3*x**2 - 2*x,x,2/3 - 0.001)
limit_two_third_right = sympy.limit(3*x**2 - 2*x,x,2/3 + 0.001)
if limit_two_third_left < 0 and limit_two_third_right > 0:
    rel_min.append(2/3)
elif limit_two_third_left > 0 and limit_two_third_right < 0:
    rel_max.append(2/3)