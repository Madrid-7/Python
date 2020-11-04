import pandas as pd              # 导入Pandas库
import numpy as np              # 导入Numpy库

df = pd.read_csv(r'Data\3 movie_metadata.csv', sep=',')

# # 查看哪些值缺失
# nan_all = df.isnull()      # 获得所有数据框中的N值
# print(nan_all)          # 打印输出
# # 查看哪些列缺失
# nan_col1 = df.isnull().any()    # 获得含有NA的列
# nan_col2 = df.isnull().all()    # 获得全部为NA的列
# print(nan_col1)              # 打印输出
# print(nan_col2)              # 打印输出

#缺失值处理
df1 = df.dropna()
print(df1)                      # 打印输出

#异常值处理
df_zscore = df1.copy()                  # 复制一个用来存储Z-score得分的数据框
cols = df1.columns                  # 获得数据框的列名
df_col = df1['num_critic_for_reviews']                  # 得到每列的值
z_score = (df_col - df_col.mean()) / df_col.std()  # 计算每列的Z-score得分
df_zscore['num_critic_for_reviews'] = z_score.abs() > 2.2        # 判断Z-score得分是否大于2.2，如果是则为True，否则为False
df2 = df1[df_zscore['num_critic_for_reviews'] == False]

#重复值处理
df3 = df2.drop_duplicates()

#数据导出
df3.to_csv("Data\out.csv",index=False,sep=',')