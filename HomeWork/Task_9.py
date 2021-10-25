x = int(input("Введите число: "))
y = 1
for i in range(1, x+1):
    y *= i
print("Факториал числа {}, равен {}.".format(x, y))