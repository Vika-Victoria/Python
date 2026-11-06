# завдання 1
# try:
#     number = float(input("Введіть число, з якого хочете отримати квадратний корінь: "))

#     if number < 0:
#         raise Exception("Не можна обчислити квадратний корінь від'ємного числа")

#     result = number ** 0.5

#     print("Квадратний корінь: ", result)

# except ValueError:
#     print("Помилка: потрібно ввести число")  

# except Exception as error:
#     print("Помилка: ", error)

# finally:
#     print("Обчислення завершено")       



# завдання 2
# try:
#     grade1 = float(input("Введіть першу оцінку: "))

#     if grade1 < 1 or grade1 > 12:
#         raise Exception("Неправильно введена перша оцінка")


#     grade2 = float(input("Введіть другу оцінку: "))

#     if grade2 < 1 or grade2 > 12:
#         raise Exception("Неправильна введена друга оцінка")

#     grade3 = float(input("Введіть третю оцінку: "))

#     if grade3 < 1 or grade3 > 12:
#         raise Exception("Неправильна введена третя оцінка")

#     average = (grade1 + grade2 + grade3) / 3

#     print("Середній бал:", average)


# except ValueError:
#     print("Оцінка має бути числом") 

# except Exception as error:
#     print(error)



# завдання 3
# try:
#     number1 = float(input("Введіть перше число: "))

#     number2 = float(input("Введіть друге число: "))

#     operation = input("Введіть дію (+, -, *, /): ")

#     if operation == "+":
#         result = number1 + number2

#     elif operation == "-":
#         result = number1 - number2

#     elif operation == "*":
#         result = number1 * number2

#     elif operation == "/":

#         if number2 == 0:
#             raise Exception("На нуль ділити не можна")

#         result = number1 / number2

#     else: 
#         raise Exception("Невідома операція")  

#     print("Результат: ", result)  
                    

# except ValueError:
#     print("Ви ввели текст замість числа!") 

# except Exception as error:
#     print(error)     
  

# завдання 4
START_BALANCE = 5000 

try:
    amount = float(input("Введіть суму зняття: "))

    if amount <= 0:
        raise Exception("Неправильна сума")

    if amount > START_BALANCE:
        raise Exception("Недостатньо коштів")

    result = START_BALANCE - amount

    print("Залишок: ", result)

except ValueError:
    print("Потрібно вводити тільки число")   

except Exception as error:
    print(error)     

