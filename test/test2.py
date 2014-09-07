
from numpy import *
import numpy as np
import redis
a1 = [1,2,2,2,3,4,]
a2 = [3,5,6,7,8,8,]
a3 = [3,4,7,8,9,9,]
a4 = [2,3,5,7,8,9,]

complete = np.concatenate((a1,a2,a3,a4))
uvals, uind = np.unique(complete, return_inverse=True)
print uvals[np.bincount(uind).argsort()[-4:]][::-1].tolist()

#
# a = np.array((0.05, 0.06, 0.07))/12
# b = np.fv(a, 10*12, -100, -100)
# print b

d = array([a1,a2,a3,a4])

# c = arange(15).reshape(3,5)
# print c.shape
# print c.ndim
# print c.dtype.name
# print c.itemsize
# print c.size
# print d.shape
# print d

# e = array(d,dtype=complex)
# print e
# print zeros((3,4))
# print ones((2,3,4),dtype=int16)
# print empty((2,3))
print d
print d<6