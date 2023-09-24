# import numpy as np
# import matplotlib.pyplot as plt
 
# rng = np.arange(10)
# rnd = np.random.randint(0, 10, size=(3, rng.size))
# yrs = 1950 + rng
 
# fig, ax = plt.subplots(figsize=(5, 3))
# ax.stackplot(yrs, rng + rnd, labels=['Eastasia', 'Eurasia', 'Oceania'])
# ax.set_title('Combined debt growth over time')
# ax.legend(loc='upper left')
# ax.set_ylabel('Total debt')
# ax.set_xlim(xmin=yrs[0], xmax=yrs[-1])
# fig.tight_layout()
 
# plt.show()
# x = np.arange(0, 100, 0.01)
# x = np.sin(x)
# # y = np.sin(x)
# fig, ax = plt.subplots()
# ax.plot(x)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

def fnIter(fn,x,delta=0.000001):
    while True:
        yield x
        prev,x = x,fn(x)
        if abs(x-prev)<delta:break

r = 3.99
seed = 0.5

total = []

for i,Xn in enumerate(fnIter(lambda x:x*r*(1-x),seed)):
    total.append(Xn)
    if (i == 500):
        break

fig, ax = plt.subplots()
ax.plot(total)
plt.show()