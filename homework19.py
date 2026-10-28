# Завдання 1
# Є словник: capitals = {"Україна": "Київ", "Польща": "Варшава", "Німеччина": "Берлін"}
# Виведи усі ключі (назви країн).
# Виведи усі значення (столиці).
# Додай до словника ще одну країну.

# capitals = {"Україна": "Київ", "Польща": "Варшава", "Німеччина": "Берлін"}

# print("Країни:")
# for country in capitals.keys():
#     print(country)

# print("Столиці:")
# for capital in capitals.values():
#     print(capital)

# capitals["Франція"] = "Париж"
# print("Оновлений словник:")
# print(capitals)    


# Завдання 2
# Створи словник prices, де зберігаються товари і їхня ціна:{"яблуко": 15, "банан": 20, "груша": 18}
# Попроси користувача ввести назву товару і виведи його ціну.
# Якщо товару немає — повідом: Такого товару немає в магазині.


# prices = {"яблуко": 15, "банан": 20, "груша": 18}

# product = input("Введіть назву товару: ")

# if product in prices:
#     print("Ціна товару:", prices[product], "грн")
# else:
#     print("Такого товару немає в магазині.")



# Завдання 3
# Створіть програму «Фірма», яка зберігає інформацію про працівників: ПІБ, телефон, корпоративний email, назва посади,
# номер кабінету, Skype. Реалізуйте можливість додавати, видаляти, знаходити та змінювати дані. Використовуйте словник
# для збереження інформації.

# employees = {}
# running = True

# while running:
#     print("\n===== ФІРМА =====")
#     print("1. Додати працівника")
#     print("2. Видалити працівника")
#     print("3. Знайти працівника")
#     print("4. Змінити дані працівника")
#     print("5. Вийти")

#     choice = input("Оберіть дію: ")

#     if choice == "1":
#         name = input("Введіть ПІБ: ")

#         if name in employees:
#             print("Такий працівник вже існує.")
#         else:
#             phone = input("Введіть телефон: ")
#             email = input("Введіть корпоративний email: ")
#             position = input("Введіть посаду: ")
#             office = input("Введіть номер кабінету: ")
#             skype = input("Введіть Skype: ")    

#             employees[name] = {
#                 "phone": phone,
#                 "email": email,
#                 "position": position,
#                 "office": office,
#                 "skype": skype
#             }

#             print("Працівника додано!")

#     elif choice == "2":
#         name = input("Введіть ПІБ працівника для видалення: ")

#         if name in employees:
#             employees.pop(name)
#             print("Працівника видалено.")
#         else:
#             print("Працівника не знайдено.")

#     elif choice == "3":
#         name = input("Введіть ПІБ працівника для пошуку: ")

#         if name in employees:
#             print("ПІБ:", name)

#             for key, value in employees[name].items():
#                 print(key, ":", value)
#             else:
#                 print("Працівника не знайдено.")

#     elif choice == "4":
#         name = input("Введіть ПІБ працівника: ")

#         if name in employees:
#             print("1. Телефон")
#             print("2. Email")
#             print("3. Посада")
#             print("4. Номер кабінету")
#             print("5. Skype")

#             field_choice = input("Що бажаєте змінити? ")

#             if field_choice == "1":
#                 field = "phone"
#             elif field_choice == "2":
#                 field = "email"
#             elif field_choice == "3":
#                 field = "position"
#             elif field_choice == "4":
#                 field = "office"
#             elif field_choice == "5":
#                 field = "skype"
#             else:
#                 field = ""

#             if field:
#                 new_value = input("Введіть нове значення: ")
#                 employees[name][field] = new_value
#                 print("Дані змінено.")
#             else:
#                 print("Неправильний вибір.")    
#         else:
#             print("Працівника не знайдено.")

#     elif choice == "5":
#         running = False
#         print("Програму завершено.")

# else:
#         print("Неправильний вибір. Спробуйте ще раз.")



# Завдання 4
# Напишіть функцію, яка об'єднує два словники. Якщо у них є спільні ключі, значення повинні складатися.

# def merge_dicts(dict1, dict2):
#     result = dict1.copy()

#     for key, value in dict2.items():
#         if key in result:
#             result[key] += value

#         else:
#             result[key] = value

#     return result

# dict1 = {'apple': 10, 'banana': 20, 'orange': 15}
# dict2 = {'banana': 5, 'orange': 10, 'pear': 12}

# result = merge_dicts(dict1, dict2)

# print(result)
                  

# Завдання 5: Підрахунок кількості слів у тексті
# Напишіть програму, яка підраховує кількість кожного слова у введеному тексті та зберігає цю інформацію в словнику.

text = input("Введіть текст: ")

words = text.lower().split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)    
 


