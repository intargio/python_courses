x = int(input("Введите число: "))
i = 1
y = 1
while i <= x:
    y *= i
    i += 1
print("Факториал числа", x, "равен", y, ".")