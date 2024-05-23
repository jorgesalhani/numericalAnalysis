import numpy as np
from interpolate import Interpolate
import matplotlib.pyplot as plt

x_i = [-2, 0, 3, 5]
y_i = [3, -2, 4, 10]

xs = np.arange(-2.6,5.6,0.1)

interpolate = Interpolate(x_i, y_i)

# fig, ax = plt.subplots(1,1, figsize=(6,10))

# fig.suptitle('Interpolação', fontsize=20)

# ax.scatter(x_i, y_i, marker='*')

# L = [interpolate.lagrange(x) for x in xs]
# ax.plot(xs, L, '-', label='Lagrange')

# L = [interpolate.newton(x) for x in xs]
# ax.plot(xs, L, '-', label='Newton')

# L = [interpolate.linear_spline(x) for x in xs]
# ax.plot(xs, L, '-', label='Spline linear')

# ax.set_xlabel('X', {'size': 15})
# ax.set_ylabel('Y', {'size': 15})
# ax.legend(title='Método', title_fontsize=13)

# plt.show()

## Runge phenomena
# ================

fRungPhen = lambda x : 1 / (1 + (25 * (x**2)))
x_i = np.arange(-.8,.9,0.1)
y_i = [fRungPhen(x) for x in x_i]

interpolate = Interpolate(x_i, y_i)

x_runge = np.arange(-1,.7,0.01)
f_runge = [fRungPhen(x) for x in x_runge]

xs = np.arange(-1,1,0.01)

L_lagrange = [interpolate.lagrange(x) for x in xs]

x_cheb = Interpolate.chebychev_nodes(-1,1,15)
y_cheb = [fRungPhen(x) for x in x_cheb]

interpolate = Interpolate(x_cheb, y_cheb)
L_cheb = [interpolate.lagrange(x) for x in xs]

fig, ax = plt.subplots(1,1, figsize=(13,10))

fig.suptitle('Interpolação', fontsize=20)

ax.plot(x_runge, f_runge, '-', label='f(x) = 1 / 1+25x^2')
ax.scatter(x_i, y_i, marker='*', label=f'Equal spaced: n = {len(x_i)}')
ax.scatter(x_cheb, y_cheb, marker='*', label=f'Chebychev nodes: n = {len(x_cheb)}')
ax.plot(xs, L_lagrange, '-r', label='Lagrange')
ax.plot(xs, L_cheb, '-k', label='Lagrange + Chebychev nodes')

ax.set_xlabel('X', {'size': 15})
ax.set_ylabel('Y', {'size': 15})
ax.legend(title='Método', title_fontsize=13)

ax.set_ylim(-0.7, 2)

plt.show()
# x_i = np.array([1,2,4])
# y_i = np.array([1,3,5])

# print(Interpolate.linear_spline(1.8, x_i, y_i))

# interpolate.cubic_spline(xs)