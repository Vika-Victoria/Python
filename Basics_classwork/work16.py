# def simpleDecorator(function):
#     print("hello, i am decorator")

#     def wrapper():
#         print("funk start")
#         function()
#         print("func end")

#         return wrapper()

# @simpleDecorator
# def sayHello():
#     print("hello")   



# Завдання 1. Простий декоратор
# Створіть декоратор, який виводить повідомлення START перед виконанням функції та END після її виконання. 
# Застосуйте його до функції, яка виводить привітання. 


# def decorator(func):
#     def wrapper():
#         print("START")
#         func()
#         print("END")

#     return wrapper


# def greeting():
#     print("Привіт!")


# greeting = decorator(greeting)

# greeting()


# Завдання 2. Перевірка числа
# Створіть декоратор positive_only, який перевіряє аргумент функції. 
# Якщо число від’ємне — виводить повідомлення про помилку та не запускає функцію. Перевірте його на функції обчислення квадрата числа.

# def positive_only(func):
#     def wrapper(number):
#         if number < 0:
#             print("Помилка: число від'ємне")
#             return

#         return func(number)

#     return wrapper


# @positive_only
# def square(number):
#     return number ** 2


# print(square(5))
# print(square(-3))



# Завдання 3. Декоратор-таймер
# Створіть декоратор timer, який вимірює час виконання функції. Перевірте його на функції, яка виконує велику кількість обчислень у циклі.


# def timerDecorator(func):
#     def wrapper():
#         print("START")

#         func()

#         print("END")

#     return wrapper


# @timerDecorator
# def calculations():
#     total = 0

#     for i in range(1000000):
#         total += i

#     print("Результат:", total)


# calculations()


# import time


# def timerDecorator(func):
#     def wrapper():
#         start = time.time()

#         func()

#         end = time.time()

#         print("Час виконання:", end - start, "секунд")

#     return wrapper


# @timerDecorator
# def calculations():
#     total = 0

#     for i in range(1000000):
#         total += i

#     print("Результат:", total)


# calculations()



# Завдання 4. Контроль доступу
# Створіть декоратор admin_required, який перевіряє роль користувача. Якщо роль "admin" — функція виконується, якщо "user" — виводиться


# def admin_requiredDecorator(func):
#     def wrapper(role):
#         if role == "admin":
#             func(role)
#         elif role == "user":
#             print("Доступ заборонено")

#     return wrapper


# @admin_requiredDecorator
# def show_admin_panel(role):
#     print("Адмін-панель відкрита")


# show_admin_panel("admin")
# show_admin_panel("user")



# Завдання 5. Декілька декораторів
# Створіть два різні декоратори та застосуйте їх одночасно до однієї функції. 
# Поміняйте декоратори місцями та порівняйте порядок виконання.

# def decorator_a(func):
#     def wrapper():
#         print("A START")
#         func()
#         print("A END")

#     return wrapper


# def decorator_b(func):
#     def wrapper():
#         print("B START")
#         func()
#         print("B END")

#     return wrapper


# # @decorator_a
# # @decorator_b
# # def hello():
# #     print("Привіт!")

# # hello()
# # поміняла місцями (верхній обгортає нижній)
# @decorator_b
# @decorator_a
# def hello():
#     print("Привіт!")

# hello()    

# Завдання 6. Перевірка аргументів
# Створіть декоратор, який перевіряє передані функції числа. Якщо всі числа додатні — функція виконується. 
# Якщо хоча б одне число від’ємне — виводиться повідомлення про помилку, а функція не запускається.

def positive_numbersDecorator(func):
    def wrapper(*args):
        for number in args:
            if number < 0:
                print("Помилка: число від’ємне")
                return

        return func(*args)

    return wrapper


@positive_numbersDecorator
def sum_numbers(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


print(sum_numbers(5, 10, 3))
sum_numbers(5, -2, 10)