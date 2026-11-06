# Завдання 1
# Користувач з клавіатури вводить список цілих чисел. Необхідно порахувати, скільки у списку парних і непарних чисел. Результати вивести на екран.

# numbers = []

# while True:
#     number = int(input("Введіть число (0 — завершити): "))

#     if number == 0:
#         break

#     numbers.append(number)

# even_number = 0    
# odd_number = 0

# for number in numbers:
#     if number % 2 == 0:
#         even_number += 1
#     else:
#         odd_number += 1

# print("Парних чисел: ", even_number)
# print("Не парних чисел: ", odd_number)            

# Завдання 2
# Користувач із клавіатури вводить список цілих чисел. Необхідно визначити максимальне і мінімальне значення у списку. Результати вивести на екран.

# numbers = []

# while True:
#     number = int(input("Введіть число (0 — завершити): "))

#     if number == 0:
#             break

#     numbers.append(number)    

# max_val = numbers[0]
# min_val = numbers[0]

# for number in numbers:
#     if number > max_val:
#         max_val = num
#     if number < min_val:
#         min_val = num

# print("Максимальне значення:", max_val)
# print("Мінімальне значення:", min_val)

# Завдання 3
# У списку цілих, заповненому випадковими числами, визначити мінімальний, додатний елемент і максимальний,
# від'ємний елемент, порахувати кількість від'ємних елементів, порахувати кількість додатних елементів, порахувати кількість нулів.
# Результати вивести на екран.

# import random

# numbers = []

# for i in range(10):
#     number = random.randint(-10, 10)

#     numbers.append(number)

# min_positive = 0
# max_negative = 0
# count_negative = 0
# count_positive = 0
# count_zero = 0

# for number in numbers:
#     if number > 0:
#         count_positive += 1

#         if min_positive == 0 or number < min_positive:
#             min_positive = number

#     elif number < 0:
#         count_negative += 1

#         if max_negative == 0 or number > max_negative:
#             max_negative = number

#     else:
#         count_zero += 1

# print("Список:", numbers)
# print("Мінімальний додатний елемент:", min_positive)
# print("Максимальний від'ємний елемент:", max_negative)
# print("Кількість від'ємних елементів:", count_negative)
# print("Кількість додатних елементів:", count_positive)
# print("Кількість нулів:", count_zero)                       

# Завдання 4
# Користувач із клавіатури вводить список цілих чисел і деяке число. 
# Необхідно видалити зі списку всі елементи, які менші за задане число. Результат вивести на екран.

# numbers = []

# while True:
#     number = int(input("Введіть число (0 — завершити): "))

#     if number == 0:
#         break

#     numbers.append(number)

# limit = int(input("Введіть число для порівняння: ")) 

# new_numbers = []

# for number in numbers:
#     if number >= limit:
#         new_numbers.append(number)

# print("Початковий список:", numbers)
# print("Результат:", new_numbers)

# Завдання 5
# Користувач вводить з клавіатури арифметичний вираз. Наприклад, 23+12.
# Необхідно вивести на екран результат виразу. У нашому прикладі це 35. 
# Арифметичний вираз може складатися тільки з трьох частин: число, операція, число. Можливі операції: +, -, *, /.

# expression = input("Введіть арифметичний вираз: ")

# if "+" in expression:
#     parts = expression.split("+") # split() — розділяє один рядок на частини і повертає список.
#     number1 = int(parts[0])
#     number2 = int(parts[1])
#     result = number1 + number2

# elif "-" in expression:
#     parts = expression.split("-")
#     number1 = int(parts[0])
#     number2 = int(parts[1])
#     result = number1 - number2

# elif "*" in expression:
#     parts = expression.split("*")
#     number1 = int(parts[0])
#     number2 = int(parts[1])
#     result = number1 * number2

# elif "/" in expression:
#     parts = expression.split("/")
#     number1 = int(parts[0])
#     number2 = int(parts[1])
#     result = number1 / number2

# print("Результат:", result)



# Завдання 6
# Користувач із клавіатури вводить список цілих чисел. Необхідно відсортувати цей список так, щоб від'ємні числа залишилися на своїх місцях,
# а решта елементів були відсортовані за зростанням. Результат вивести на екран.

numbers = []

while True:
    number = int(input("Введіть число (0 — завершити): "))

    if number == 0:
        break

    numbers.append(number)

positive_numbers = []

for number in numbers:
    if number >= 0:
        positive_numbers.append(number)

positive_numbers.sort()

index = 0

for num in range(len(numbers)):
    if numbers[num] >= 0:
        numbers[num] = positive_numbers[index]
        index += 1

print("Результат:", numbers)