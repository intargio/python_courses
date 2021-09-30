x = int(input("Введите число: "))
y = 1
for i in range(1, x+1):
    y += i
print("Сумма чисел от 1 до ", x, "равна", y-1, ".")