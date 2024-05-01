import numpy as np
from eigenV import EigenV

A = np.array([
  [1,1,2],
  [2,1,1],
  [1,3,1]
], dtype=float)

VQ = EigenV.ortogonal_GS(A)
print(VQ['V'])
print(VQ['Q'])
# QR = np.linalg.qr(A)
# print(QR[0])
# print(QR[1])