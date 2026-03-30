d= {}
print(type(d))

d = dict()
d = {"key1":"value",
     "number":12,
     "d":{}}
print(d)


# словарь + цикл
"""
dict:
    .keys() - возаращются ключи
    .values() - возвращаются значения
    .items() - возвращает пары ключ:значение - кортеж(ключ, значение)
"""

print()

for k, v in d.items():
    print(k, v)

print()

for k in d.keys():
    print(k)

print()

for v in d.values():
    print(v)


# # KeyError
# print(d[12]) 
# d["key2"] = "hello"
# print(d)

print(len(d)) # 3

d2 = d.copy()

print(d2)

print(d2.pop("key1"))
print(d2)
print(d2.pop("key1", None))

print(d2.popitem())
print(d2)

d2.update(name="Tom", surname="Due", age=22)

print(d2)

