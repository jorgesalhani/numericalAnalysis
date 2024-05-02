import numpy as np
import itertools as itt
"""
Classe DirectMethods

Solução de sistemas lineares via métodos diretos
"""
class DirectMethods:

  def progressive_substituition(L, b):
    """ Obter o vetor x tal que torne verdadeira a equação Lx = b

    L : ndarray
      matriz triangular inferior 2D com tipos float
    b : ndarray
      vetor de resultado 1D com tipos float
    """
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
    """ Obter o vetor x tal que torne verdadeira a equação Ux = b

    U : ndarray
      matriz triangular superior 2D com tipos float
    b : ndarray
      vetor de resultado 1D com tipos float
    """
    n = len(U)

    x = [0]*n
    for i in range(n-1,-1,-1):
      x_i = b[i]

      for j in range(i, n):
        x_i -= U[i][j] * x[j]

      x_i /= U[i][i]
      x[i] = x_i

    return np.array(x)

  def decomposition_lu(A):
    """ Obter o vetor decomposição LU da matriz A tal que A = LU

    A : ndarray
      2D array com tipos float
    """
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
    """ Obter o vetor decomposição H da matriz A tal que A = H(H^T) via Cholesky

    A : ndarray
      2D array com tipos float
    """
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
    """ Obter a matriz triangular superior de A via eliminação de Gauss

    A : ndarray
      2D array com tipos float
    b : ndarray
      vetor de resultado 1D com tipos float
    """
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
  
  def inverse(A):
    """ Obter a matriz inversa de A (A^(-1))

    A : ndarray
      2D array com tipos float
    """
    n = len(A)
    I = np.eye(n)

    v = []

    LU = DirectMethods.decomposition_lu(A)

    for e in I:
      y = DirectMethods.progressive_substituition(LU['L'], e)
      x = DirectMethods.regressive_substitution(LU['U'], y)

      v.append(x)

    return np.array(v).transpose()