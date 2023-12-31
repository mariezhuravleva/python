"""
Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод: 
1 2 3 2 3 
Вывод:
2
"""
# Ввод списка чисел
numbers = input("Введите список чисел, разделяя их пробелами: ").split()

# Создаем словарь для подсчета количества вхождений каждого числа
count_dict = {}

# Проходим по списку чисел и подсчитываем вхождения каждого числа
for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

# Ищем количество пар
pair_count = 0
for count in count_dict.values():
    pair_count += count // 2

# Выводим количество пар
print("Количество пар элементов, равных друг другу:", pair_count)