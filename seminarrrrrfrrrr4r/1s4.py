import numpy as np
import matplotlib.pyplot as plt
U = [350,
400,
450,
500,
550,
600,
725,
700,
675,
650,
625,
575,
]
I = [68,
77,
87,
97,
106,
116,
139,
136,
130,
126,
121,
111,
]
I=sorted(I)
U=sorted(U)
fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(111)
x = [68, 140]
y = np.interp(x, I, U)

plt.title('График зависимости напряжения от силы тока', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.xlabel('I, A')
plt.ylabel('U, B')

ax1.scatter(I, U, marker='x')
ax1.errorbar(I, U, yerr=0.002, xerr = 0.004, color = 'hotpink', linestyle = 'None')
ax1.plot(x, y, 'r')
ax1.grid()
slope, intercept = np.polyfit(np.log(I), np.log(U), 1)
print(slope)


plt.show()
