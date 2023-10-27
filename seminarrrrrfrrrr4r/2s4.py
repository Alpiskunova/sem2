import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

plt.title('kakoy title?', fontdict={'fontname': 'sans-serif', 'fontsize': 18})
values1 = np.random.normal(0, 10, 10000)
values2 = np.random.normal(0, 10, 1000000)
values3 = np.random.normal(0, 10, 100000000)
ax1.hist(values1, 1000, )
ax1.set_title('graph numero uno')
ax1.grid()

ax2.hist(values2, 1000)
ax2.set_title('graph numero dos')

ax2.grid()
ax3.hist(values3, 1000)
ax3.set_title('graph numero tres')

ax3.grid()
plt.show()