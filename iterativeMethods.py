import numpy as np

class IterativeMethods:
  def __init__(self, max_it = 5000, epsilon = 0.001) -> None:
    self.MAX_ITERATION = max_it
    self.epsilon = epsilon

  def solve_gauss_jacobi(self, A, b, x0):
    n = len(A)
    Dinv = np.diagflat([1/A[i,i] for i in range(n)])
    I = np.eye(n)
    
    C = I - np.matmul(Dinv, A)
    g = np.matmul(Dinv, b)

    norm = np.linalg.norm(b - np.matmul(A,x0))

    k = 0
    while norm > self.epsilon and k <= self.MAX_ITERATION:
      x0 = np.matmul(C,x0) + g
      k += 1
      norm = np.linalg.norm(b - np.matmul(A,x0))
    
    if k >= self.MAX_ITERATION:
      raise Exception('Cálculo não converge')
    
    return x0

  # TODO não convergindo
  def solve_gauss_seidel(self, A, b, x0):
    n = len(A)
    L = np.tril(A)
    U = np.triu(A,1)
    
    Linv = - np.linalg.inv(L)
    C = - np.matmul(Linv, U)
    g = np.matmul(Linv, b)

    norm = np.linalg.norm(b - np.matmul(A,x0))

    k = 0
    while norm > self.epsilon and k <= self.MAX_ITERATION:
      x0 = np.matmul(C,x0) + g
      k += 1
      norm = np.linalg.norm(b - np.matmul(A,x0))
    
    if k >= self.MAX_ITERATION:
      raise Exception('Cálculo não converge')
    
    return x0
  
  def solve_gradientes(self, A, b, x0):
    n = len(A)
    r = b - np.matmul(A, x0)
    norm = np.linalg.norm(r)

    k = 0
    while norm > self.epsilon and k <= self.MAX_ITERATION:
      rT = r.transpose()
      Ar = np.matmul(A, r)
      alpha = np.dot(rT, r) / np.dot(r, Ar)
      x0 += alpha * r
      r = b - np.matmul(A, x0)
      norm = np.linalg.norm(r)
      
    if k >= self.MAX_ITERATION:
      raise Exception('Cálculo não converge')
    
    return x0

