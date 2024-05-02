import numpy as np
from eigenV import EigenV

A = np.array([
  [3,1],
  [4,-1]
], dtype=float)

QR = EigenV.decomposition_QR_classic(A)
print(QR['Q'])
print(QR['R'])
print()
QR = np.linalg.qr(A)
print(QR[0])
print(QR[1])