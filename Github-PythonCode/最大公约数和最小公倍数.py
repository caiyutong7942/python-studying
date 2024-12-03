x = int(input("请输入第一个数："))
y = int(input("请输入第二个数："))

if x>y:
    x,y=y,x

print(x,y)
for factor in range(x,0,-1):
    if x % factor == 0 and y % factor == 0:
        print(f"{x}和{y}的最大公约数是{factor}")
        print(f"{x}和{y}的最小公倍数是{x * y // factor}")
        break