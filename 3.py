import random
while True:
    list_length_str = input("Введите длину списка ")
    try:
        list_length= int(list_length_str)
        if list_length > 0:

            break
        else:
            print("Введите положительное натуральное число.")
    except ValueError:
        print("Некорректный ввод. Введите натуральное число.")

my_list = []
product=1
max_element = None  # Инициализируем переменную для максимального элемента
for i in range (list_length):
    number = random.randint(1, 10)
    my_list.append(number)
    if max_element is None or number > max_element:
        max_element = number
    if number%2==1:
        product*=number
print("Список случайных чисел:", my_list)
print("Произведение нечетных элементов:", product)
print("Наибольший элемент:", max_element)
# Удаляем наибольший элемент из списка
my_list.remove(max_element)
print("Список после удаления наибольшего элемента:", my_list)
my_list.sort(reverse=True)
# Выводим на экран три наибольших элемента
print("Три наибольших элемента списка:", my_list[:3])