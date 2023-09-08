# Создаем словарь с информацией о товарах
jewelry_store = {
    "Кольцо": ["золото", 5000, 10],
    "Цепочка": ["серебро", 1500, 20],
    "Серьги": ["золото", 3500, 15],
    "Браслет": ["серебро", 2000, 25],
}

def print_description():
    for item, info in jewelry_store.items():
        print(f"{item} - {info[0]}")

def print_prices():
    for item, info in jewelry_store.items():
        print(f"{item} - {info[1]} рублей")

def print_quantities():
    for item, info in jewelry_store.items():
        print(f"{item} - {info[2]} штук")

def print_all_info():
    for item, info in jewelry_store.items():
        print(f"{item} - {info[0]}, Цена: {info[1]} рублей, Количество: {info[2]} штук")

def buy_item(item, quantity):
    if jewelry_store[item][2] >= quantity:
        price = jewelry_store[item][1] * quantity
        jewelry_store[item][2] -= quantity
        print(f"Вы купили {quantity} штук товара '{item}' за {price} рублей.")
    else:
        print(f"Извините, у нас нет столько товара '{item}'.")


while True:
    print("\nМеню:")
    print("1. Просмотр описания")
    print("2. Просмотр цен")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. Выход")

    choice = input("Выберите действие (1-6): ")

    if choice == "1":
        print_description()
    elif choice == "2":
        print_prices()
    elif choice == "3":
        print_quantities()
    elif choice == "4":
        print_all_info()
    elif choice == "5":
        item = input("Введите название товара (или 'n' для возврата в меню): ")
        if item == 'n':
            continue
        if item in jewelry_store:
            while True:
                St = input("Введите количество товара: ")
                try:
                    quantity = int(St)
                    if quantity > 0:
                        break
                    else:
                        print("Введите положительное натуральное число.")
                except ValueError:
                    print("Некорректный ввод. Введите натуральное число.")
            buy_item(item, quantity)
        else:
            print("Такого товара нет!")

    elif choice == "6":
        print("Спасибо за покупки! До свидания!")
        break
    else:
        print("Некорректный ввод. Пожалуйста, выберите действие из меню.")
