import numpy as np

class IterativeMethods:
  def __init__(self, max_it = 5000, epsilon = 0.001, printCG = False, forceReturnResult = False) -> None:
    self.MAX_ITERATION = max_it
    self.epsilon = epsilon
    self.printCG = printCG
    self.forceReturnResult = forceReturnResult

  @staticmethod
  def test_convergency_gauss_jacobi(A):
    if 0 in np.diag(A): return False

    n = len(A)
    alpha = []
    for k in range(n):
      alpha_k = (np.sum(abs(A[k,:k])) + np.sum(abs(A[k,k+1:]))) / abs(A[k,k])
      alpha.append(alpha_k)
    
    if max(alpha) < 1: return True

    alpha = []
    for k in range(n):
      alpha_k = (np.sum(abs(A[k,:k])) + np.sum(abs(A[k,k+1:]))) / abs(A[k,k])
      alpha.append(alpha_k)

    if max(alpha) < 1: return True
    return False
  
  @staticmethod
  def test_convergency_gauss_seidel(A):
    if 0 in np.diag(A): return False

    n = len(A)

    beta = [np.sum(abs(A[0,1:])) / abs(A[0,0])]
    for k in range(1, n):
      beta_k = (np.sum(abs(A[k,:k]) * beta[k-1]) + np.sum(abs(A[k,k+1:]))) / abs(A[k,k])
      beta.append(beta_k)
    print(beta)
    
    if max(beta) < 1: return True
    return False

  def solve_gauss_jacobi(self, A, b, x0):
    n = len(A)
    Dinv = np.diagflat([1/A[i,i] for i in range(n)])
    I = np.eye(n)
    
    C = I - np.matmul(Dinv, A)
    g = np.matmul(Dinv, b)

    if (self.printCG):
      print('C = ')
      print(C)
      print()

      print('g = ')
      print(g)
    
    norm = np.linalg.norm(b - np.matmul(A,x0))

    k = 0
    while norm > self.epsilon and k <= self.MAX_ITERATION:
      x0 = np.matmul(C,x0) + g
      k += 1
      norm = np.linalg.norm(np.matmul(A,x0) - b)
    
    if k >= self.MAX_ITERATION:
      if (self.forceReturnResult): return x0
      raise Exception('Cálculo não converge')
    
    return x0

  def solve_gauss_seidel(self, A, b, x0):
    n = len(A)
    L = np.tril(A)
    U = np.triu(A,1)
    
    Linv = np.linalg.inv(L)
    C = - np.matmul(Linv, U)
    g = np.matmul(Linv, b)

    if (self.printCG):
      print('C = ')
      print(C)
      print()

      print('g = ')
      print(g)

    norm = np.linalg.norm(np.matmul(A,x0) - b)

    k = 0
    while norm > self.epsilon and k <= self.MAX_ITERATION:
      x0 = np.matmul(C,x0) + g
      k += 1
      norm = np.linalg.norm(np.matmul(A,x0) - b)
    
    if k >= self.MAX_ITERATION:
      if (self.forceReturnResult): return x0
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
      if (self.forceReturnResult): return x0
      raise Exception('Cálculo não converge')
    
    return x0
