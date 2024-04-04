import numpy as np

class IterativeMethods:
  def __init__(self, max_it = 5000, epsilon = 0.01, x0 = 0) -> None:
    self.MAX_ITERATION = 5000
    self.x0 = x0
    self.epsilon = epsilon

  def solve_gauss_jacobi(self, A, b):
    n = len(A)
    D = np.diagflat(np.diag(A))
    I = np.eye(n)
    
    C = I - D/A
    g = D/b

    norm = np.linalg.norm(b - A*self.x0)

    k = 0
    x0 = self.x0
    while norm > self.epsilon and k <= self.MAX_ITERATION:
      x0 = C*x0 + g
      k += 1
    
    if k >= self.MAX_ITERATION:
      raise Exception('Cálculo não converge')
    
    return x0


