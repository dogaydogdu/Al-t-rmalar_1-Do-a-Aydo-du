a = []
for i in range(100,1000,2):
    sayı = list(str(i))
    if sayı[0] == sayı[1] or sayı[0] == sayı[2]:
        a.append(i)
print(len(a))
