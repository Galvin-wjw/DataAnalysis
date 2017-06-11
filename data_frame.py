import pandas
list = [('Wangdachui',4000),('Lingling',5000),('Niuyun',6000)]
frame = pandas.DataFrame(data=list,index=range(1,4),columns=['name','pay'])
print(frame,'\n')
print(frame['name'],'\n')
print(frame['pay'].min(),'\n')
print(frame[frame.pay>=5000],'\n')


list1 = {'name':['Wangdachui','Lingling','Niuyun'],'pay':[4000,5000,6000]}
frame1 = pandas.DataFrame(list1,index=range(1,4))
print(frame1)