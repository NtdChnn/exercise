addSquares = int(0)
squaresAdd = int(0)
for i in range(1, 101):
    squaresAdd += i*i
    addSquares += i
addSquares = addSquares*addSquares
different = addSquares - squaresAdd
print(different)
#ans = 25164150
