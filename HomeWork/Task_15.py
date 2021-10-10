def fibonacci(i):
    import math
    SQRT5 = math.sqrt(5)
    PHI = (SQRT5 + 1) / 2
    return int(PHI ** i / SQRT5 + 0.5)
 


for i in range(int(input("Введите нужное количество чисел Фибоначчи: " ))):
    print("Порядковый номер числа:", i+1)
    print("Число Фибоначчи:",fibonacci(i))