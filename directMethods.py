import numpy as np

def progressive_substituition(L, b):
  n = len(L)

  x = []
  for i in range(n):
    x_i = b[i]

    for j in range(i):
      x_i -= L[i][j] * x[j]

    x_i /= L[i][i]
    x.append(x_i)
  
  return x

def regressive_substitution(U, b):
  n = len(U)

  x = [0]*n
  for i in range(n-1,-1,-1):
    x_i = b[i]

    for j in range(i, n):
      x_i -= U[i][j] * x[j]

    x_i /= U[i][i]
    x[i] = x_i

  return x

# TODO: com erro
def decomposition_lu(A):
  n = len(A)

  L = np.identity(n)
  U = np.zeros((n,n))

  for k in range(1, n):
    for j in range(k, n):
      U[k,j] = A[k,j] - np.sum(L[k,1:k-1] * U[1:k-1,j])

    for i in range(k, n):
      L[i,k] = (A[i,k] - np.sum(L[i,1:k-1] * U[1:k-1,k])) * (1 / U[k,k])

  return {'L': L, 'U': U}

def decomposition_cholesky(A):
  n = len(A)
  H = np.zeros((n,n))

  for j in range(n):
    h_ij = 0
    for i in range(j,n):

      if i == j:
        h_ij = np.sqrt(A[i,j] - sum(H[i,:i]**2))
      else:
        h_ij = (A[i,j] - sum(H[i,:i]*H[j,:i])) / H[j,j]

      H[i,j] = h_ij

  return H

def gauss_elimination(A, b):
  n = len(A)

  for j in range(n):
    # Com pivot
    pivot = max(abs(A[j:,j]))
    # indice da linha que contem 'pivot' em seu triangulo inf
    p = [i for i in range(n) if pivot in abs(A[i,:i])]
    if not p: continue
    temp = np.array(A[p,:])
    A[p,:] = A[j,:]
    A[j,:] = temp

    temp = b[j]
    b[j] = b[p]
    b[p] = temp

    for i in range(j+1,n):
      m_ij = - A[i,j] / A[j,j]
      A[i,j:] = A[i,j:] + m_ij * A[j,j:]

      b[i] = b[i] + m_ij * b[j]

  return {'A': A, 'b': b}

A = np.array([
  [0,1,2],
  [1,-1,3],
  [-2,3,1]
], dtype=float)

# print(A)
# b = np.array([8,8,7], dtype=float)

# print(gauss_elimination(A, b))
# print(regressive_substitution(A, b))

A = np.array([[100,200,300], [0,20,10], [0,0,20]])
b = np.array([20,40,60])
print(regressive_substitution(A,b))

