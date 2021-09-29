# Task: Create a programm, that will calculare volume of a sphere by its radius(google the formula, use Pi=3.14). Input and output from console.
# Input: float number.
# Output: volume of a sphere(float number).
#
# Example:
#   Enter radius: 4.5
#   Volume of a spehere with radius 4.5 is 381.51
#
# Write your solution below.
r = float(input("Напишите радиус вашей сферы в метрах: "))
v = ( 4 / 3 ) * 3.14 * ( r ** 3 )
print("Объем вашей сферы равен ", v, " кубических метров.")