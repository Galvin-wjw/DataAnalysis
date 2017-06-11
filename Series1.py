import pandas
from pandas import Series
aSer = pandas.Series([1,2,'a'])
print(aSer,'\n')

bSer = pandas.Series(['apple','peach','lemon'],index=[1,2,3])
print(bSer,'\n')

#Series数据对齐
data = {'AXP':'86.4','CSCO':'122.64','BA':'99.44'}
sindex = ['AXP','CSCO','BA','AAPL']
cSer = pandas.Series(data,index=sindex)
print(cSer,'\n')

data1 = {'AXP':'88','CSCO':'122.64','CVX':23.78}
dSer = pandas.Series(data1)
print(cSer+dSer)