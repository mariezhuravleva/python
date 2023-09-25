"""
Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
"""
def modify_str(input_str):
    # Разбиваем входную строку на отдельные слова
    words = input_str.split()
    
    # Создаем словарь для отслеживания количества повторений каждого слова
    word_count = {}
    
    # Создаем новый список для модифицированных слов
    modified_words = []

    for word in words:
        if word in word_count:
            # Увеличиваем счетчик и форматируем слово с постфиксом
            word_count[word] += 1
            modified_word = f"{word}_{word_count[word] - 1}"
        else:
            # Если это первое вхождение слова, не добавляем постфикс
            word_count[word] = 1
            modified_word = word

        # Добавляем модифицированное слово в новый список
        modified_words.append(modified_word)

    # Объединяем модифицированные слова в строку и возвращаем результат
    return " ".join(modified_words)

# Входная строка
input_str = "a a a b c a a d c d d"

# Вызываем функцию и выводим результат
modified_str = modify_str(input_str)
print(modified_str)