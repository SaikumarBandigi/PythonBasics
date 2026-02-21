def fib(n):
    global third
    if n == 0:
        return 0
    if n == 1:
        return 1

    first = 0
    second = 1

    for i in range(2, n + 1):
        third = first + second
        first = second
        second = third

    return third


for i in range(10):
    print(fib(i), end=" ")