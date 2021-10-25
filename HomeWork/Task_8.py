
def my_max(first, second):
    if first > second:
        return first
    else:
        return second


count = int(input("Введите N чисел: "))

max = int(input("Введите число: "))

for i in range(1, count):
    number = int(input("Введите число: "))
    max = my_max(max, number)

print(max)