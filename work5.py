# number = float(input("Введіть число: "))
# print(number)

# secret_code = 1234

# try:
#     code = int(input("Введіть секретний код: "))

#     if code == secret_code:
#         print("Сейф відкрито!")
#     else:
#         print("Неправильний код!")

# except ValueError:
#     print("Помилка: потрібно ввести число!")


# secret_number = 50

# try:
#     number = int(input("Введіть число: "))

#     if number > secret_number:
#         print("Менше")
#     elif number < secret_number:
#         print("Більше")
#     else:
#         print("Перемога!")

# except ValueError:
#     print("Помилка: потрібно ввести число!")

# try:
#     age = int(input("Введіть свій вік: "))

#     if age < 0 or age > 120:
#         raise Exception("Некоректний вік")

#     print("Вік правильний")

# except Exception as e:
#     print(e)


balance = 5000

try:
    amount = float(input("Введіть суму для зняття: "))

    if amount <= 0:
        raise ValueError("Сума повинна бути більшою за 0")

    if amount > balance:
        raise ValueError("Недостатньо коштів на рахунку")

    balance -= amount

    print(f"Залишок на рахунку: {balance}")

except ValueError as e:
    print(f"Помилка: {e}")