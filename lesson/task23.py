"""
Задача №23. Решение в группах
Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
Примечание: Пользователь может вводить значения списка или список задан изначально.
"""
import random

list_1 = []
count = 0

for _ in range(5):
    i = random.randint(-1, 5)
    list_1.append(i)

list_2 = []

for i in range(1, len(list_1)):
    if list_1[i] > list_1[i - 1]:
        list_2.append(f'{list_1[i - 1]} < {list_1[i]}')
        count += 1

print(list_1)
print(f'{count} {" ".join(list_2)}')