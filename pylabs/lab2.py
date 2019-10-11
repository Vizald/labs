from math import *

number = int(input("Какую переменную ищем?(1-3): "))

if number == 1:
    a = float(input("Введите a:"))
    x = float(input("Введите x:"))
    g = - (16 * a * a + 24 * a * x - 27 * x * x) / (45 * a * a - 29 * a * x + 4 * x * x)
    print("G =", g)
elif number == 2:
    a = float(input("Введите a:"))
    x = float(input("Введите x:"))
    f = -atan(10 * a * a + 13 * a * a - 30 * x * x)
    print("F =", f)
elif number == 3:
    a = float(input("ВВедите a:"))
    x = float(input("Введите x:"))
    y = log(2 * a * a + 19 * a * x + 9 * x * x + 1) / log(10)
    print("Y =", y)
else:
    print("Вы ввели неправильное число :(")

