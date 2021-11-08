def fibonacci(n):
    a = 0
    b = 1
    for n in range(n):
        a, b = b, a + b
    return a


for i in range(10):
    print(fibonacci(i)) # 0 1 1 2 3 5 8 13 21 34