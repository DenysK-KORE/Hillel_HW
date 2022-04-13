# 1.1 list
from distutils.command.install import value

a = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
a = list(set(a))
print("#1.1 Исключить дубликаты:", a)

# 1.2
a.sort()
print("#1.2 Отсортировам list", a)
print("#1.2 Максимальное значиени -1:", a[-1])
print("#1.2 Максимальное значение -2:", a[-2])
print("#1.2 Максимальное значение -3:", a[-3])

# 1.3
b = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
b = list(set(b))
print("#1.3.1 Исключить дубликаты:", b)
print("#1.3 Индекс максимального числа:", b.index(max(b)))
# 1.4
c = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
c = list(set(c))
print("#1.4 Обратная сортировка:", sorted(c, reverse=True))

# 2.0
list_range = list(range(0,100))
print("Массив в диапазоне от 0 до 100", list_range)
ch = [int(i) for i in list_range if i % 2 == 0]
print("#2 Четные числа", ch)

# 3.0
d1 = {"a": 1, "b": 2, "c": 3, "d": 4}
d2 = {"a": 6, "b": 7, "z": 20, "x": 40}
def Common_keys(a, b):
    for i in a.keys():
        for j in b.keys():
            if i == j:
               print("#3 Общий ключ", i)

Common_keys(d1,d2)

# 4.0
keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = {a: a ** 2 for a in keys}
print("#4 Expected result:", d)