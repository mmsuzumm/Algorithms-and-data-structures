#Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a, b, c = map(float, input('введите 3 числа через пробел\n').strip().split())

abc_lst = [a, b, c]
abc_lst.sort()
print(f'Среднее число это {abc_lst[1]}')
#
# if a>b>c:
# 	print(f'Среднее число = {b}')
# elif c>b>a:
# 	print(f'Среднее число = {b}')
#
#
# elif b>a>c:
# 	print(f'Среднее число = {a}')
# elif c>a>b:
# 	print(f'Среднее число = {a}')
#
#
# elif a>c>b:
# 	print(f'Среднее число = {c}')
# else:
# 	print(f'Среднее число = {c}')