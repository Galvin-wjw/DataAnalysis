name = ["Wangdachui","Niuyun","Liuling","Tianqi"]
salaries = [3000,2000,4500,8000]
d = dict(zip(name,salaries))  #生成字典
print(d)

for k,v in d.items():
    print(k,v)