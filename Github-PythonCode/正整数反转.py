num = int(input("num="))
res_num=0

while num>0:
    res_num = res_num*10 + num%10
    num //= 10
    
print(res_num)