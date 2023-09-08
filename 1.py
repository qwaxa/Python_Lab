import random
while True:
    St = input("Введите натуральное число: ")
    try:
        number = int(St)
        if number > 0:
            break
        else:
            print("Введите положительное натуральное число.")
    except ValueError:
        print("Некорректный ввод. Введите натуральное число.")

sum_of_digits = 0
for digit_str in str(number):
    digit = int(digit_str)
    sum_of_digits += digit

print("Сумма цифр введенного числа:", sum_of_digits)
































