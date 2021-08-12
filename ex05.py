Sum = int(0)
boo = False
for i in range(1, 1000000000000000):
    for j in range(1, 20):
        if i % j == 0:
            boo = True
        else:
            boo = False
            break
    if boo == True:
        Sum = i
        break
print(i)
#ans = 232792560
