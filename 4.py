import random

# Заранее определенные значения для ключей и значений
keys_list = ["apple", "banana", "cherry", "watermellon", "pineapple"]
values_list = [random.randint(1, 15) for _ in keys_list]

# Создаем словарь из списков
my_dict = dict(zip(keys_list, values_list))

print("Словарь:", my_dict)
