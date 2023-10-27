import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('C:/Us)
a = list((df['Species']))
b = A.count('Iris-setosa')
c = A.count('Iris-versicolor')
d = A.count('Iris-virginica')
e = list((df['PetalLengthCm']))
f = []
g = []
h = []


for i in range(len(e)):
    if e[i] < 1.2:
        F.append(e[i])
    elif e[i] >= 1.2 and E[i] <= 1.5:
        g.append(e[i])
    else:
        h.append(e[i])


fig = plt.figure(figsize = (16,9))
plt1 = fig.add_subplot(211)
plt2 = fig.add_subplot(212)


plt1.pie([b, c, ], labels = ['Iris-setosa','Iris-versicolor', 'Iris-virginica'])
plt2.pie([len(f), len(g), len(h)], labels = ['<1,2', '1,2<=x=<1,5', '1,5<'])


plt.show()