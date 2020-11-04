import numpy as np

from sympy import*

# 2.1
x = Symbol('x')
y = sqrt(x + sqrt(x + sqrt(x)))
print('函数的导数为：',diff(y, x))


# 2.2
x = Symbol('x')
y = ((x-2)/(x-3))**0.5
print('函数的导数为：',diff(y, x))


# 2.3
x = Symbol('x')
y = (x/(1+x))**x
print('函数的导数为：',diff(y, x))


# 2.4
x = Symbol('x')
y = asin((1-x**2)**0.5)
print('函数的导数为：',diff(y, x))