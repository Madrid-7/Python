import xlrd
import numpy as np

shuju = xlrd.open_workbook("C:/Users/如雨随行/Desktop/大数据数学基础/exec7.6.xlsx")
booksheet = shuju.sheet_by_index(0)
data = np.zeros((50, 7))
for i in range(50):
    rows = booksheet.row_values(i + 1)
    for j in range(1, 8):
        data[i][j - 1] = rows[j]
data = data.T

cov = np.cov(data)
print('\n协方差矩阵：\n', cov)

eig_val_cov, eig_vec_cov = np.linalg.eig(cov)

eig_val_cov = eig_val_cov[np.argsort(-eig_val_cov)]
print('\n特征值：', eig_val_cov)
print('\n特征向量：\n', eig_vec_cov)
print('\n')

for i in range(0, len(eig_val_cov)):
    contribution = eig_val_cov[i] / sum(eig_val_cov)
    print('第{}主成分的贡献率：{}'.format(i + 1, contribution))

print('\n')
for i in range(1, len(eig_val_cov) + 1):
    accumulated_contribution = sum(eig_val_cov[:i]) / sum(eig_val_cov)
    print('前{}个主成分的累计贡献率： {}'.format(i, accumulated_contribution))
