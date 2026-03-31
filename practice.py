num = 12345

# 1. Створіть функцію, яка підраховує кількість цифр у числі
def countNums(num):
    print(len(str(num)))

countNums(num)

# 2. Користувач вводить рядок, необхідно отримати кількість повторень
# кожного слова в рядку. Ігноруємо коми, крапки.
#    Вивід:
#    слово: кількість
#    і т.д.

def countSameWords():
    user_input = input("Enter the row: ")
    
    words = user_input.replace(".", "").replace(",", "").split()

    counts = {}
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

    for word, count in counts.items():
        print(f"{word}: {count}")

countSameWords()


# 3. Створити список із цілих чисел. Його необхідно відфільтрувати, щоб у результаті залишилися парні числа. 
# Вивести квадрати цих чисел, використовуючи map.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
squares = list(map(lambda x: x**2, even_numbers))
print(f"Squares of even numbers: {squares}")


# 4. Створіть словник, у якому кожна пара — це студент і список його оцінок
# * Вивести по кожному студенту середній бал
# * Вивести студента з максимальною оцінкою


students = {
    "Danya": [12, 10, 11, 12],
    "Robert": [8, 9, 7, 10],
    "Martin": [11, 12, 10, 9]
}

for student, grades in students.items():
    avg = sum(grades) / len(grades)
    print(f"{student} average score: {avg}")

best_student = ""

max_grade = 0
for student, grades in students.items():
    current_max = max(grades)

    if current_max > max_grade:
        max_grade = current_max
        best_student = student
print(f"Top student is {best_student} with grade: {max_grade}")


# 5. Напишіть функцію, яка приймає рядок і повертає словник, де ключ — це символ рядка, 
# а значення — кількість його повторень.
def count_char_frequency(text):
    char_map = {}
    for char in text:
        char_map[char] = char_map.get(char, 0) + 1
    return char_map

print(count_char_frequency("hello world"))


# 6. Створіть кортеж із кількох рядків і чисел. Напишіть функцію, яка повертає новий кортеж, 
# що містить лише числа.

def extract_numbers(data_tuple):
    return tuple(item for item in data_tuple if isinstance(item, (int, float)))

mixed_data = ("Python", 19, "VS Code", 3.14, 2026, "Gemini")
print(extract_numbers(mixed_data))


# 7. Напишіть функцію, яка приймає список рядків і повертає список, у якому рядки відсортовані за довжиною.
def sort_strings_by_len(list_of_strings):
    return sorted(list_of_strings, key=len)

test_strings = ["programming", "it", "code", "python", "dev"]
print(sort_strings_by_len(test_strings))


# 8. Створіть словник із даними про співробітників компанії (ім’я, посада, зарплата). 
# Напишіть функцію, яка сортує співробітників за зарплатою.

employees = [
    {"name": "David", "position": "Developer", "salary": 5000},
    {"name": "Martin", "position": "Designer", "salary": 4200},
    {"name": "Ilon", "position": "Lead", "salary": 7000}
]


def sort_by_salary(emp_list):
    return sorted(emp_list, key=lambda x: x["salary"])

print(sort_by_salary(employees))


# 9. Використовуючи лямбда-вираз, створіть функцію, яка повертає найбільше з двох чисел.
get_max = lambda a, b: a if a > b else b

print(f"Max value: {get_max(123, 456)}")


# 10. Напишіть функцію, яка знаходить усі унікальні елементи в списку і повертає їх у вигляді множини.

l1 =  [1,1,2,3,3]


def uniqueSet(list):
    unique_set = set()
    print(list)

    for n in list:
        print(n)
        unique_set.add(n)
    print(unique_set)

uniqueSet(l1)

# 11. Створіть словник, де ключі — це числа від 1 до 10, а значення — їхні квадрати. Напишіть функцію, яка знаходить суму всіх значень у словнику.

def printSquaredValuesFromDictionary():
    d = {}
    for i in range(1 , 11):
        d[i] = i**2
    return d

dict1 = printSquaredValuesFromDictionary()
print(dict1)

def sumDict(dict):
    sum = 0

    for v in dict.values():
        sum += v
    
    return sum

dict1_sum = sumDict(dict1)
print(dict1_sum)


# 12. Напишіть функцію, яка приймає список чисел і повертає новий список, що містить лише ті числа, які більші за 10 і парні.

def filterEvenAboveTen(list):
    l_result = []
    for n in list:
        if n > 10  and n%2==0:
            l_result.append(n)
    return l_result

l2 = [1,4, 15, 16, 888]
filtered_list = filterEvenAboveTen(l2)
print(filtered_list)



# 13. Створіть кортеж із кількох чисел. Напишіть функцію, яка знаходить суму всіх чисел у кортежі.
def tupleSum(tuple):
    tuple_sum = 0
    for n in tuple:
        tuple_sum += n

    return tuple_sum


tuple1 = (3, 10, 987)
print(tupleSum(tuple1))

# 14. Напишіть лямбда-функцію, яка перевіряє, чи є число додатним.

isPosisitve = lambda x: True if x > 0 else False
print(isPosisitve(-5))
print(isPosisitve(5))

# 15. Створіть словник, у якому зберігаються імена людей і їхній вік. 
# Напишіть функцію, яка приймає вік і повертає список імен людей, старших за цей вік.

people = {
    "Danya": 19,
    "David": 21,
    "Ilon": 18,
    "Niccolo": 25
}

def get_older_people(people_dict, min_age):
    older_names = []
    for name, age in people_dict.items():
        if age > min_age:
            older_names.append(name)
    return older_names

print(get_older_people(people, 20))


# 16. Створіть кортеж із чисел і напишіть функцію, яка знаходить найбільше і найменше значення в кортежі.
numbers_tuple = (45, 12, 88, 3, 199, 10)

def find_min_max(tup):
    maximum = max(tup)
    minimum = min(tup)
    return maximum, minimum

max_val, min_val = find_min_max(numbers_tuple)
print(f"Max: {max_val}, Min: {min_val}")


# 17. Використовуючи лямбда-вираз і функцію filter, знайдіть усі числа, які діляться на 3, у списку чисел.
nums_list = [1, 3, 5, 9, 12, 15, 20, 21]

divisible_by_three = list(filter(lambda x: x % 3 == 0, nums_list))
print(divisible_by_three)


# 18. Напишіть функцію, яка перетворює рядок у список кортежів, де кожен кортеж містить символ і його індекс у рядку.

def string_to_indexed_tuples(text):
    result = []
    for index, char in enumerate(text):
        result.append((char, index))
    return result

print(string_to_indexed_tuples("Python"))


# 19. Напишіть генератор, який буде генерувати числа, що діляться на 3 або 5, починаючи з 1 і до заданої межі.
def div_3_or_5_generator(limit):
    for i in range(1, limit + 1):
        if i % 3 == 0 or i % 5 == 0:
            yield i

for num in div_3_or_5_generator(20):
    print(f"Generated: {num}")


# 20. Напишіть замикання, яке дозволяє викликати передану функцію не більше ніж **n** разів. 
# Після перевищення ліміту має повертатися повідомлення.
def limit_calls(func, n):
    calls = 0
    def wrapper(*args, **kwargs):
        nonlocal calls
        if calls < n:
            calls += 1
            return func(*args, **kwargs)
        else:
            return "Error: Call limit exceeded"
    return wrapper

def say_hello():
    return "Hello!"

limited_hello = limit_calls(say_hello, 2)
print(limited_hello()) # 1
print(limited_hello()) # 2
print(limited_hello()) # Error


# 21. Створіть замикання, яке приймає список чисел і повертає функцію, 
# що перевіряє, чи належить число цьому списку.
def create_membership_checker(num_list):
    search_set = set(num_list)
    def checker(n):
        return n in search_set
    return checker

is_in_list = create_membership_checker([1, 2, 3, 5, 8])
print(f"Is 5 in list? {is_in_list(5)}")
print(f"Is 10 in list? {is_in_list(10)}")


# 22. Напишіть замикання, яке приймає шаблон рядка і повертає функцію, що форматує рядок за цим шаблоном.
def create_formatter(template):
    def formatter(name):
        return template.format(name)
    return formatter

welcome_msg = create_formatter("Welcome, {}! Happy coding!")
log_msg = create_formatter("[LOG]: User {} has logged in")

print(welcome_msg("Danya"))
print(log_msg("Niccolo Machiavelli"))





