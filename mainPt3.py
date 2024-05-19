import numpy as np
from interpolate import Interpolate
import matplotlib.pyplot as plt

x_i = [-2, 0, 3, 5]
y_i = [3, -2, 4, 2]

dx = 1 
n = 10
xs = np.arange(-2.6,5.6,0.1)


L = [Interpolate.lagrange(x, y_i, x_i) for x in xs]

fig, ax = plt.subplots(1,1, figsize=(6,10))

fig.suptitle('Interpolação', fontsize=20)

ax.scatter(x_i, y_i, marker='*')
ax.plot(xs, L, '-', label='Lagrange')

ax.set_xlabel('X', {'size': 15})
ax.set_ylabel('Y', {'size': 15})
ax.legend(title='Método', title_fontsize=13)

plt.show()

