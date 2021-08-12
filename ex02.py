Fibonacci = []
Sum = int(0)
for i in range(1,100):
    if i <= 2:
        Fibonacci.append(i)
    else:
        x = Fibonacci[i-2]+Fibonacci[i-3]
        Fibonacci.append(x)
    if Fibonacci[i-1] <= 4000000 and Fibonacci[i-1] % 2 == 0:
        Sum += Fibonacci[i-1]
    if Fibonacci[i-1] > 4000000:
        break
print(Sum)
#ans = 4613732
