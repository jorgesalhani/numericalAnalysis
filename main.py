import numpy as np

from directMethods import DirectMethods
from iterativeMethods import IterativeMethods

A = np.array([
  [3, -2, 1, 0, 0, 0],
  [-2, 4, -2 ,1 ,0, 0],
  [1, -2, 4, -2 ,1, 0],
  [0, 1 ,-2, 4, -2, 1],
  [0, 0 ,1 ,-2, 4, -2],
  [0, 0 ,0 ,1 ,-2, 3],
], dtype=float)

b = np.array([10, -8, 10, 10, -8, 10])
# LU = DirectMethods.decomposition_lu(A)
# print(np.matmul(LU['L'], LU['U']))

r = IterativeMethods().solve_gauss_jacobi(A,b)
print(r)