import pandas as pd              # 导入Pandas库
import numpy as np              # 导入Numpy库
import matplotlib.pyplot as plt
import math

df = pd.read_csv(r'Data\5 iris.csv')
df.columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']

X = df.values[:,0:4]
y = df.values[:,4]

plt.figure(figsize=(8, 6))

for lab in ('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'):
    plt.hist(X[y==lab],
        label=lab,
        bins=10,
        alpha=0.3,)

plt.tight_layout()
plt.show()

#将特征数据标准化
from sklearn.preprocessing import StandardScaler
X_std = StandardScaler().fit_transform(X)
print (X_std) #打印所有结果

#计算协方差矩阵方法
mean_vec = np.mean(X_std, axis=0) #计算均值
cov_mat = (X_std - mean_vec).T.dot((X_std - mean_vec)) / (X_std.shape[0]-1) #协方差矩阵
print('协方差矩阵 \n%s' %cov_mat)

#计算特征值和特征向量
eig_vals, eig_vecs = np.linalg.eig(cov_mat)
print('特征值 \n%s' %eig_vecs)
print('\n特征向量 \n%s' %eig_vals)

#将特征值和特征向量对应
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]
print(eig_pairs)
print('----------')
eig_pairs.sort(key=lambda x: x[0], reverse=True)

#将结果转变成百分数
tot = sum(eig_vals)
var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)] #计算百分数
print('贡献率 \n%s' %var_exp)
cum_var_exp = np.cumsum(var_exp, dtype=list)#计算累加值
print('贡献率累加 \n%s' %cum_var_exp)

#提取前两个特征
matrix_w = np.hstack((eig_pairs[0][1].reshape(4,1),
                      eig_pairs[1][1].reshape(4,1)))
print('提取后的结果:\n', matrix_w)

Y = X_std.dot(matrix_w)

#可视化降维后的结果
plt.figure(figsize=(6, 4))
for lab, col in zip(('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'),
                        ('yellow', 'black', 'green')):
     plt.scatter(Y[y==lab, 0],
                Y[y==lab, 1],
                label=lab,
                c=col)
plt.xlabel('X')
plt.ylabel('Y')
plt.tight_layout()
plt.show()

