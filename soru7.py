a = []
for i in range(100,1000):
    sayı = list(str(i))
    if int(sayı[0])+int(sayı[1]) == int(sayı[-1]):
        a.append(i)
        print(i)
print(len(a))
