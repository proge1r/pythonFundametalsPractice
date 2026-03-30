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
    {"name": "Alice", "position": "Developer", "salary": 5000},
    {"name": "Bob", "position": "Designer", "salary": 4200},
    {"name": "Charlie", "position": "Lead", "salary": 7000}
]


def sort_by_salary(emp_list):
    return sorted(emp_list, key=lambda x: x["salary"])

print(sort_by_salary(employees))


# 9. Використовуючи лямбда-вираз, створіть функцію, яка повертає найбільше з двох чисел.
get_max = lambda a, b: a if a > b else b



print(f"Max value: {get_max(123, 456)}")








