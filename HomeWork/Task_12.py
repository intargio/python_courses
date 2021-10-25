def factorial(x):
    y = 1
    for i in range(1, x + 1):
        y *= i
    return y


a = 1
e = 1
while True:
    x = 1 / factorial(a)
    e += x
    a += 1
    if x <= 0.001:
        break
print(e)
    


