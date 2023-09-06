import random
# Создаем пустой кортеж, в который будем добавлять случайные числа
random_numbers = ()

# Генерируем 10 случайных чисел и добавляем их в кортеж
for _ in range(10):
    random_number = random.randint(1, 100)
    random_numbers = random_numbers + (random_number,)
#random_numbers = tuple(random.randint(1, 100) for _ in range(10))

# Находим максимальный и минимальный элементы в кортеже
max_number = max(random_numbers)
min_number = min(random_numbers)

# Выводим результаты
print("Случайные числа:", random_numbers)
print("Максимальное число:", max_number)
print("Минимальное число:", min_number)