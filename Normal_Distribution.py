import random
from matplotlib import pyplot as plt
import numpy as np
import collections
from scipy.interpolate import interp1d


cases = [1,2,3,4,5,6]

result = random.choices(cases, weights = [1,3,5,5,3,1], k = 1000)

result.sort()

frequency = collections.Counter(result)

print(frequency)

x_axis = np.array(frequency.keys())
y_axis = np.array(frequency.values())

print(x_axis)
print(y_axis)

plt.style.use('ggplot')

plt.tight_layout()

plt.plot(x_axis,y_axis,color = '#444444',linestyle = '--',label ='Random datas')

plt.xlabel('Numbers')
plt.ylabel('Frequency')
plt.title('Trends of Randomness')

plt.legend()

plt.show()