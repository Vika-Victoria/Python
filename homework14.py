# ## Завдання 1. Розрахунок замовлення
# Створіть функцію: calculate_order(price, quantity)
# Функція повинна приймати ціну одного товару та кількість товарів і за допомогою `return` повертати загальну вартість.

# Приклад:
# result = calculate_order(250, 3)
# print(result)
# Результат:
# 750

# def calculate_order(price, quantity):

#     if price <= 0 or quantity <= 0:
#         raise "Ціна і кількість товару не може бути менше нуля!"

#     result = price * quantity

#     return result


# price = int(input("Введіть ціну одного товару: "))
# quantity = int(input("Введіть загальну кількість товарів:"))

# print("Загальна вартість товарів: ", calculate_order(price, quantity))


## Завдання 2. Перевірка віку
# Створіть функцію:check_age(age)
# Функція повинна за допомогою `return` повертати:
# - `"Доступ дозволено"`, якщо користувачу 18 років або більше;
# - `"Доступ заборонено"`, якщо менше 18.
# Викличте функцію для декількох різних значень.

# def check_age(age): 

#     if age >= 18:
#         return "Доступ дозволено"

#     return  "Доступ заборонено"

# print(check_age(25))
# print(check_age(17))
# print(check_age(18))
# print(check_age(10)) 


# Завдання 3. Калькулятор зі значенням за замовчуванням
# Створіть функцію: calculate(a, b, operation="+")`
# Функція повинна підтримувати операції:+  - * / та повертати результат через `return`.
# Якщо третій аргумент не переданий: calculate(10, 5) функція повинна виконати додавання. Передбачте ділення на нуль.

# def calculate(a, b, operation="+"):

#     match operation:
#         case "-":
#             return a - b

#         case "*":
#             return a * b

#         case "/":
#             if b == 0:
#                 raise ValueError("На 0 ділити не можна!")
#             else:
#                 return a / b

#         case "+":
#             return a + b

#         case _:
#             print("Невірний вибір операції!")


# a = int(input("Введіть перше число: "))
# b = int(input("Введіть друге число: "))
# operation = input("Введіть операцію (*, /, +, -): ")

# try:
#     if operation == "":
#         result = calculate(a, b)
#     else:
#         result = calculate(a, b, operation)
    
#     print(f"Результат: {result}")

# except ValueError as e:
#     print(f"Помилка: {e}")



## Завдання 4. Локальні та глобальні змінні
# Створіть глобальну змінну: total_students = 0
# Створіть функцію:register_student(name)
# При кожному виклику функції збільшуйте `total_students` на `1`.
# Для зміни глобальної змінної використайте:  global total_students
# Усередині функції створіть локальну змінну: message = ... , яка міститиме повідомлення: Студента Anna зареєстровано
# Функція повинна повертати `message` через `return`.
# Створіть також функцію:show_students_count(),  яка повертає загальну кількість зареєстрованих студентів.     

# total_students = 0


# def register_student(name):

#     global total_students

#     if name == "":
#         return "Ім'я не може бути порожнім"

#     if len(name) < 2:
#         return "Ім'я повинно містити мінімум 2 символи"

#     total_students += 1

#     message = "Студента " + name + " зареєстровано"

#     return message


# def show_students_count():
#     return total_students


# while True:
#     name = input("Введіть ім'я студента (0 — завершити): ")

#     if name == "0":
#         break

#     print(register_student(name))
#     print("Загальна кількість зареєстрованих студентів:", show_students_count())


#  Завдання 5. Функція з різною кількістю аргументів
# Створіть функцію: average(*numbers)
# Функція повинна приймати будь-яку кількість чисел та повертати їх середнє арифметичне.
# Наприклад: print(average(10, 8, 12))
# print(average(5, 10, 15, 20, 25))
# Не використовуйте готову функцію для обчислення середнього значення.
# Передбачте ситуацію, коли жодного числа не передано.

# def average(*numbers):
#     if len(numbers) == 0:
#         raise ValueError("Не передано жодного числа")

#     total = 0

#     for number in numbers:
#         total += number

#     return total / len(numbers)


# num_all = []

# while True:
#     try:
#         number = int(input("Введіть число (0 — завершити): "))

#         if number == 0:
#             break

#         num_all.append(number)

#     except ValueError:
#         print("Потрібно ввести ціле число!")


# try:
#     print("Середнє арифметичне:", average(*num_all))
# except ValueError as e:
#     print(e)


# Завдання із зірочкою ⭐
# Створіть функцію:create_profile(name, age, city="Kyiv", *skills)
# Функція отримує:
# - `name` — ім'я;
# - `age` — вік;
# - `city` — місто зі значенням за замовчуванням `"Kyiv"`;
# - `*skills` — будь-яку кількість навичок.
# Функція повинна сформувати та **повернути через `return`** інформацію про користувача.
# Наприклад:
# profile = create_profile("Alex", 19,"Lviv","Python",HTML", "Git")
# print(profile)
# У домашній роботі повинні бути використані:
# - функції;- параметри;- позиційні аргументи;- аргумент зі значенням за замовчуванням;- `*args`;
# - `return`;- локальна змінна;- глобальна змінна;- `global`;- виклики функцій з різними аргументами.



total_profiles = 0

def create_profile(name, age, city = "Kyiv", *skills):
    global total_profiles

    total_profiles += 1

    message = "Ім'я: " + name + "\n"
    message += "Вік: " + str(age) + "\n"
    message += "Місто: " + city + "\n"
    message += "Навички: " + ", ".join(skills)

    return message


name = input("Введіть ім'я: ")
age = int(input("Введіть вік: "))

city = input("Введіть місто (Enter — Kyiv): ")

if city == "":
    city = "Kyiv"

skills = []

while True:
    skill = input("Введіть навичку (0 — завершити): ")

    if skill == "0":
        break

    skills.append(skill)


profile = create_profile(name, age, city, *skills)

print()
print(profile)

print()
print("Кількість створених профілів:", total_profiles)
