import numpy as np

class FuncZeros:
  def __init__(self, max_it = 5000, epsilon = 0.001) -> None:
    self.MAX_ITERATION = max_it
    self.epsilon = epsilon

  def bissection(self, func, a, b):
    x = (a+b)/2
    erro = np.inf

    while erro > self.epsilon:
      if func(a) * func(x) < 0: b = x 
      else: a = x

      x0 = x
      x = (a+b)/2
      erro = abs(x-x0)

    return x
  
  def newton(self, func, dfunc, x):
    k = 0
    while k < self.MAX_ITERATION:
      dx = func(x) / dfunc(x)
      x -= dx
      if abs(dx) < self.epsilon:
        return x
      
    return None
  
  def newton_jacobian(self, funcs, jacobian, x0):
    k = 0
    x = x0
    while k < self.MAX_ITERATION:
      calc_jac = jacobian(*list(x0))
      calc_funcs = funcs(*list(x0))

      jacInv = np.linalg.inv(calc_jac)
      v = np.matmul(jacInv, calc_funcs)
      x -= v
      k += 1
      if np.linalg.norm(v) < self.epsilon:
        return x
    return None



