#--*-- coding:utf-8 --*--
import tushare
from matplotlib.font_manager import FontProperties
from pandas import *
import matplotlib.pyplot as plt

data1 = tushare.get_hist_data('601992',start='2017-05-01',end='2017-05-31') #金隅股份
frame = pandas.DataFrame(data1)
#frame.index = range(1,len(data1)+1)  #换索引

# writer = pandas.ExcelWriter('金隅股份.xlsx')
# f = frame.to_excel(writer,sheet_name='sheet1')
# writer.save()

open_price = frame['open']
line1 = open_price.sort_index(ascending=True)
line1.plot(label = 'open_price')

close_price = frame['close']
line2 = close_price.sort_index(ascending=True)
line2.plot(label = 'close_price')
plt.legend()
#中文字体设置
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)
plt.title(u'中文',fontproperties = font_set)
plt.title("金隅股份5月开盘收盘价分析")
plt.grid(True)
plt.show()

print("30日最高价:",frame['high'].max(),'\n')
print("收盘价高于8块的日期：\n" , frame[frame.close>8],'\n')
print("30日最高价平均值:" , frame['high'].mean(),'\n')


