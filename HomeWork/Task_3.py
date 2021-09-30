# Task: Create algorythm that accepts a number and returns a sqaure root of the number. (Google the algorythm).
# Do not use math functions, implement any desired matimatical algorithm. Input and output from console.
# Input: integer number
# Output: square root of the number
#
# Example:
#   Enter number: 144
#   Square root of 144 is 12
#
# Write your solution below.
x = int(input("Введите число, из которого необходимо извлечь квадратный корень: "))
y = x ** (0.5)
print("Квадратный корень из числа "+str(x)+" это "+str(y)) 