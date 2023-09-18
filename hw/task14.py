'''
Задача 14: Требуется вывести все целые степени двойки 
(т.е. числа вида 2k), не превосходящие числа N.
'''
N = int(input("Введите число N: "))

current_power = 1
result = []

while current_power <= N:
    print(current_power, end=" ")
    current_power *= 2