import random

suiji = random.randint(1,100)

count = 0

while 1:
    a = int(input("请输入你猜的数字："))
    count+=1
    if a > suiji:
        print("猜大了")
        
    elif a < suiji:
        print("猜小了")
    elif a == suiji:
        print("猜对了")
        break
print(f"count={count}")

