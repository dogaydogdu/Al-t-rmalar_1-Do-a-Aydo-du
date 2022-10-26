X=[]

for i in range(1,10):
    
    for y in range(0,10):

        for a in range(0,10):

            for b in range(0,10):

                for c in range(0,10):

                    if str(i)+str(y)==str(b)+str(a):

                        sayı=str(i)+str(y)+str(a)+str(b)+str(c)
                        X.append(int(sayı))
                        
print("koşulu sağlayan sayı miktarı=",len(X))
