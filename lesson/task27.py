"""
Задача №27. Решение в группах
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore
I'm sure that the shells are sea shore shells
Output: 13
"""
# Ввод текста от пользователя
text = input("Введите текст: ")

# Разбиваем текст на слова, используя пробелы как разделители
words = text.split()

# Создаем множество для хранения уникальных слов
unique_words = set()

# Проходим по каждому слову и добавляем его в множество
for word in words:
    unique_words.add(word)

# Выводим количество уникальных слов
print(len(unique_words))