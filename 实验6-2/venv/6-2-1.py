# -*- coding: utf-8 -*-

import xlrd
import numpy as np
import matplotlib.pylab as plt
import scipy.cluster.vq as vq
import scipy.cluster.hierarchy as sch


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

workbook = xlrd.open_workbook("C:/Users/如雨随行/Desktop/大数据数学基础/exec6.5.xlsx")
booksheet = workbook.sheet_by_index(0)
data = np.zeros((55,8))
for i in range(55):
    rows = booksheet.row_values(i+1)
    for j in range(2,10):
        data[i][j-2] = rows[j]

data1 = vq.whiten(data)

Ave = sch.linkage(data1, method='average')
P = sch.dendrogram(Ave)
plt.xlabel('类别标签')
plt.ylabel('距离')
plt.title('类平均法')
plt.show()

Ward = sch.linkage(data1, method='ward')
P = sch.dendrogram(Ward)
plt.xlabel('类别标签')
plt.ylabel('距离')
plt.title('离差平方和法')
plt.show()

kmeans_cent = vq.kmeans(data1, 5)
print('聚类中心为：\n', kmeans_cent[0])

p = plt.figure(figsize=(16,16))
plt.title('聚类中心散点图')
for i in range(8):
    for j in range(8):
        ax = p.add_subplot(8,8,i*8+1+j)
        plt.scatter(data1[:, j], data1[:, i])
        plt.scatter(kmeans_cent[0][:, j], kmeans_cent[0][:, i], c='r')

plt.show()