import numpy as np
import itertools as itt

from directMethods import DirectMethods
from iterativeMethods import IterativeMethods

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

""" Questão 2

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

