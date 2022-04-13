# Есть список
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# 1.1) Выведите элемент коллекции с индексом 4
print('Эдемень с индексом 4 =', a[4])

# 1.2) Добавить число 10 в конец списка

a.append(10)
print('Добавленное число 10 в конец списка:',a)
# 1.3) Удалить элемент из списка под индексом 10

a.remove(10)
print('Удаление элемента с индексом 10 из списка:', a)

# 1.4) Выведите все элементы, которые меньше 5.

b = [1, 1, 2, 3, 5, 8, 3, 2.1, 3.4, 0, 89]

def elem_less_5(x):
    res = []
    for elem in x:
        if elem < 5:
            res.append(elem)
    print('Числа меньше 5 записаны res =', res)

elem_less_5(b)


# 1.5) Выведите первый и последний элемент списка.

print('Первый элемент:', a[0], 'Последний элемент:', a[-1])

# 1.6) Выведите чётные числа из заданного списка
ch = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
ch1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def ch_in_list(x):
    r = []
    for elem in x:
       if elem % 2 == 0:
            r.append(elem)
    return print('Четные числа из:', x, 'Сохранены в:', r)

r1 = ch_in_list(ch)
r2 = ch_in_list(ch1)

# 1.7) Объеденить 2 списка в один список

res = ch + ch1

print('Сложение слвоарей:', res)

ch.extend(ch1)
print('Объединили 2 списка:', ch)


# 1.8) Нужно вернуть список, который состоит из элементов, общих для этих двух списков.

def common_element(a,b):
    c = []
    for i in a:
        if i in c:
            continue
        for j in b:
            if i == j:
                c.append(i)
    return c


ce = common_element(ch, ch1)
print('Общие элементы из двух списков:', ce)
# dict

# Создать словарь который содержит имена и возраст пользователей.
# (напр. {'name': 'Vasia', 'age': 30})

some_piople = [{'name': 'Vasia', 'age': 25},
               {'name': 'Dima', 'age': 17},
               {'name': 'Oleg', 'age': 37},
               {'name': 'Stas', 'age': 34},
               {'name': 'Vasilisa', 'age': 31}]

# 2.1) Добавить к существующему словрю еще одно имя.
some_piople.append({'name': 'Anna', 'age': 23})
print('Добавленное значение:', some_piople)

# 2.2) Удалить пользователя из словаря с конкретным именем(напр. "Vasia")
some_piople.pop(0)
print('Удалил нулевой элемент:', some_piople)

# 2.3) Отсортировать словарь по значению age
def get_age(some_piople):
    return some_piople.get('age')

some_piople.sort(key=get_age)
print('Отсортированные имена по возрасту:', some_piople)

# set

# Создать 2 сета
# 3.1) найти общие елементы у двух сетов

s1 = [10, 20, 30, 40, 100, 11]
s2 = [1, 3, 55, 10, 40, 65, 11, 15]

res_common = common_element(s1, s2)
print('Общие элементы:', res_common)


# 3.2) найти разницу между двумя сетами
dif1= set(s1).difference(s2)
dif2= set(s2).difference(s1)
print('Разница между s1 и s2:', dif1)
print('Разница между s2 и s1:', dif2)

# 3.3) добавить значение в сет

s1.append(13)
print('Добавлено значение 13 в:', s1)

# 3.4) удалить значение из сета

s2.remove(65)
print('Удалено значение 65 из:', s2)

# str
# создать строку
# 4.1) получить первый элемент строки
str1 = 'Это строка для задания 4.1'
print('Первый элемент строки:', str1[0])

# 4.2) получить последний элемент строки

print('Последний элемент строки:', str1[-1])

# 4.3) получить 5-й элемент строки

print('Пятый элемент строки:', str1[4])

# 4.4) добавить символ к строке

res_str = str1 + ' -последний элемент-'
print('Добавлен текст в конец строки str1:', res_str)

# 4.5) заменить все пробелы в строке на '_'

space = ' '

def replace_elements1(s):
    for elem in s:
        if elem.lower() in space:
             s = s.replace(elem, '_')
    return s

res_repl = replace_elements1(res_str)
print('Заменены space на _ :', res_repl)

# 4.6) есть лист ['h', 'e', 'l', 'l', 'o']. Преобразовать его в строку 'hello'

simple_list = ['h', 'e', 'l', 'l', 'o']

print('Преобразование в строку:', "".join(simple_list))

# 4.7) поработать с форматом строки. Например:
# name = 'Vasia'
# "Hello {} world".format(name) или тоже самое но более нового вида формат
# f"Hello {name} world"

name = 'Vasia'
age = 34
d = 10

print(f'{name} age is {age} and d={d}')

first_name = "John"
last_name = "Doe"
print("Hello {} {}, hope you're well!".format(first_name, last_name))