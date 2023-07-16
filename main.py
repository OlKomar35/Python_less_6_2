# TЗадача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)
import random

print(arr := [random.randint(-10,10) for _ in range(int(input('n= ')))])
min_val_range = int(input('min= '))
max_val_range = int(input('max= '))

for i in range(len(arr)):
    if max_val_range >= arr[i] >= min_val_range:
        print(i, end=' ')

