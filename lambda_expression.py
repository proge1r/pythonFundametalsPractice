#lambda - анонимная функция, которая быстро создается с помощью
# ключевого слова lambda

def sample():
    print("This is a sample function")
    print("Use it")

sample()

 # lambda params: expression

greeting = lambda user:print(f"Hello, {user}")
greeting("Danya")

def operations(val1, val2, operation):
    print(operation(val1, val2))

operations(12, 13, lambda x,y: x+y)
operations(25, 10, lambda x,y: x-y)
operations(2, 3, lambda x,y: x**y)

import random as rnd

# создает 10 рандомных элементов
l = [rnd.randrange(50) for i in range(10)]
print(l)

l.sort(key = lambda x: x%2==0)
print(l)

l2 = l.copy()

print(list(map(lambda x: x**2, l2)))

print(list(filter(lambda x: x<=10, l)))

