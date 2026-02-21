def isEven(n):
    return (n & 1) == 0

for i in range(10):
    if isEven(i):
        print(i)