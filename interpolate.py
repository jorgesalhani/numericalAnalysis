import numpy as np

class Interpolate:
  @staticmethod
  def lagrange(x, x_i, y_i):
    n = len(y_i)
    L = []

    for k in range(n):
      l_ki = lambda x, k, i : (x - x_i[i]) / (x_i[k] - x_i[i])
      l_k = lambda x, k : np.prod([l_ki(x,k,i) for i in range(n) if i != k])

      L.append(y_i[k] * l_k (x,k))

    return np.sum(L)

  @staticmethod
  def newton(x, x_i, y_i):
    n = len(x_i)

    D = np.zeros((n, n))
    D[:, 0] = y_i

    for j in range(1,n):
      for i in range(n-j):
        divided_diff = lambda i,j : (D[i+1, j-1] - D[i,j-1]) / (x_i[i+j] - x_i[i])

        D[i,j] = divided_diff(i,j)

    p_ki = lambda x, ord_i : np.prod([(x - x_i[i]) for i in range(ord_i)])
    P_k = [D[0,i] * p_ki(x, i) for i in range(n)]

    return np.sum(P_k)
  
  @staticmethod
  def chebychev_nodes(a, b, n):

    theta = lambda i : ((2*i - 1) / (2*(n+1))) * np.pi
    cheb_xi = lambda i : ((a+b)/2) + ((b-a)/2) * np.cos(theta(i))

    return [cheb_xi(i) for i in range(1,n)]
  
  @staticmethod
  def linear_spline(x, x_i, y_i):
    n = len(x_i)

    m_i = lambda i : ((x_i[i+1] - x) / (x_i[i+1] - x_i[i]))
    m_inext = lambda i : ((x - x_i[i]) / (x_i[i+1] - x_i[i]))
    
    s_i = lambda i : y_i[i] * m_i(i) + y_i[i+1] * m_inext(i)

    first_max_i = [i for i in range(1,n) if x_i[i-1] <= x]
    if len(first_max_i) == 0: return 0

    return s_i(first_max_i[-1]-1)

