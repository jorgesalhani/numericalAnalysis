import numpy as np
import itertools as itt
import time

from directMethods import DirectMethods
from iterativeMethods import IterativeMethods
from funcZeros import FuncZeros

# Lista 1 - Sistemas Lineares

# Métodos diretos - Teorico (para comparação)

""" Questão 1
A = np.array([
  [4,-8,1],
  [6,5,7],
  [0,-10,-3]
], dtype=float)

b = np.array([8, -4, 12])
G = DirectMethods.gauss_elimination(A, b)
LU = DirectMethods.decomposition_lu(G['A'])
print(LU['L'])
print(LU['U'])
print(np.matmul(LU['L'], LU['U']))
"""

""" Solução
a)
4.0
17.0
0.23529411764705888

b)
6.0
-11.333333333333332
0.23529411764705843
"""

""" Questão 3

A = np.array([
  [1, -1, 0],
  [-1, 2, -1],
  [0, -1, 1]
])

LU = DirectMethods.decomposition_lu(A)
print(LU['L'])
print(LU['U'])
print(np.matmul(LU['L'], LU['U']))

"""

""" Solução

L = 
[[ 1.  0.  0.]
 [-1.  1.  0.]
 [ 0. -1.  1.]]

U =
[[ 1. -1.  0.]
 [ 0.  1. -1.]
 [ 0.  0.  0.]]

"""

""" Questão 5

A = np.array([
  [-1, 2, -2, 1],
  [-2, 2, -3, 0],
  [-2, 0, -1, -3],
  [-2, 0, 0, -2]
])

LU = DirectMethods.decomposition_lu(A)
print(LU['L'])
print(LU['U'])
print(np.matmul(LU['L'], LU['U']))
"""

""" Solução

L = 
[[1. 0. 0. 0.]
 [2. 1. 0. 0.]
 [2. 2. 1. 0.]
 [2. 2. 2. 1.]]

U = 
[[-1.  2. -2.  1.]
 [ 0. -2.  1. -2.]
 [ 0.  0.  1. -1.]
 [ 0.  0.  0.  2.]]
"""

# Métodos iterativos - Teorico (para comparação)

""" Questão 3

A = np.array([
  [-8, 1, 1],
  [1, -5, 1],
  [1, 1, -4]
])

b = np.array([1,16,7])
x0 = np.zeros(len(b))

itm = IterativeMethods()
x = itm.solve_gauss_jacobi(A, b, x0)

x = itm.solve_gauss_seidel(A, b, x0)

"""

""" Solução 

BGJ =
[[0.    0.125 0.125]
 [0.2   0.    0.2  ]
 [0.25  0.25  0.   ]]

cGJ =
[-0.125 -3.2   -1.75 ]

BGS =
[[-0.     -0.125  -0.125 ]
 [-0.     -0.025  -0.225 ]
 [-0.     -0.0375 -0.0875]]

xGS =
[0.125  3.225  2.5875]

"""


# Métodos diretos - Prática

""" Questão 1

A = np.array([
  [2, -3, -1],
  [3, 2, -5],
  [2, 4, -1]
])

LU = DirectMethods.decomposition_lu(A)

detL = list(itt.accumulate(np.diag(LU['L']), func=np.multiply, initial=1))[-1]
detU = list(itt.accumulate(np.diag(LU['U']), func=np.multiply, initial=1))[-1]
detA = detL * detU

print(detA, np.linalg.det(A))

B = np.array([
  [2, 0, -1, 0],
  [0, 1, 2, 0],
  [-1, 2, 0, 1],
  [0, 0, 1, -2]
])

LU = DirectMethods.decomposition_lu(B)

detL = list(itt.accumulate(np.diag(LU['L']), func=np.multiply, initial=1))[-1]
detU = list(itt.accumulate(np.diag(LU['U']), func=np.multiply, initial=1))[-1]
detB = detL * detU

print(detB, np.linalg.det(B))


"""

""" Solução

49.0 -- 49.000000000000014
16.0 -- 15.999999999999991

"""


""" Questão 2 - a)

A = np.array([
  [2, -3, -1],
  [3, 2, -5],
  [2, 4, -1]
])

b = np.array([3, -9, -5])

# Ax = b -> LUx = b
# Ux = y
# Ly = b 

LU = DirectMethods.decomposition_lu(A)

y = DirectMethods.progressive_substituition(LU['L'], b)
x = DirectMethods.regressive_substitution(LU['U'], y)

print(x)
print(np.matmul(A, x.transpose()))

"""

""" Solução - a)

x = 
[ 
  0.65306122 
  -1.14285714  
  1.73469388
]

"""

""" Questão 2 - b)

B = np.array([
  [2, 0, -1, 0],
  [0, 1, 2, 0],
  [-1, 2, 0, 1],
  [0, 0, 1, -2]
])

Z = np.array([
 [1, 0, 0, 0],
 [0, 0, 1, 0] 
])

X = []
for z in Z:
  LU = DirectMethods.decomposition_lu(B)

  y = DirectMethods.progressive_substituition(LU['L'], z)
  x = DirectMethods.regressive_substitution(LU['U'], y)

  X.append(x)

X = np.array(X)
print(X.transpose())
print(np.matmul(B, X.transpose()))

"""

""" Solução - b) 

X =
[[ 0.4375 -0.125 ]
 [ 0.25    0.5   ]
 [-0.125  -0.25  ]
 [-0.0625 -0.125 ]]

"""

""" Questão 3 - a) TODO

A = np.array([
  [0,0,2,1,2],
  [0,1,0,2,-1],
  [1,2,0,-2,0],
  [0,0,0,-1,1],
  [0,1,-1,1,-1],
])

b = np.array([1,1,-4,-2,-1])

Ab = DirectMethods.gauss_elimination(A, b)
x = DirectMethods.regressive_substitution(Ab['A'], Ab['b'])
print(Ab['A'], Ab['b'])
# print(np.matmul(A, x.transpose()))

"""

""" Solução - a) TODO

"""

# Métodos iterativos - Prática

""" Questão 2 

A = np.array([
  [3,-2,1,0,0,0],
  [-2,4,-2,1,0,0],
  [1,-2,4,-2,1,0],
  [0,1,-2,4,-2,1],
  [0,0,1,-2,4,-2],
  [0,0,0,1,-2,3]
])

b = np.array([10,-8,10,10,-8,10])

x0 = np.array([0,0,0,0,0,0])

itm = IterativeMethods()
st = time.time()
x = itm.solve_gauss_jacobi(A, b, x0)
print(x)
print(f'GJ: {time.time() - st}')

st = time.time()
LU = DirectMethods.decomposition_lu(A)
y = DirectMethods.progressive_substituition(LU['L'], b)
x = DirectMethods.regressive_substitution(LU['U'], y)
print(x)
print(f'LU: {time.time() - st}')

"""

""" Solução

x = 
[1.99992302e+00 6.96739190e-05 3.99996233e+00 3.99996233e+00
 6.96739190e-05 1.99992302e+00]

GJ: 0.008947134017944336

x = 
 [2.00000000e+00 0.00000000e+00 4.00000000e+00 4.00000000e+00
 1.53980681e-16 2.00000000e+00]

LU: 0.0011858940124511719

"""


# Método dos gradientes

""" Questão 1

A = np.array([
  [10, 1, 0],
  [1, 10, 1],
  [0, 1, 10]
], dtype=float)

b = np.array([11,11,1], dtype=float)
x0 = np.array([0,0,0], dtype=float)

itm = IterativeMethods(epsilon=0.1)
x = itm.solve_gradientes(A, b, x0)
print(x)

"""

""" Solução

x = 
[1.00077186e+00 9.91759863e-01 8.59247324e-04]

"""


""" Questão 2 - b)

A = np.array([
  [1, 0.4, 0.4],
  [0.4, 1, 0.4],
  [0.4, 0.4, 0.4]
])

b = np.array([1,2,3], dtype=float)

x0 = np.array([0,0,0], dtype=float)
itm = IterativeMethods(epsilon=0.001)
x = itm.solve_gradientes(A, b, x0)
print(x)

print(np.matmul(A,x))

"""

""" Solução - b)

x = 
[-3.33187992 -1.66521325 12.49604646]

"""



# fz = FuncZeros()
# # func = lambda x : x**3 - 30*(x**2) + 2552
# # print(fz.bissection(func, -10, 0))

# func = lambda x : x**2 + x - 6
# dfunc = lambda x : 2*x + 1
# x0 = 5.5
# fz.epsilon = 1e-7
# print(fz.newton(func, dfunc, x0))