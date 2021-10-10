from fractions import Fraction 
e = Fraction(0)
f = Fraction(1)
n = Fraction(1)
while True:
    d = Fraction(1) / f 
    if d < Fraction(1, 10**40): 
        break
    e += d 
    f *= n 
    n += Fraction(1) 
print("Можете объяснить как это работает, когда проверите?. И как убрать лишний пробел перед точкой в конце? Число е равно: ",float(e), ".")