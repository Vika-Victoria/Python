# Завдання 1:
# Створи декоратор @debug_info, який перед виконанням функції виводить "Start function",
# а після — "End function".

# def debug_info(func):
#     def wrapper():
#         print("Start function")
#         func()
#         print("End function")
#     return wrapper   


# @debug_info
# def start_function():
#     print("Start function")

# start_function()  


# Завдання 2:
# Створи декоратор @check_login, який не дозволяє виконати функцію, якщо user_logged_in = False.
# user_logged_in = False
# @check_login
# def show_profile():
#  print("Welcome to your profile!")


# user_logged_in = False

# def check_login(func):
#     def wrapper():
#         if user_logged_in:
#             func()
#         else:
#             print("Please log in first!")
#     return wrapper


# @check_login
# def show_profile():
#     print("Welcome to your profile!")

# show_profile()    


# Завдання 3:
# Напиши декоратор @upper_text, який робить результат функції великими літерами.

# def upper_text(func):
#     def wrapper():
#         result = func()
#         return result.upper()
#     return wrapper


# @upper_text
# def greeting():
#     return "Hello, world!"


# print(greeting())


# Завдання 4:
# Створи декоратор @repeat_three_times, який запускає функцію тричі.

# def repeat_three_times(func):
#     def wrapper():
#         func()
#         func()
#         func()
#     return wrapper


# @repeat_three_times
# def test():
#     print("Привіт!")


# test()



# авдання 5. Приховування персональних даних
# Умова
# Створіть декоратор hide_personal_data.
# Після виконання функції потрібно приховати особисті дані у рядку.
# Приклад 1
# Функція повертає телефон
# @hide_personal_data
# def phone():
#  return "+380991234567"
# Результат
# +38099****567

# def hide_personal_data(func):
#     def wrapper():
#         data = func()

#         if "@" in data:
#             name, domain = data.split("@")
#             hidden_data = name[:3] + "*****@" + domain

#         else:
#             hidden_data = data[:6] + "****" + data[-3:]  

#         return hidden_data
    
#     return wrapper


# @hide_personal_data
# def phone():
#     return "+380991234567"

# @hide_personal_data
# def email():
#     return "student@gmail.com"

# print(phone())
# print(email()) 



# Додатково Мініпроєкт "Безпечна система"
# Створіть функцію
# show_profile()
# та застосуйте до неї відразу три декоратори:
# @working_hours
# @limit_calls(5)
# @logger
# def show_profile():
#  print("Особистий кабінет відкрито")
# Потрібно реалізувати:
# журналювання кожного виклику;
# обмеження кількості запусків;
# перевірку часу роботи.

from datetime import datetime


def logger(func):
    def wrapper():
        print("Журнал: виклик функції", func.__name__)
        return func()
    return wrapper


def limit_calls(max_calls):
    def decorator(func):
        calls = 0

        def wrapper():
            nonlocal calls

            if calls < max_calls:
                calls += 1
                return func()
            else:
                print("Помилка: перевищено ліміт викликів!")
        return wrapper
    return decorator


def working_hours(func):
    def wrapper():
        current_hour = datetime.now().hour

        if 9 <= current_hour < 18:
            return func()
        else:
            print("Доступ заборонено: неробочий час!")
    return wrapper


@logger
@limit_calls(5)
@working_hours
def show_profile():
    print("Особистий кабінет відкрито")


show_profile()