palindrome = int(0)
for i in range(100, 1000):
    for j in range(100, 1000):
        z = i*j
        list_ = [int(y) for y in str(z)]
        list_r = list_.copy()
        list_r.reverse()
        if list_ == list_r and z > palindrome:
            palindrome = z
print(palindrome)
#ans = 906609
