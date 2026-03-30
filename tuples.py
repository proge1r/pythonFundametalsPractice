# Immutable VS mutable

# Immutable - неизмененный тип
"""
int
bool
float
str
tuple
"""
num = 4
print(type(num)) 

# Python выделяет область памяти для значения 10 в heap, которое находится в num
num = 10 
# значение num со значением 10 не перезаписывается , а ссылается на новую
# область в памяти со значением 20.
num += 10 
print(num)

# str неизминяемый (Immutable) 
st = 'HELLO'
print(st[1])
# st[1]='B'

# mutable
l1 = list("HELLO")
print(l1[1])
l1[1]='B'
print(l1)

# списки в Python не имеют реальных объектов, вместо них набор ссылок
# на конкретные объекты

# tuple (кортеж) - неизменная коллекция элементов, которая неизменяема.
# То есть, данные в полной безопасности будут неизменными
t = tuple([1,2,3,4,5])
print(t)
t1 = (1, )
print(t1)

print(len(t))  # 5
print(t[1]) 
print(t[-1])
print(t[:3])

for i in t:
    print(i)

print(t.index(3))
print()
print(t.count(5))

def sample():
    num = 5
    return (1,2,3, num)

# mistake
# (num,...) = sample()

# print(num)


a =5
b =12
print(f"{a}  {b}")
(a, b) = (b, a)
print(f"{a} -> {b}")









