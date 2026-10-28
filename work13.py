# Напишіть функцію, яка відображає на екран форматований текст, зазначений нижче:
# Plain Text
# "Don't let the noise of others' opinions 
#     drown out your own inner voice."Steve Jobs

# def print_quote():
#     print('"Don\'t let the noise of others\' opinions')
#     print('    drown out your own inner voice."')
#     print('Steve Jobs')


# print_quote()

# def check_age(name, age):
#     if age >= 18:
#         print(f"{name} повнолітня")
#     else:
#         print(f"{name} неповнолітня")


# age = int(input("Введіть вік: "))

# check_age("Vika", age)

# функція калькулятор
# def calculator(number1, number2, operation):
#     if operation == "+":
#         print(number1 + number2)
#     elif operation == "-":
#         print(number1 - number2)
#     elif operation == "*":
#         print(number1 * number2)
#     elif operation == "/":
#         print(number1 / number2)


# number1 = int(input("Введіть перше число: "))
# number2 = int(input("Введіть друге число: "))
# operation = input("Введіть операцію (+, -, *, /): ")

# calculator(number1, number2, operation)

# Завдання 2
# Напишіть функцію, яка приймає два числа як параметр і відображає всі непарні числа між ними.

# def show_odd_numbers(number1, number2):
#     for number in range(number1, number2 + 1):
#         if number % 2 != 0:
#             print(number)


# number1 = int(input("Введіть перше число: "))
# number2 = int(input("Введіть друге число: "))

# show_odd_numbers(number1, number2)


# Завдання 3
# Напишіть функцію, яка відображає горизонтальну або вертикальну лінію з деякого символу. 
# Функція приймає як параметр: довжину лінії, напрямок, символ.

# def draw_line(length, direction, symbol):
#     if direction == "horizontal":
#         print(symbol * length)
#     elif direction == "vertical":
#         for i in range(length):
#             print(symbol)


# length = int(input("Введіть довжину лінії: "))
# direction = input("Введіть напрямок (horizontal/vertical): ")
# symbol = input("Введіть символ: ")

# draw_line(length, direction, symbol)


# Завдання 4
# Напишіть функцію, яка відображає максимальне з чотирьох чисел. Числа передаються як параметри.

# def find_max(number1, number2, number3, number4):
#     maximum = number1

#     if number2 > maximum:
#         maximum = number2

#     if number3 > maximum:
#         maximum = number3

#     if number4 > maximum:
#         maximum = number4

#     print("Максимальне число:", maximum)


# number1 = int(input("Введіть перше число: "))
# number2 = int(input("Введіть друге число: "))
# number3 = int(input("Введіть третє число: "))
# number4 = int(input("Введіть четверте число: "))

# find_max(number1, number2, number3, number4)

# Завдання 5
# Напишіть функцію, яка перевіряє чи є число простим. Число передається як параметр. Якщо число просте потрібно повернути  true, інакше false.

# def is_prime(number):
#     if number < 2:
#         return False

#     for i in range(2, number):
#         if number % i == 0:
#             return False

#     return True


# number = int(input("Введіть число: "))

# print(is_prime(number))


# Завдання 6
# Напишіть функцію, яка перевіряє, чи є шестизначне число "щасливим". 
# Число передається як параметр. Якщо число щасливе потрібно повернути з функції true, інакше false.
# "Щасливе шестизначне число " — це число, у якого сума перших трьох цифр дорівнює сумі трьох других цифр.
# Наприклад, 123420 — щасливе 1+2+3 = 4+2+0, а 723422 — нещасливе 7+2+3 != 4+2+2.

# def is_lucky(number):
#     if number < 100000 or number > 999999:
#         return False

#     digit1 = number // 100000
#     digit2 = number // 10000 % 10
#     digit3 = number // 1000 % 10

#     digit4 = number // 100 % 10
#     digit5 = number // 10 % 10
#     digit6 = number % 10

#     sum1 = digit1 + digit2 + digit3
#     sum2 = digit4 + digit5 + digit6

#     if sum1 == sum2:
#         return True
#     else:
#         return False


# number = int(input("Введіть шестизначне число: "))

# print(is_lucky(number))


# Завдання 7
# Напишіть функцію, яка повертає добуток чисел у вказаному діапазоні. Межі діапазону передаються як параметри.
#  Якщо межі діапазону переплутані (наприклад, 5 — верхня межа, 25 — нижня межа), їх потрібно поміняти місцями.

# def multiply_range(number1, number2):
#     if number1 > number2:
#         number1, number2 = number2, number1

#     result = 1

#     for number in range(number1, number2 + 1):
#         result *= number

#     return result


# number1 = int(input("Введіть першу межу: "))
# number2 = int(input("Введіть другу межу: "))

# print("Добуток:", multiply_range(number1, number2))


# Завдання 8
# Напишіть функцію для знаходження максимуму в списку цілих. Список передається як параметр.

# import random


# def find_max(numbers):
#     maximum = numbers[0]

#     for number in numbers:
#         if number > maximum:
#             maximum = number

#     return maximum


# numbers = [random.randint(1, 100) for i in range(10)]

# print("Список:", numbers)
# print("Максимальне число:", find_max(numbers))



# Завдання 9
# Напишіть функцію, що обчислює суму елементів списку цілих. Список передається як параметр.

# import random


# def sum_numbers(numbers):
#     total = 0

#     for number in numbers:
#         total += number

#     return total


# numbers = [random.randint(1, 100) for i in range(10)]

# print("Список:", numbers)
# print("Сума елементів:", sum_numbers(numbers))