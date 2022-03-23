"""
# changeable data type
list()
dict()
set()

# unchangeable
int()
str()
tuple()
"""

# list
a = [1, 2, 3, 4]
print(a[0])

a.append(100)
print(a)
a.remove(3)
print(a)

# dict()
d = {"firstName" : "Denys", "age" : 34}
d["adress"] = "Kharkov"
print(d)
print(d["age"])

# set()
s = {1, 2, 3, 4, 5}
print(s)
s.add(10)
print(s)
c = [1, 2, 3, 3, 4, 4, 5]
print(list(set(c)))

# int()
x = 2
y = 2
x: int = 2
print(x+y)

# str()
st = 'text'
print(st[1])

# tuple()
b = (1, 2, 3, 4)
print(b)