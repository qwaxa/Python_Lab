

#является ли
def is_palindrome(word):
    # Функция для проверки, является ли слово палиндромом
    return word == word[::-1]

# Ввод строки текста
text = input("Введите строку текста: ")

# Разбиваем строку на слова
words = text.split()

# Итерируемся по словам и выводим палиндромы
print("Палиндромы в строке:")
for word in words:
    if is_palindrome(word):
        print(word)
#for commit