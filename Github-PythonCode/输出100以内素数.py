# 输出100以内所有的素数
import math
for i in range(2,100):
    end = int(math.sqrt(i))
    flag = True
    for j in range(2,end+1):
        if i % j == 0:
            flag=False

    if flag:
        print(i)