import numpy as np
from eigenV import EigenV

# A = np.array([
#   [1,1,0],
#   [0,1,2],
#   [1,0,1],
#   [0,1,3]
# ], dtype=float)

# QR = EigenV.decomposition_QR_classic(A)
# print(np.matmul(QR['Q'], QR['R']))

# A = np.array([
#   [3,1],
#   [4,-1]
# ], dtype=float)

# QR = EigenV.decomposition_QR_modified(A)
# print(QR)
# print(np.matmul(QR['Q'], QR['R']))
# print()
# QR = np.linalg.qr(A)
# print(QR)

# QR = np.linalg.qr(A)
# print(np.matmul(QR[0], QR[1]))

A = np.array([
  [2,1],
  [1,2]
], dtype=float)

eigen = EigenV()
print(eigen.francis(A))