import numpy as np
import itertools as itt

class EigenV:
  def __init__(self, max_it = 10000, tol = 0.001) -> None:
    self.tol = tol
    self.max_it = max_it

  @staticmethod
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

  """
  @TODO corrigir
  """
  @staticmethod
  def decomposition_QR_modified(A):
    m,n = [len(A), len(A[0])]

    V = np.copy(A)
    Q = np.zeros((m,n))
    R = np.zeros((n,n))

    for j in range(n):
      R[j,j] = np.linalg.norm(V[:,j])
      Q[:,j] = V[:,j] / R[j,j]
      
      for i in range(j, n):
        R[i,j] = np.dot(Q[:,i].transpose(), V[:,j])
        V[:,j] -= R[i,j] * Q[:, i]

    return {'Q': Q, 'R': R}

  def francis(self, A):
    n = len(A)
    V = np.eye(n)
    erro = np.infty

    k = 0
    while erro > self.tol and self.max_it >= k :
      QR = self.decomposition_QR_modified(A)
      print(QR)
      A = np.matmul(QR['R'], QR['Q'])
      V = np.matmul(V, QR['Q'])

      erro = np.sqrt(abs(np.linalg.norm(A, ord='fro')**2 - np.sum(np.diag(A)**2)))
      k += 1

    return {'V': V, 'D': np.diag(A)}
