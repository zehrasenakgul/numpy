# -*- coding: utf-8 -*-

import numpy as np

#a = np.arange(1,10)

a = np.array([1,3,5,7,9,11])
a = a.reshape(2,3)
print(a)
print(a.dtype)
print(a.ndim)

b = np.array([[1,3],[5,7],[9,11]])
print(b)
print(b.ndim)


