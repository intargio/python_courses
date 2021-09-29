# Task: Create a program that prints a rectangle with X width and Y height using "X" symbol.
# Input: integer X, integer Y.
# Output: rectange out of X'es.
#
# Example:
#   Enter height: 3
#   Enter width: 4
#   XXXX
#   X  X
#   XXXX
#
# Write your solution below.
x = int(input("Напишите ширину прямоугольника: "))
y = int(input("Напишите длина прямоугольника: "))
print("Ваш прямоугольник:")
print(x * "X")
for i in range(2, y):
    print("X" +  (x - 2) * " " + "X")
print(x * "X")
