# 1 task
import random
from itertools import groupby


consonants = 'bcdfghjklrmnpstvwxyz '
vowels = 'aeiou'

def replace_elements(s):
    for elem in s:
        if elem.lower() in consonants:
             s = s.replace(elem, random.choice(vowels))
    return s

s = replace_elements('hkgctgb6um8ioptculjkbkjhiuh')
print(s)

# 2.1 sorted task

data = [
  {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
  {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
  {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
  {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
  {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
  {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

new_dict = sorted(data, key = lambda k:k['age'])
print(new_dict)

# 2.2 groupby task

data = sorted(data, key = lambda k:k['city'])

for k, v in groupby(data, key = lambda k:k['city']):
    print(k , ':')
    print(list(v))

# 3 most_frequent

s = ['asas', 'asas', 'asas', 'asas', 'asassasas', 'asassasas', 'asassasas', 'ss', 'ss']
ss = (['a', 'a', 'bi', 'bi', 'bi'])
def most_frequent(a):
    di = {}
    for word in a:
        if word in di.keys():
            di[word] += 1
        else:
            di[word] = 1
    key = max(di, key=di.get)
    print(key, di[key])

most_frequent(ss)




