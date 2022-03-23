#Validation using matrix diagonalization
import numpy as np

a = [[8, 3, -3], [-2, -8, 5], [3,5,10]]
diag = np.diag(np.abs(a))
diagCheck = np.sum(np.abs(a), axis = 1) - diag

if np.all(diag > diagCheck):
  print('Matrix is diagonally dominant')
else:
  print('Matrix is NOT diagonally dominant')