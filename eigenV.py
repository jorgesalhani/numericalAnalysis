import numpy as np
import itertools as itt

class EigenV:
  def decomposition_QR_classic(A):
    m,n = [len(A), len(A[0])]

    Q = np.zeros((m,n))
    R = np.zeros((n,n))

    for j in range(n):
      V = A[:,j]
      
      for i in range(j):
        R[i,j] = np.dot(Q[:,i].transpose(), A[:,j])
        V = V - R[i,j] * Q[:, i]

      R[j,j] = np.linalg.norm(V)
      Q[:,j] = V / R[j,j]

    return {'Q': Q, 'R': R}

  def decomposition_QR_modified(A):
    m,n = [len(A), len(A[0])]

    V = np.copy(A)
    Q = np.zeros((m,n))
    R = np.zeros((n,n))

    for j in range(n):
      R[j,j] = np.linalg.norm(V[:,j])
      Q[:,j] = V[:,j] / R[j,j]
      
      for i in range(j):
        R[i,j] = np.dot(Q[:,i].transpose(), A[:,j])
        V[:,j] -= R[i,j] * Q[:, i]

    return {'Q': Q, 'R': R}

  def francis():
    pass