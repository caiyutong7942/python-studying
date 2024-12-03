for x in range(22):
    for y in range(33):
        z = 100-x-y
        if x*5+y*3+z/3 == 100:
            print(x,y,z)
            print(x*5,y*3,z/3)
            print("-------------")
