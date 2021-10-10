def my_max(first, second):
    if a > b:
        print(a, "больше чем", b)
    if a < b:
        print(b, "больше чем", a)
    else:
        print(a, "равно", b)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
my_max(a, b)