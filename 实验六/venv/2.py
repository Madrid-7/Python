import numpy as np
from scipy import optimize

x1 = np.array([4,3,4,2,2,2,3,4,3,2])
x2 = np.array([9.3,4.8,8.9,6.5,4.2,6.2,7.4,6.0,7.6,6.1])
y = np.array([100,50,100,100,50,80,75,65,90,90])

def regula(p):
    a,b,c = p
    return y - a - b * x1 - c * x2

result = optimize.least_squares(regula, [0,1,1])
a,b,c = result.x
print("设x1表示运输次数，x2表示运输时间，y表示运输里程")
print("设拟合函数为y = a + b * x1 + c * x2，则由最小二乘法得到：")
print("a = %f，b = %f，c = %f" %(a,b,c))
print("即得到的拟合函数为：y = %f %f * x1 + %f * x2" %(a,b,c))
