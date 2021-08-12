prime = []
isPrime = False
for i in range(2,100000000000000):
    if i == 2:
        prime.append(i)
    else:
        for j in prime:
            if i%j == 0:
                isPrime = False
                break
            else:
                isPrime = True
        if isPrime == True:
            prime.append(i)
            isPrime = False
    if len(prime) == 10001:
        break
print(prime[-1])
#ans = 104743
