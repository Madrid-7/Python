import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
movie_data = pd.read_excel(r'Data\1 某县广电宽度数据.xls',encoding='gbk')
#print(movie_data.head())
charge_type = movie_data.收费类型
charge_type_num=movie_data['收费类型'].value_counts()
print("收费类型类别统计如下")
print(charge_type_num)
#print(movie_data.收费类型)
farm_net_num=0
normal_num=0
BT_num=0
for man_type in charge_type:
    if man_type =="农网居民":
        farm_net_num+=1
    elif man_type =="普通":
        normal_num+=1
    elif man_type == "广电系统":
        BT_num+=1
man_type_data=[farm_net_num,normal_num,BT_num]
man_type_labels=['农网居民','普通','广电系统']
#乱码设置
plt.rcParams['font.sans-serif']=['SimHei']
plt.axes(aspect='equal')
man_type_pie=plt.pie(x=man_type_data,labels=man_type_labels,pctdistance=0.8)
plt.title("该县收费类型分布图")
plt.show()