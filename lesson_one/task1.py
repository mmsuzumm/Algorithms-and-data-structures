number = int(input('Введите трехзначное число\n'))
i = 0
sum_ = 0
multiple = 1
while i < 3:
    i += 1
    sum_ += number % 10
    multiple *= number % 10
    number //= 10

print(f'Сумма цифр числа = {sum_}')
print(f'Перемножение цифр числа = {multiple}')
