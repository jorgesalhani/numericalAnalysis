import numpy as np

class Interpolate:
  @staticmethod
  def lagrange(x, y_i, x_i):
    n = len(y_i)
    L = []

    for k in range(n):
      l_ki = lambda x, k, i : (x - x_i[i]) / (x_i[k] - x_i[i])
      l_k = lambda x, k : np.prod([l_ki(x,k,i) for i in range(n) if i != k])

      L.append(y_i[k] * l_k (x,k))

    return np.sum(L)

  def newton():
    pass