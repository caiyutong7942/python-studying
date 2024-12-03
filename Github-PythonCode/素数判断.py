import math 
a = int(input("请输入一个数字："))
b = int(math.sqrt(a))
c = True
for x in range(2,b+1) :
    if a%x==0:
        c = False
        print("------------")
        break
if c and a!=1:
    print("是素数")
else:
    print("不是素数")
