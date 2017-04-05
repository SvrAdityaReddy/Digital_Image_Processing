import numpy as np
from numpy import linalg as LA

''' 

Given matrix is [[0, 0, 1], [0, 1, 1], [1, 1, 0]]

'''

cov = np.array([[(2/9), (1/9), (-2/9)], [(1/9), (2/9), (-1/9)], [(-2/9), (-1/9), (2/9)]])
# cov = np.cov(np.array([[0, 0, 1], [0, 1, 1], [1, 1, 0]]))

w, v = LA.eig(cov)

temp = np.copy(v)

'''

For the given example lamda3 > lambda2 > lambda1

'''

v[:,0] = temp[:,2]
v[:,1] = temp[:,1]
v[:,2] = temp[:,0]

result = np.dot(cov, v)
result = np.dot(v.transpose(), result)

print w
# print v
print result