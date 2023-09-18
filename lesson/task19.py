"""
Задача №19. Решение в группах
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
"""
num_k = int(input('Введите число K: '))
list_1 = [1, 2, 3, 4, 5]

if num_k >= 0 and num_k < len(list_1):
    shifted_list = list_1[-num_k:] + list_1[:-num_k]
    print(shifted_list)
else:
    print('Некорректное значение K')