num = 600851475143
factor = []
for i in range(1, 100000):
    if num % i == 0:
        factor.append(i)
        num = num/i
        i -= 1
    if num == 1:
        break;
print(factor)
#ans = 6857
