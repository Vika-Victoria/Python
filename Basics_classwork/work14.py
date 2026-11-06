# Завдання 1 — Перевірка віку
# def is_adult(age):
# Повертає:
# True
# або:
# False

# def is_adult(age):
#     if age >= 18:
#         return True

#     return False


# age = int(input("Введіть вік: "))

# print(is_adult(age))

# Завдання 2 — Найбільше число
# def get_max(a, b, c):
# Повернути найбільше.

# def get_max(a, b, c):
#     maximum = a

#     if b > maximum:
#         maximum = b

#     if c > maximum:
#         maximum = c

#     return maximum


# a = int(input("Введіть перше число: "))
# b = int(input("Введіть друге число: "))
# c = int(input("Введіть третє число: "))

# print(get_max(a, b, c))

# Завдання 3 — RPG Battle
# Є два персонажі.
# Створити:
# def calculate_damage(attack, armor):
# Формула:
# damage = attack - armor
# Але damage не може бути меншим за 0.
# Наприклад: damage = calculate_damage(50, 20)
 
# print(damage) Результат:30

# def calculate_damage(attack, armor):
#     damage = attack - armor

#     if damage < 0:
#         damage = 0

#     return damage


# damage = calculate_damage(50, 20)

# print(damage)


# Завдання 4. Функція отримує список оцінок студента та повинна повернути:
# мінімальну оцінку;
# максимальну оцінку;
# середню оцінку.

# import random


# def get_statistics(grades):
#     minimum = grades[0]
#     maximum = grades[0]
#     total = 0

#     for grade in grades:
#         if grade < minimum:
#             minimum = grade

#         if grade > maximum:
#             maximum = grade

#         total += grade

#     average = total / len(grades)

#     return minimum, maximum, average


# grades = [random.randint(1, 12) for i in range(6)]

# minimum, maximum, average = get_statistics(grades)

# print("Оцінки:", grades)
# print("Мінімальна оцінка:", minimum)
# print("Максимальна оцінка:", maximum)
# print("Середня оцінка:", average)


# Створіть програму для бронювання квитків у кінотеатрі.
# Створіть глобальну змінну available_seats = 20 — кількість вільних місць.
# Створіть функцію book_tickets(count), яка бронює вказану кількість місць та зменшує available_seats.
# Усередині функції використайте локальну змінну price = 150 — вартість одного квитка.
# Обчисліть загальну вартість бронювання в локальній змінній total_price.
# Якщо місць недостатньо — виведіть відповідне повідомлення.
# Створіть функцію show_seats(), яка показує кількість вільних місць.
# Для зміни глобальної змінної використайте global


available_seats = 20


def book_tickets(count):
    global available_seats

    price = 150

    if count <= available_seats:
        available_seats -= count

        total_price = count * price

        print("Квитки успішно заброньовано!")
        print("Кількість квитків:", count)
        print("Загальна вартість:", total_price, "грн")
    else:
        print("Недостатньо вільних місць!")


def show_seats():
    print("Вільних місць:", available_seats)


show_seats()

count = int(input("Скільки квитків забронювати? "))
book_tickets(count)

show_seats()