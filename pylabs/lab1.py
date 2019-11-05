from math import *

a = float(input("Введите a:"))
x = float(input("Введите x:"))
g = - (16 * a ** 2 + 24 * a * x - 27 * x ** 2) / (45 * a ** 2 - 29 * a * x + 4 * x ** 2)
print("G =", g, end="")

a = float(input("Введите a:"))
x = float(input("Введите x:"))
f = -atan(10 * a ** 2 + 13 * a * x - 30 * x ** 2)
print("F =", f, end="")

a = float(input("ВВедите a:"))
x = float(input("Введите x:"))
y = log(2 * a ** 2 + 19 * a * x + 9 * x ** 2 + 1) / log(10)
print("Y =", y, end="")
