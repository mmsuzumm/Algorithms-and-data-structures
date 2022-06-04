# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

first_letter = ord(input('Введите первую букву: \n'))
second_letter = ord(input('Введите вторую букву: \n'))
first_letter = first_letter - ord('a') + 1
second_letter = second_letter - ord('a') + 1
print(f'Первая буква на позиции: {first_letter}, вторая: {second_letter}')
print(f'Между буквами {abs(first_letter-second_letter)-1} символов')
