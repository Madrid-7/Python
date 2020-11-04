import numpy as np
from scipy import optimize

x = np.array([12,21,27,31,35,44,62])
y = np.array([652,743,836,941,1190,1556,1845])

def regula(p):
    a,b = p
    return y - a - b * x

result = optimize.least_squares(regula, [0,0])
a,b = result.x
print("设x表示分店数量，y表示盈利额")
print("设拟合函数为y = a + b * x，由最小二乘法估计得：")
print("a = %f, b = %f" %(a,b))
print("即得到的拟合函数为：y = %f + %f * x" %(a,b))
print("根据预测，2020年达到的盈利额为：%d" %(a + b * 100))
