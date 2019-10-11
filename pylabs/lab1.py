from math import *

a = float(input("Введите a:"))
x = float(input("Введите x:"))
g = - (16 * a * a + 24 * a * x - 27 * x * x) / (45 * a * a - 29 * a * x + 4 * x * x)
print("G =",g)

a = float(input("Введите a:"))
x = float(input("Введите x:"))
f = -atan(10 * a * a + 13 * a * a - 30 * x * x)
print("F =",f)

a = float(input("ВВедите a:"))
x = float(input("Введите x:"))
y = log(2 * a * a + 19 * a * x + 9 * x * x + 1) / log(10)
print("Y =",y)
