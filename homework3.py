#  завдання 1
# num1 = float(input("Введіть перше число: "))
# num2 = float(input("Введіть друге число: "))
# num3 = float(input("Введіть третє число: "))

# print("\nЩо ви хочете зробити з цими числами?")
# print("1 — Порахувати суму")
# print("2 — Порахувати добуток")
# choice = input("Ваш вибір (1 або 2): ")

# if choice == "1":
#     total_sum = num1 + num2 + num3
#     print(f"\nСума трьох чисел дорівнює: {total_sum}")
# elif choice == "2":
#     product = num1 * num2 * num3
#     print(f"\nДобуток трьох чисел дорівнює: {product}")
# else:
#     print("\nПомилка: ви ввели неправильний варіант! Будь ласка, оберіть 1 або 2.")


#  завдання 2
# num1 = float(input("Введіть перше число: "))
# num2 = float(input("Введіть друге число: "))
# num3 = float(input("Введіть третє число: "))

# print("\nЩо ви хочете зробити з цими числами?")
# print("1 — Порахувати максимум із трьох")
# print("2 — Порахувати мінімум із трьох")
# print("3 — Порахувати середньоарифметичне трьох чисел")
# choice = input("Ваш вибір (1 ,2 або 3): ")

# if choice == "1":
#     maximum = max(num1, num2, num3)
#     print(f"\nМаксимум із трьох чисел: {maximum}")

# elif choice == "2":
#    minimum = max(num1, num2, num3)
#    print(f"\Мінімум із трьох чисел: {minimum}")   

# elif choice == "3":
#     average = (num1 + num2 + num3) / 3
#     print(f"\nСереднє арифметичне: {average}")   

# else:
#     print("\nПомилка: ви ввели неправильний варіант! Будь ласка, оберіть 1, 2 або 3.")    

#  завдання 3
# grade = int(input("Введіть оцінку (від 1 до 5): "))

# if grade == 1:
#     print("Дуже погано.")
# elif grade == 2:
#     print("Погано.")
# elif grade == 3:
#     print("Задовільно.")
# elif grade == 4:
#     print("Добре.")
# elif grade == 5:
#     print("Відмінно.")
# else:
#     print("Помилка: введено число поза межами діапазону 1-5.")

#  завдання 6
purchase_amount = float(input("Введіть суму покупки (грн): "))
age = int(input("Введіть свій вік: "))

if age < 18:
    discount_percent = 10
elif 18 <= age <= 60:
    discount_percent = 5
else:
    discount_percent = 15

discount_amount = purchase_amount * (discount_percent / 100)
final_amount = purchase_amount - discount_amount

print(f"Ваша знижка: {discount_percent}% (економія {discount_amount} грн)")
print(f"Підсумкова суму до сплати: {final_amount} грн")
  

