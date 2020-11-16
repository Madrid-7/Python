import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

io = r'Data\2.xlsx'
data = pd.read_excel(io, sheet_name = 0, usecols = [2, 3], skiprows = [1])

print(data)
print('\n平均值：')
print(data.mean())

print('\n方差：')
print(data.var())
print('\n标准差：')
print(data.std())

plt.figure(1)
plt.rcParams['font.sans-serif']=['SimHei']    #处理中文乱码
plt.boxplot(x=[data["西安"],data["北京"]],    #指定绘图数据

            labels=["西安","北京"],
            patch_artist=True,  # 要求用自定义颜色填充盒形图，默认白色填充
            showmeans=True,  # 以点的形式显示均值
            boxprops={'color': 'black', 'facecolor': '#9999ff'},  # 设置箱体属性，填充色和边框色
            flierprops={'marker': 'o', 'markerfacecolor': 'red', 'color': 'black'},  # 设置异常值属性，点的形状、填充色和边框色
            meanprops={'marker': 'D', 'markerfacecolor': 'indianred'},  # 设置均值点的属性，点的形状、填充色
            medianprops={'linestyle': '--', 'color': 'orange'})  # 设置中位数线的属性，线的类型和颜色

plt.figure(2)

sns.violinplot(x = None, # 指定x轴的数据
               y = None, # 指定y轴的数据
               data = data) # 指定绘图的数据集

plt.show()