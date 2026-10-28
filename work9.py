
# size = int(input("Введіть розмір квадрата: "))

# for row in range(size):
#     for col in range(size):
#         print(" * ", end=" ")
#     print()


# print("Меню:")
# print("1 — Квадрат")
# print("2 — Прямокутник")
# print("3 — Трикутник")

# choice = int(input("Виберіть фігуру: "))

# match choice:

#     case 1:
#         size = int(input("Введіть розмір квадрата: "))

#         for row in range(size):
#             for col in range(size):
#                 print(" * ", end=" ")
#             print()

#     case 2:
#         width = int(input("Введіть ширину: "))
#         height = int(input("Введіть висоту: "))

#         for row in range(height):
#             for col in range(width):
#                 print(" * ", end=" ")
#             print()

#     case 3:
#         height = int(input("Введіть висоту трикутника: "))

#         for row in range(1, height + 1):
#             for col in range(row):
#                 print(" * ", end=" ")
#             print()

#     case _:
#         print("Такого пункту меню немає!")



# print("Меню:")
# print("1 — Квадрат")
# print("2 — Прямокутник")
# print("3 — Трикутник")

# choice = int(input("Виберіть фігуру: "))
# symbol = input("Введіть символ: ")

# match choice:

#     case 1:
#         size = int(input("Введіть розмір квадрата: "))

#         for row in range(size):
#             for col in range(size):
#                 print(symbol, end=" ")
#             print()

#     case 2:
#         width = int(input("Введіть ширину: "))
#         height = int(input("Введіть висоту: "))

#         for row in range(height):
#             for col in range(width):
#                 print(symbol, end=" ")
#             print()

#     case 3:
#         height = int(input("Введіть висоту трикутника: "))

#         for row in range(1, height + 1):
#             for col in range(row):
#                 print(symbol, end=" ")
#             print()

#     case _:
#         print("Помилка: такого пункту немає!")



# width = int(input("Введіть ширину: "))
# height = int(input("Введіть висоту: "))
# symbol = input("Введіть символ: ")

# for row in range(height):
#     for col in range(width):

#         if row == 0 or row == height - 1 or col == 0 or col == width - 1:
#             print(symbol, end="  ")
#         else:
#             print(" ", end="  ")

#     print()


# Написати програму, яка виводить на екран шахову дошку із заданим розміром клітинки. Наприклад, три:
# HTML
#  ***---***---***---***---
#  ***---***---***---***---
#  ***---***---***---***---
#  ---***---***---***---***
#  ---***---***---***---***
#  ---***---***---***---***


# size = int(input("Введіть розмір клітинки: "))

# for row in range(8 * size):
#     for col in range(8 * size):

#         if (row // size + col // size) % 2 == 0:
#             print("*", end="  ")
#         else:
#             print("-", end="  ")

#     print()


#     Завдання 2
# Напишіть програму, яка малює драбинку висотою N, де:
# Перший рядок містить числа від 1 до N.
# Другий рядок — від 1 до N-1.
# Третій рядок — від 1 до N-2, і так далі.
# Приклад введення:
# Введіть висоту драбинки: 5.
# Приклад виведення:
 
# HTML
# 1 2 3 4 5
#   1 2 3 4
#     1 2 3
#       1 2
#         1

# height = int(input("Введіть висоту драбинки: "))

# for row in range(height, 0, -1):

#     print("  " * (height - row), end="")

#     for col in range(1, row + 1):
#         print(col, end=" ")

#     print()






# Завдання 3
# Написати програму, яка перевіряє користувача на знання таблиці множення.
# Програма виводить на екран два числа, користувач має ввести їхній добуток. 
# Розробити кілька рівнів складності (відрізняються складністю та кількістю запитань). 
# Вивести користувачеві оцінку його знань.

import random

print(" Таблиця множення ")
print("1 — Легкий рівень: 5 запитань, числа від 1 до 5")
print("2 — Середній рівень: 10 запитань, числа від 1 до 10")
print("3 — Складний рівень: 15 запитань, числа від 1 до 12")

level = int(input("Оберіть рівень: "))

match level:

    case 1:
        questions = 5
        max_number = 5

    case 2:
        questions = 10
        max_number = 10

    case 3:
        questions = 15
        max_number = 12

    case _:
        print("Такого рівня немає!")
        questions = 0


correct = 0

for i in range(questions):

    a = random.randint(1, max_number)
    b = random.randint(1, max_number)

    answer = int(input(f"{a} * {b} = "))

    if answer == a * b:
        print("Правильно!")
        correct += 1
    else:
        print("Неправильно!")
        print("Правильна відповідь:", a * b)


print()
print("Результат:", correct, "правильних відповідей із", questions)

if questions > 0:

    if correct == questions:
        print("Оцінка: 12")

# к-ть правильних відповідей >= 80% від загальної к-ті запитань
    elif correct >= questions * 0.8:
        print("Оцінка: 10")

    elif correct >= questions * 0.6:
        print("Оцінка: 8")

    elif correct >= questions * 0.4:
        print("Оцінка: 6")

    else:
        print("Оцінка: 4")
 

 