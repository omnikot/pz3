import time
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Строки для сравнения
str1, str2 = 'привет', 'привет'

# Функция Левенштейна
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

# Измерение времени выполнения Левенштейна
start_time = time.time()
distance = levenstein(str1, str2)
end_time = time.time()

# Вывод расстояния Левенштейна и времени выполнения
print(f"Расстояние Левенштейна между '{str1}' и '{str2}': {distance}")
print(f"Время выполнения: {end_time - start_time:.6f} секунд")
print(f"m * n = {len(str1) * len(str2)}")

# Пример использования fuzzywuzzy

# Обычное сравнение
a = fuzz.ratio('Привет мир', 'Привет мир')
print(f"Обычное сравнение: {a}")

# Частичное сравнение
a = fuzz.partial_ratio('Привет мир', 'Привет мир!')
print(f"Частичное сравнение: {a}")

# Сравнение по токенам
a = fuzz.token_sort_ratio('Привет наш мир', 'мир наш Привет')
print(f"Сравнение по токенам (сортировка): {a}")

a = fuzz.token_set_ratio('Привет наш мир', 'мир мир наш наш наш ПриВЕт')
print(f"Сравнение по токенам (множества): {a}")

# Продвинутое обычное сравнение
a = fuzz.WRatio('Привет наш мир', '!ПриВЕт наш мир!')
print(f"Продвинутое сравнение: {a}")

# Работа со списком
city = ["Москва", "Санкт-Петербург", "Саратов", "Краснодар", "Воронеж", "Омск",
        "Екатеринбург", "Орск", "Красногорск", "Красноярск", "Самара"]

a = process.extract("Саратов", city, limit=2)
print(f"Результат работы со списком: {a}")


# Функция для замера времени выполнения
def measure_time(func, *args, iterations=1000):
    total_time = 0
    for _ in range(iterations):
        start_time = time.time()
        func(*args)
        total_time += time.time() - start_time
    return total_time / iterations

# Строки для сравнения
str1, str2 = 'привет', 'привет мир'

# Замер времени Левенштейна
levenstein_time = measure_time(levenstein, str1, str2)
print(f"Среднее время выполнения Левенштейна: {levenstein_time:.6f} секунд")

# Замер времени для fuzzywuzzy
fuzz_time = measure_time(fuzz.ratio, str1, str2)
print(f"Среднее время выполнения fuzz.ratio: {fuzz_time:.6f} секунд")

# Сравнение скорости выполнения
if levenstein_time < fuzz_time:
    print("Функция Левенштейна выполняется быстрее.")
else:
    print("Операции fuzzywuzzy выполняются быстрее.")
