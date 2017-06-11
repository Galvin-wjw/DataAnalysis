import numpy
xArray = numpy.ones((3,4))
print(xArray)

aArray = numpy.array([1,2,3])
print(aArray)

import pandas
from pandas import Series
bSer = pandas.Series(['apple','peach','lemon'],index=[1,2,3])
print(bSer[2])