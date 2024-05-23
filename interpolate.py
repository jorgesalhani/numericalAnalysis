import numpy as np

class Interpolate:
  def __init__(self, x_i, y_i) -> None:
    self.x_i = np.array(x_i)
    self.y_i = np.array(y_i)
    self.n = len(self.x_i)

  def lagrange(self, x):
    L = []

    for k in range(self.n):
      l_ki = lambda x, k, i : (x - self.x_i[i]) / (self.x_i[k] - self.x_i[i])
      l_k = lambda x, k : np.prod([l_ki(x,k,i) for i in range(self.n) if i != k])

      L.append(self.y_i[k] * l_k (x,k))

    return np.sum(L)

  def newton(self, x):

    D = np.zeros((self.n, self.n))
    D[:, 0] = self.y_i

    for j in range(1,self.n):
      for i in range(self.n-j):
        divided_diff = lambda i,j : (D[i+1, j-1] - D[i,j-1]) / (self.x_i[i+j] - self.x_i[i])

        D[i,j] = divided_diff(i,j)

    p_ki = lambda x, ord_i : np.prod([(x - self.x_i[i]) for i in range(ord_i)])
    P_k = [D[0,i] * p_ki(x, i) for i in range(self.n)]

    return np.sum(P_k)
  
  @staticmethod
  def chebychev_nodes(a, b, n):

    theta = lambda i : ((2*i - 1) / (2*(n+1))) * np.pi
    cheb_xi = lambda i : ((a+b)/2) + ((b-a)/2) * np.cos(theta(i))

    return [cheb_xi(i) for i in range(1,n)]
  
  def linear_spline(self, x):
    m_i = lambda i : ((self.x_i[i+1] - x) / (self.x_i[i+1] - self.x_i[i]))
    m_inext = lambda i : ((x - self.x_i[i]) / (self.x_i[i+1] - self.x_i[i]))
    
    s_i = lambda i : self.y_i[i] * m_i(i) + self.y_i[i+1] * m_inext(i)

    first_max_i = [i for i in range(1,self.n) if self.x_i[i-1] <= x]
    if len(first_max_i) == 0: return 0

    return s_i(first_max_i[-1]-1)
  
  def cubic_spline(self, x):

    h = self.x_i[2:] - self.x_i[1:self.n-1]
    u = 2 * [h[1:self.n-1] + h[2:self.n]]
    print(h)
    print(u)
    
    # a_i = lambda i : (z[i+1] - z[i]) / 6 h[i]
    # b_i = lambda i : z[i] / 2
    # c_i = lambda i : ((self.y_i[i+1] - self.y_i[i]) / h[i]) - (h[i] * z[i+1]) / 6 - (h[i] * z[i]) / 3
    # d_i = lambda i : self.y_i[i]

    first_max_i = [i for i in range(1,self.n) if self.x_i[i-1] <= x]
    if len(first_max_i) == 0: return 0

    # s_i(first_max_i[-1]-1)

