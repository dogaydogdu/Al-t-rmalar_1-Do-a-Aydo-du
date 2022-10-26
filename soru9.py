X=[]

for i in range(1,10):
    
    for y in range(0,10):

        for a in range(0,10):

            if (i+y+a)<9:

                sayı=str(i)+str(y)+str(a)
                X.append(int(sayı))

print(X)    
print("koşulu sağlayan sayıların miktarı=",len(X))
