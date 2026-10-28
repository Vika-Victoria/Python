# Завдання 1
# Напишіть функцію, яка відображає на екран форматований текст, зазначений нижче:

# "Don't compare yourself with anyone in this world… 
#     if you do so, you are insulting yourself."
#         Bill Gates

# def print_text():
#     print("\"Don't compare yourself with anyone in this world… ")
#     print("   if you do so, you are insulting yourself.\"")
#     print("       Bill Gates")

# print_text() 


# Завдання 2
# Напишіть функцію, яка приймає два числа як параметр і відображає всі парні числа між ними.

# def even_numbers(number1, number2):

#     if number1 > number2:
#         number1, number2 = number2, number1

#     for number in range(number1, number2 + 1):
#         if number % 2 == 0:
#             print(number)

# number1 = int(input("Введіть перше число: "))
# number2 = int(input("Введіть друге число: "))

# even_numbers(number1, number2)    


# Завдання 3
# Напишіть функцію, яка відображає порожній або заповнений квадрат з деякого символу.
# Функція приймає як параметри: довжину сторони квадрата, символ і змінну логічного типу:
# якщо вона дорівнює True, квадрат заповнений;
# якщо False, квадрат порожній.        

# def draw_square(size, symbol, filled):
#     for row in range(size):# рядок квадрата
#         for column in range(size):# символи цього рядка
#             if filled:
#                 print(symbol, end="")
#             else:
#                 if row == 0 or row == size - 1 or column == 0 or column == size - 1:
#                     print(symbol, end="")
#                 else:
#                     print(" ", end="")

#         print()# перейти на новий рядок

# size = int(input("Введіть довжину сторони квадрата: "))
# symbol = input("Введіть символ: ")
# filled = input("Заповнений квадрат? (True/False): ")  

# if filled == "True":
#     filled = True
# else:
#     filled = False

# draw_square(size, symbol, filled)  


# Завдання 4
# Напишіть функцію, яка повертає мінімальне з п'яти чисел. Числа передаються як параметри 

# def find_min(number1, number2, number3, number4, number5):
#     minimum = number1

#     if number2 < minimum:
#         minimum = number2

#     if number3 < minimum:
#         minimum = number3

#     if number4 < minimum:
#         minimum = number4 

#     if number5 < minimum:
#         minimum = number5 

#     return minimum

# number1 = int(input("Введіть перше число: "))
# number2 = int(input("Введіть друге число: "))
# number3 = int(input("Введіть третє число: "))
# number4 = int(input("Введіть четверте число: "))
# number5 = int(input("Введіть п'яте число: "))

# print("Мінімальне число:", find_min(number1, number2, number3, number4, number5))                  



# Завдання 5
# Напишіть функцію, яка рахує кількість цифр у числі. Число передається як параметр. 
# З функції потрібно повернути отриману кількість цифр. Наприклад, якщо передали 3456, кількість цифр буде 4.


# def count_digits(number):
#     count = 0

#     while number > 0:
#         number = number // 10
#         count += 1

#     return count

# number = int(input("Введіть число: "))

# print("Кількість цифр:", count_digits(number))    



# Завдання 6
# Напишіть функцію, яка перевіряє чи є число паліндромом. Число передається як параметр. Якщо число паліндром, потрібно повернути з функції true,
# інакше false.
# "Паліндром" — це число, у якого перша частина цифр дорівнює другій перевернутій частині цифр.
# Наприклад, 123321 — паліндром (перша частина 123, друга 321, яка після перевороту стає 123), 546645 — паліндром, а 421987 — не паліндром.

def is_palindrome(number):
    
    if number == 0:
        return True
    
    original_number = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    if original_number == reversed_number:
        return True
    else:
        return False


number = int(input("Введіть число: "))

print(is_palindrome(number))       
