aStr = "Hello,World!"
bStr = aStr[:6] + "Python!"
print(bStr)

count = 0
for ch in bStr:
    if ch in ',.!?':   #计算标点符号
        count += 1
print(count)