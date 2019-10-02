from math import *

a = float(input())
x = float(input())
g = - (16 * a * a + 24 * a * x - 27 * x * x) / (45 * a * a - 29 * a * x + 4 * x * x)
print(g)

a = float(input())
x = float(input())
f = -atan(10 * a * a + 13 * a * a - 30 * x * x)
print(f)

a = float(input())
x = float(input())
y = log(2 * a * a + 19 * a * x + 9 * x * x + 1) / log(10)
print(y)
