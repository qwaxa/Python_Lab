import random
# Получаем от пользователя желаемую длину списков
list_length = int(input("Введите длину списков: "))

# Создаем пустые списки для ключей и значений
keys_list = []
values_list = []

# Заполняем список ключей
print("Введите ключи:")
for _ in range(list_length):
    key = input("Ключ: ")
    keys_list.append(key)

# Заполняем список значений

for _ in range(list_length):

    values_list.append(random.randint(1,15))

# Создаем словарь из списков
my_dict = dict(zip(keys_list, values_list))

print("Словарь:", my_dict)
