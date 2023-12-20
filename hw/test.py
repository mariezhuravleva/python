# Введите ваше решение ниже
import warnings

warnings.filterwarnings('ignore')

# Тест 1
# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# stroka = 'по-русски говорят'
# stroka = 'мо-локо и мёд'
# stroka = 'как ве-тер сме-ёт лис-ти'
# stroka = 'за-гад-ка-ра-свет-ка-ра-газ-да-не-на-ма-ли-ва-ла'
# stroka = 'со-лнце-гре-ет ве-сной'
stroka = 'Пух'

def count_vowels(word):
    vowels = "АЕЁИОУЫЭЮЯаеёиоуыэюя"  # Гласные буквы
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count

def check_rhythm(pooh_poem):
    phrases = pooh_poem.split()

    if len(phrases) <= 1:
        return "Количество фраз должно быть больше одной!"

    # Собираем список ритмов для каждой фразы
    rhythms = [count_vowels(phrase.replace('-', '').lower()) for phrase in phrases]

    # Если все ритмы одинаковы, возвращаем "Парам пам-пам", иначе "Пам парам"
    if all(rhythm == rhythms[0] for rhythm in rhythms):
        return "Парам пам-пам"
    else:
        return "Пам парам"

result = check_rhythm(stroka)
print(result)