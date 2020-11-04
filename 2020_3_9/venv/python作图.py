import numpy as np
from scipy import stats as sts
import sympy as sp
import statsmodels as stats

from matplotlib import pyplot as plt

#  f(x) = x^0.5
plt.figure(1)

x = np.arange(-5,5,0.01)
y = np.sqrt(x)
plt.xlabel("x")
plt.ylabel("y")
plt.title(r"$f(x) = x^0.5$")

plt.plot(x,y)


#  f(x) = 2^x
plt.figure(2)
x = np.arange(-5,5,0.01)
y = 2**x
plt.xlabel("x")
plt.ylabel("y")
plt.title(r"$f(x) = 2^x$")

plt.plot(x,y)


#  f(x) = sinx & cosx
plt.figure(3)

plt.xlabel("x")
plt.ylabel("y")
plt.title(r"$f(x) = sinx & cosx$")
x = np.arange(-5,5,0.01)
y = np.sin(x)
plt.plot(x,y)
y = np.cos(x)
plt.plot(x,y)

#  f(x) = tanx
plt.figure(4)
x = np.arange(-0.49*np.pi,0.49*np.pi,0.01)
y = np.tan(x)
plt.xlabel("x")
plt.ylabel("y")
plt.title(r"$f(x) = tanx$")

plt.plot(x,y)


#  f(x) = arctanx
plt.figure(5)
x = np.arange(-5,5,0.01)
y = np.arctan(x)
plt.xlabel("x")
plt.ylabel("y")
plt.title(r"$f(x) = arctanx$")

plt.plot(x,y)


#  f(x) = arccosx & arcsinx
plt.figure(6)
x = np.linspace(-1,1,100)
y = np.arccos(x)
plt.xlabel("x")
plt.ylabel("y")
plt.title(r"$f(x) = arccosx & arcsinx$")
plt.plot(x,y)
y = np.arcsin(x)
plt.plot(x,y)


#  f(x) = x^-1
plt.figure(7)

plt.xlabel("x")
plt.ylabel("y")
plt.title(r"$f(x) = x^-1")
x = np.linspace(-1,1,100)
y = x**-1
plt.plot(x,y)


#  f(x) = x^-1 & x & x^2 & x^3
plt.figure(8)

plt.xlabel("x")
plt.ylabel("y")
plt.title(r"$f(x) = x^-1 & x & x^2 & x^3")
x = np.linspace(-1.5,1.5,100)
y = x
plt.plot(x,y)
y = x**2
plt.plot(x,y)
y = x**3
plt.plot(x,y)


#  f(x) = logx
plt.figure(9)

plt.xlabel("x")
plt.ylabel("y")
plt.title(r"$f(x) = logx")
x = np.linspace(-0.1,10,100)
y = np.log(x)
plt.plot(x,y)
plt.show()