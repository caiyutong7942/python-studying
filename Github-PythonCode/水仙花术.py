for x in range(100,1000):
    ge = x%10
    shi = x//10%10
    bai = x//100
    if ge**3 + shi**3 + bai**3 ==x:
        print(x)
    