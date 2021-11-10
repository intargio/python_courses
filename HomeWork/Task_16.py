# 1 DONE
N = int(input("1 Введите количество чисел, которые вы собираетесь вводить: "))
arr = []
for i in range(N):
    arr += [int(input("Введите число: "))]
print(arr)


# 2 DONE
N = int(input("2 Введите число: "))
arr = []
for i in range(N):
    arr += [i + 1]
print(arr)


# 3 DONE
N = 2 * int(input("3 Введите число: "))
arr = []
for i in range(N):
    if i % 2 == 0:
        arr += [i + 2]
print(arr)


# 4 DONE
N = 2 * int(input("4 Введите число: "))
arr = []
for i in range(N):
    if i % 2 == 0:
        arr += [i + 1]
print(arr)


# 5 DONE
N = 2 * int(input("5 Введите число: "))
arr = []
for i in range(N):
    arr += [2 ** i]
print(arr)


# 6 IN PROGRESS (Фибоначчи)


# 7 DONE
N = int(input("7 Введите число, с которого начнется список: "))
arr = []
for i in range(5):
    arr += [N - i]
print(arr)


# 8 DONE
N = int(input("8 Введите число: "))
arr = []
for i in range(N):
    if i % 2 == 0:
        arr += [0]
    else:
        arr += [1]
print(arr)


# 9 DONE
N = int(input("9 Введите число: "))
arr = []
for i in range(N):
    arr += [i + 1]
for i in range(N):
    if i > 0:
        arr += [N - i]        
print(arr)


# 9* DONE
N = int(input("9* Введите число: "))
arr = []
for i in range(round(N/2)):
    arr += [i + 1]
for i in range(N//2):
    arr += [N//2 - i]        
print(arr)


# 10 DONE
from random import randint
import math
N = int(input("10 Введите число: "))
arr = []
for i in range(N):
    arr += [randint(0, 1000000)]      
print(arr)