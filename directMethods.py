import numpy as np
import itertools as itt

class DirectMethods:

  def progressive_substituition(L, b):
    n = len(L)

    x = []
    for i in range(n):
      x_i = b[i]

      for j in range(i):
        x_i -= L[i][j] * x[j]

      x_i /= L[i][i]
      x.append(x_i)
    
    return np.array(x)

  def regressive_substitution(U, b):
    n = len(U)

    x = [0]*n
    for i in range(n-1,-1,-1):
      x_i = b[i]

      for j in range(i, n):
        x_i -= U[i][j] * x[j]

      x_i /= U[i][i]
      x[i] = x_i

    return np.array(x)

  # TODO: com erro
  def decomposition_lu(A):
    n = len(A)

    L = np.identity(n)
    U = np.zeros((n,n))

    for i in range(n):
      for j in range(n):

        if i <= j:
          sumTerm = np.sum(L[i,:i] * U[:i,j])
          U[i,j] = A[i][j] - sumTerm

        if i > j:
          sumTerm = np.sum(L[i,:j] * U[:j,j])
          L[i,j] = (A[i,j] - sumTerm) / U[j,j]

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
      p = [k for k in range(j, n) if pivot == A[k,j]]
      if not p: continue
      p = p[0]
      temp = np.array(A[p,:])
      A[p,:] = A[j,:]
      A[j,:] = temp

      temp = b[j]
      b[j] = b[p]
      b[p] = temp

      # print(A[j,j])
      for i in range(j+1,n):
        m_ij = - A[i,j] / A[j,j]
        A[i,j:] = A[i,j:] + m_ij * A[j,j:]

        b[i] = b[i] + m_ij * b[j]

    return {'A': A, 'b': b}