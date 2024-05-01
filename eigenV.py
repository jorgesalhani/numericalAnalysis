import numpy as np
import itertools as itt

class EigenV:
  def ortogonal_GS(A):
    n = len(A)
    V = np.copy(A)
    Q = np.copy(A)
    for j in range(n):
      Q[:,j] = V[:,j] / np.linalg.norm(V[:,j])
    
      proj_qa = [(np.dot(Q[:,i], A[:,i]) / np.linalg.norm(V[:,j])) * Q[:,i]  for i in range(j)]
      sumTerm = np.sum(proj_qa)
      V[:,j] = A[:,j] - sumTerm
    
    return {'V': V, 'Q':Q}

  def decomposition_QR_classic():
    pass

  def decomposition_QR_modified():
    pass

  def francis():
    pass