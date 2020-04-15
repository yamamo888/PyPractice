# -*- coding: utf-8 -*-


import numpy as np
import seaborn as sns
from scipy.stats import poisson
import matplotlib.pyplot as plt

sns.set_style("dark")
# probability distribution
x = np.arange(0,10)
# poisson distribution
y = poisson.pmf(x,3)

fig = plt.figure()

plt.plot(x,y,color='black')

plt.xlabel('k')
plt.ylabel('P(X=k)')

plt.savefig('poisson_lamda3.png')