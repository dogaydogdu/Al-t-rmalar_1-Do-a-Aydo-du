x = []
for i in range(1000,10000):
    sayı = list(str(i))
    if sayı[0] > sayı[-1]:
        x.append(i)
print(len(x))
