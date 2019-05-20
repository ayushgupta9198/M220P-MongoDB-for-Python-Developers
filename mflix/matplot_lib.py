from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
# x=[1,2,3,4,5]
# y=[10]
# pyplot.scatter(x,y)
# pyplot.plot(x,y)
# x1=[7]
# y1=[11]
# pyplot.xlabel('age')
# pyplot.ylabel('count')
# pyplot.plot(x1,y1,'red',label='user_count')

# pyplot.bar(x1,y1,align='center',color='red',label='cout_age')
# pyplot.pie(x, x1, y1, startangle=90)
# style.use('ggplot')
# pyplot.show()

# ===================

# slices = [7,2,2,13]
# activities = ['sleeping','eating','working','playing']
# cols = ['c','m','r','b']
#
# plt.pie(slices,
#         labels=activities,
#         colors=cols,
#         startangle=90,
#         shadow= True,
#         explode=(0,0.2,0.1,0.2),
#         autopct='%1.1f%%')
# plt.legend(activities)
# plt.title('Interesting Graph\nCheck it out')
# plt.show()
# plt.savefig('pie_b.png')

# ===============================

# names = ['group_a', 'group_b', 'group_c']
# values = [1, 10, 100]
#
# plt.figure(1, figsize=(9, 3))
#
# plt.subplot(131)
# plt.bar(names, values)
# plt.subplot(132)
# plt.scatter(names, values)
# plt.subplot(133)
# plt.plot(names, values)
# plt.suptitle('Categorical Plotting')
# plt.show()

# ==========================

# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
#
# plt.scatter('a', 'b', c='c', s='d', data=data)
# plt.xlabel('entry a')
# plt.ylabel('entry b')
# plt.show()

# ==============================
#
# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)
#
# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)
#
# plt.figure(1)
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
#
# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()

# ==================================

import matplotlib.mlab as mlab

mu, sigma = 100, 15
x = mu + sigma*np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='green', alpha=0.75)

# add a 'best fit' line
y = mlab.normpdf( bins, mu, sigma)
l = plt.plot(bins, y, 'b--', linewidth=1)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)

plt.show()