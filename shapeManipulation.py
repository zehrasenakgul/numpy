# -*- coding: utf-8 -*-

import numpy as np

a = np.floor(10*np.random.random((3,6)))

print(a)
print(a.shape)
print(a.ravel())
a = a.ravel()
print(a)
print(a.shape)

a = a.reshape(2,9)
print(a)
print(a.T)
print(a.reshape(2,-1))

b = a.resize(6,3)
print(b)
