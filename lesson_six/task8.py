from sys import getsizeof

year = int(input('Введите год:\n'))
print(getsizeof(year))
if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print("Обычный")
else:
    print("Високосный")

print()
# В ходе данного задания было выделено 28 мб памяти под переменные
# PS не очень понял смысл задания. Потренироваться с 'getsizeof'?