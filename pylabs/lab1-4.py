from math import *

arrayG = []
arrayF = []
arrayY = []
arrayA = []
arrayX = []

while True:
    a = int(input("Введите a:"))
    x = int(input("Введите x:"))
    number = int(input("Какую переменную ищем?(1-3; 1-G, 2-F, 3-Y): "))
    step = int(input("Какой шаг?: "))
    count = int(input("Сколько шагов?: "))
    if number == 1:
        for i in range(count):
            if ((45 * a * a - 29 * a * x + 4 * x * x) != 0):
                g = - (16 * a * a + 24 * a * x - 27 * x * x) / (45 * a * a - 29 * a * x + 4 * x * x)
                arrayG.append(g)
                arrayA.append(a)
                arrayX.append(x)
                print("G =", arrayG[i], "a =", arrayA[i], "x =", arrayX[i])
                a += step
                x += step
            else:
                print("На ноль делить нельзя ^-^")
        print("Минимальное значение:", min(arrayG), "Максимальное значение:", max(arrayG))
        continuation = str(input("Продолжить?(да/нет): "))
        if continuation == "да":
            arrayG.clear()
            arrayA.clear()
            arrayX.clear()
            continue
        else:
            break
    elif number == 2:
        for i in range(count):
            f = -atan(10 * a * a + 13 * a * a - 30 * x * x)
            arrayF.append(f)
            arrayA.append(a)
            arrayX.append(x)
            print("F =", arrayF[i], "a =", arrayA[i], "x =", arrayX[i])
            a += step
            x += step
        print("Минимальное значение:", min(arrayF), "Максимальное значение:", max(arrayF))
        continuation = str(input("Продолжить?(да/нет): "))
        if continuation == "да":
            arrayF.clear()
            arrayA.clear()
            arrayX.clear()
            continue
        else:
            break
    elif number == 3:
        for i in range(count):
            if (2 * a * a + 19 * a * x + 9 * x * x + 1) >= 0:
                y = log(2 * a * a + 19 * a * x + 9 * x * x + 1) / log(10)
                arrayY.append(y)
                arrayA.append(a)
                arrayX.append(x)
                print("Y =", arrayY[i], "a =", arrayA[i], "x =", arrayX[i])
                a += step
                x += step

            else:
                print("Log отрицательный =(")
        print("Минимальное значение:", min(arrayY), "Максимальное значение:", max(arrayY))
        continuation = str(input("Продолжить?(да/нет): "))
        if continuation == "да":
            arrayY.clear()
            arrayA.clear()
            arrayX.clear()
            continue
        else:
            break
    else:
        print("Вы ввели неправильную переменную :(")
