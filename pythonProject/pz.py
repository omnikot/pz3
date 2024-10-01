from fuzzywuzzy import fuzz
from fuzzywuzzy import process
str1, str2 = 'привет', 'привет'

def levenstein(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]
distance = levenstein(str1, str2)
print(f"Расстояние Левенштейна между '{str1}' и '{str2}': {distance}")

#обычное сравнение
a = fuzz.ratio('Привет мир', 'Привет мир')
print(a)

#Частичное сравнение
a = fuzz.partial_ratio('Привет мир', 'Привет мир!')
print(a)

#Сравнение по токену
a = fuzz.token_sort_ratio('Привет наш мир', 'мир наш Привет')
print(a)

a = fuzz.token_set_ratio('Привет наш мир', 'мир мир наш наш наш ПриВЕт')
print(a)

#Продвинутое обычное сравнение
a = fuzz.WRatio('Привет наш мир', '!ПриВЕт наш мир!')
print(a)

#Работа со списком
city = ["Москва", "Санкт-Петербург", "Саратов", "Краснодар", "Воронеж", "Омск", "Екатеринбург", "Орск", "Красногорск", "Красноярск", "Самара"]
a = process.extract("Саратов", city, limit=2)
# Параметр limit по умолчанию имеет значение 5
print(a)

