def progressiveSubstituition(L, b):
  n = len(L)

  x = []
  for i in range(n):
    x_i = b[i]

    for j in range(i):
      x_i -= L[i][j] * x[j]

    x_i /= L[i][i]
    x.append(x_i)
  
  return x

def regressiveSubstitution(U, b):
  n = len(U)

  x = [0]*n
  for i in range(n-1,-1,-1):
    x_i = b[i]

    for j in range(i, n):
      x_i -= U[i][j] * x[j]

    x_i /= U[i][i]
    x[i] = x_i

  return x

