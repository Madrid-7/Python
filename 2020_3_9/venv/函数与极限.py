from sympy import*
import math

# 1
x = Symbol('x')
f1 = ((x**3 - x**2 + x/2)*exp(x) - (x**6 + 1)**0.5)
print('第一题：',limit(f1, x, oo))

# 2
x = Symbol('x')
f2 = sin(x)**tan(x)
print('第二题：',limit(f2, x, pi/2, dir = '-'))

# 3
x = Symbol('x')
f3 = ((4*x+3)/(4*x+1))**(2*x+5)
print('第三题：',limit(f3, x, oo))

# 4
x = Symbol('x')
f4 = ((1-0.5*x**2)**(2/3)-1)/(x*log(1+x))
print('第四题：',limit(f4, x, 0))