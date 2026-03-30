
# Список - структуированый тип
# Список - это коллекция ссылок

l = [1,2,3,4,5]
print(l)

l2 = list("HelLo")
print(l2)

print(len(l2))

print(l2[0]) # H

print(l2[-2]) # L

# [start:stop:step]

l3 = [i for i in range(1,100)]
print(l3)


# print(l3[0:10]). Срезы
print(l3[0:11])
print(l3[:10]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(l3[::-1])

for i in l2:
    print(i)

l2.append("Hello")
l2.append(12)
print(l2)

# reverse() - переворачивает список
l2.reverse()
print(l2)


l2.extend("world")
print(l2)

print(l2.pop())
print(l2)

# вставка по индексу
l2.insert(-1, "Last")
print(l2)

# узнает индекс элемента
print(l2.index("Last"))

print(l2.count('l'))

newList = l2.copy()
l2.append("newItem")
print(newList)

# очищает список
newList.clear()
print(newList)

# удаление элемента из списка
l2.remove(12)
print(l2)



















