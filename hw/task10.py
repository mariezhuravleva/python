'''
Задача 10: На столе лежат n монеток. 
Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
'''

coin_sequence = input("Введите последовательность монет (1 для решки, 2 для орла): ")

count_heads = coin_sequence.count("2")
count_tails = coin_sequence.count("1")

min_flips = min(count_heads, count_tails)

print(f"Минимальное количество переворотов: {min_flips}")