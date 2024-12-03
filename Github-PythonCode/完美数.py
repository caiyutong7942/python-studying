for h in range(2,10000):
    count = 0
    for j in range(2,h):
        if h % j == 0:
            count+=j
    if count == h:   #这里啥错了
        print(h)
# 为什么打不出来结果