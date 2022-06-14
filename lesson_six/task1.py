from sys import getsizeof

number = int(input('Введите трехзначное число\n'))
i = 0  # 24
sum_ = 0  # 24
multiple = 1 # 28
while i < 3:
    print('i: ' + str(getsizeof(i)))
    i += 1  # 28
    print('sum:' + str(getsizeof(sum_)))
    sum_ += number % 10  # 28
    print('multiple: ' + str(getsizeof(multiple)))
    multiple *= number % 10  # 28
    print('number: ' + str(getsizeof(number)))
    number //= 10

print(f'Сумма цифр числа = {sum_}')
print(f'Перемножение цифр числа = {multiple}')


print(f'В ходе данного задания было выделено 112 мб памяти под переменные')
# В ходе данного задания было выделено 112 мб памяти под переменные
