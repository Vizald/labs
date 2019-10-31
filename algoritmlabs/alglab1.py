from random import randint

array = []
n = 30
symmmin = 0
symmmax = 0

for i in range(n):
    array.append(randint(1, 999))
    print(array[i], end=" ")

for i in range(n - 1):
    for j in range(n - i - 1):
        if array[j] > array[j + 1]:
            per = array[j]
            array[j] = array[j + 1]
            array[j + 1] = per

for i in range(n):
    print(array[i], end=" ")
print()

for i in range(n):
    if i <5:
        symmmin += array[i]
    elif i >n-6:
        symmmax += array[i]
print(symmmin)
print(symmmax)
