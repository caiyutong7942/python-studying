n = 20
lis = []

for i in range(n):
    if i==0 or i==1:
        lis.append(1)
    else:
        lis.append(lis[i-1]+lis[i-2])
    print(lis)