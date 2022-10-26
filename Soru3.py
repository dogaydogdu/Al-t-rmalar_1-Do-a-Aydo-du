x=0
for i in range(1,999):
    y=1
    for a in range(1,i):
        y*=a
        x+=1/y
        print(x)
