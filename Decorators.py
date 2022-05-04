# ЗАДАЧА-1
# Написать свой декоратор который будет проверять остаток
# от деления числа 100 на результат работы функции.

# def integer_remainder(f):
#     def wrapper(r):
#         if 100 % f == 0:
#             print('----------------')
#             f(r)
#             print('----------------')
#         else:
#             print('Some text')
#     return wrapper
#
# @integer_remainder
# def func_1(numb):
#     r = numb * 100
#     return print('Result:', r)
#
# f = func_1()

# Если остаток от деления = 0, вывести сообщение "We are OK!», иначе «Bad news guys, we got {}» остаток от деления.








# ЗАДАЧА-2
# Написать декоратор который будет выполнять предпроверку типа аргумента который передается в вашу функцию.
# Если это int, тогда выполнить функцию и вывести результат, если это str(),
# тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))

# Пример рейза ошибок:
# try:
#   f()
# except ValueError:
#   raise ValueError(“string type is not supported”)

# *ЗАДАЧА-3
# Написать декоратор который будет кешировать значения аргументов и результаты работы вашей функции и записывать
# его в переменную cache. Если аргумента нет в переменной cache и функция выполняется, вывести сообщение
# «Function executed with counter = {}, function result = {}» и количество раз сколько эта функция выполнялась.
# Если значение берется из переменной cache, вывести сообщение «Used cache with counter = {}» и
# количество раз обращений в cache.