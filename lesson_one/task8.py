# Определить, является ли год, который ввел пользователем, високосным или невисокосным.

year = int(input('Введите год:\n'))
if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print("Обычный")
else:
    print("Високосный")
