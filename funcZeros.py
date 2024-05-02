import numpy as np

class FuncZeros:
  def __init__(self, max_it = 5000, epsilon = 0.001, forceReturnResult = False) -> None:
    self.MAX_ITERATION = max_it
    self.epsilon = epsilon
    self.forceReturnResult = forceReturnResult

  def bissection(self, func, a, b):
    """ Obter solução x tal que f(x) = 0 via algoritmo de bisseção dentro do intervalo [a,b]

    func : function
      função f(x)
    a : float
      limite inferior do intervalo a ser verificado
    b: float
      limite superior do intervalo a ser verificado
    """
    x = (a+b)/2
    erro = np.inf

    k = 0
    while erro > self.epsilon:
      if func(a) * func(x) < 0: b = x 
      else: a = x

      x0 = x
      x = (a+b)/2
      erro = abs(x-x0)
      k += 1
      if k >= self.MAX_ITERATION and self.forceReturnResult: 
        return x

    return x
  
  def newton(self, func, dfunc, x0):
    """ Obter solução x tal que f(x) = 0 via algoritmo de Newton

    func : function
      função f(x)
    dfunc : function
      derivada de f(x) -- df/dx
    x0: float
      valor inicial
    """
    k = 0
    x = x0
    while k < self.MAX_ITERATION:
      dx = func(x) / dfunc(x)
      x -= dx
      if abs(dx) < self.epsilon:
        return x
    
    if (self.forceReturnResult): return x

    return None
  
  def newton_jacobian(self, funcs, jacobian, x0):
    """ Obter solução x tal que f(x) = 0 via algoritmo de Newton para sistemas

    funcs : ndarray[function]
      vetor 1D com funções do sistema 
    jacobian : ndarray[[function]]
      matriz 2D com Jacobiana (parciais de f(x))
    x0: ndarray
      vetor 1D com valores iniciais
    """
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
      
    if (self.forceReturnResult): return x
    
    return None
