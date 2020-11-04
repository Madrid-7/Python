import pandas as pd

data1=pd.read_csv(r'Data\4 ReaderInformation.csv',sep=',')
data2=pd.read_csv(r'Data\4 ReaderRentRecode.csv',sep=',')
data_co=pd.merge(data1,data2,on='num')
print(data_co)
data_co.to_csv(r'Data\Compositon_data_out.csv',index=False,sep=',')