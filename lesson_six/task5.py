from sys import getsizeof

first_letter = ord(input('Введите первую букву: \n'))
second_letter = ord(input('Введите вторую букву: \n'))
first_letter = first_letter - ord('a') + 1
print(getsizeof(first_letter))
second_letter = second_letter - ord('a') + 1
print(getsizeof(second_letter))
print(f'Первая буква на позиции: {first_letter}, вторая: {second_letter}')
print(f'Между буквами {abs(first_letter-second_letter)-1} символов')


# Опять получилось везде по 28 байт, тк везде цифры из-за ord. Итого 56 байт на переменные
