from sympy import *

# 5.1
x = Symbol('x')
f = sin(x)/(1+sin(x)+cos(x))
init_printing()
print(integrate(f,x))

# 5.2
x = Symbol('x')
f = (1/x)*((1+x)/x)**0.5
print(integrate(f,x))

# 5.3
x = Symbol('x')
f = (x**(2/3)*x**0.5+x**0.2)/x**0.5
print(integrate(f,x))

# 5.4
x = Symbol('x')
f = exp(2*x)*sin(3*x)
print(integrate(f,x))


# 6.1
x = Symbol('x')
f = 1 - (sin(x))**3
print(integrate(f,(x,0,pi)))

# 6.2
x = Symbol('x')
f = (x+2)/(x**2+2*x+2)
print(integrate(f,(x,-2,0)))

# 6.3
x = Symbol('x')
f = sin(log(x))
print(integrate(f,(x,1,exp(1))))

# 6.4
x = Symbol('x')
f = exp(x**0.5)
print(integrate(f,(x,0,1)))
