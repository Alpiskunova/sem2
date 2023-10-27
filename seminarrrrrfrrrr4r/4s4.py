#4s4
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("iris_data.csv")
SepalLength = list(df['SepalLengthCm'])
SepalWidth = list(df['SepalWidthCm'])

PetalLength = list(df['PetalLengthCm'])
PetalWidth = list(df['PetalWidthCm'])

SL = np.array(SepalLength)
SW = np.array(SepalWidth)

PL = np.array(PetalLength)
PW = np.array(PetalWidth)

fig, ax = plt.subplots(3, 2)
fig.tight_layout(h_pad= 2)

ax[0, 0].set_title('Combinations of lengths (OX) and widths of sepals (OY)')
ax[0, 1].set_title('Combinations of sepal lengths (OX) and petal lengths (OY)')
ax[1, 0].set_title('Combinations of lengths (OX) and widths of petals (OY)')
ax[1, 1].set_title('Combinations of sepal widths (OX) and petal lengths (OY)')
ax[2, 0].set_title('Combinations of sepal widths (OX) and petal widths (OY)')
ax[2, 1].set_title('Combinations of lengths (OX) and widths of petals (OY)')

ax[0, 0].plot(SL, SW, 'o', label='Data', markersize=2)
ax[0, 1].plot(SL, PL, 'o', label='Data', markersize=2)
ax[1, 0].plot(SL, PW, 'o', label='Data', markersize=2)
ax[1, 1].plot(SW, PL, 'o', label='Data', markersize=2)
ax[2, 0].plot(SW, PW, 'o', label='Data', markersize=2)
ax[2, 1].plot(PL, PW, 'o', label='Data', markersize=2)

A1 = np.vstack([SL, np.ones(len(SL))]).T
m1, c1 = np.linalg.lstsq(A1, SW, rcond=None)[0]

A2 = np.vstack([SL, np.ones(len(SL))]).T
m2, c2 = np.linalg.lstsq(A2, PL, rcond=None)[0]

A3 = np.vstack([SL, np.ones(len(SL))]).T
m3, c3 = np.linalg.lstsq(A3, PW, rcond=None)[0]

A4 = np.vstack([SW, np.ones(len(SW))]).T
m4, c4 = np.linalg.lstsq(A4, PL, rcond=None)[0]

A5 = np.vstack([SW, np.ones(len(SW))]).T
m5, c5 = np.linalg.lstsq(A5, PW, rcond=None)[0]

A6 = np.vstack([PL, np.ones(len(PL))]).T
m6, c6 = np.linalg.lstsq(A6, PW, rcond=None)[0]

ax[0, 0].plot(SL, m1 * SL + c1, 'r' ,linewidth=1, label='approximate')
ax[0, 1].plot(SL, m2 * SL + c2, 'r' ,linewidth=1, label='approximate')
ax[1, 0].plot(SL, m3 * SL + c3, 'r' ,linewidth=1, label='approximate')
ax[1, 1].plot(SW, m4 * SW + c4, 'r' ,linewidth=1, label='approximate')
ax[2, 0].plot(SW, m5 * SW + c5, 'r' ,linewidth=1, label='approximate')
ax[2, 1].plot(PL, m6 * PL + c6, 'r' ,linewidth=1, label='approximate')

ax[0, 0].grid()
ax[0, 1].grid()
ax[1, 0].grid()
ax[1, 1].grid()
ax[2, 0].grid()
ax[2, 1].grid()

fig.suptitle('Podgonian')
plt.subplots_adjust(top= 0.86 )

plt.show()