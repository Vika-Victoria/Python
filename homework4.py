# завдання 1
# number = float(input("Введіть число: "))
# power = int(input("Введіть степінь від 0 до 7: "))

# if power >= 0 and power <= 7:
#     result = number ** power
#     print("Результат:", result)
# else:
#     print("Помилка! Степінь має бути від 0 до 7.")


# завдання 2
# Вартість розмови залежно від оператора:
# Якщо телефонуємо всередині одного оператора — додаткова плата 0%
# Kyivstar -> Vodafone — +20%
# Kyivstar -> lifecell — +30%
# Vodafone -> Kyivstar — +20%
# Vodafone -> lifecell — +30%
# lifecell -> Kyivstar — +20%
# lifecell -> Vodafone — +20%

# cost = float(input("Введіть вартість розмови: "))

# print("Оберіть оператора, з якого телефонуєте:")
# print("1 - Kyivstar")
# print("2 - Vodafone")
# print("3 - lifecell")

# from_operator = int(input("Ваш вибір: "))

# print("Оберіть оператора, на який телефонуєте:")
# print("1 - Kyivstar")
# print("2 - Vodafone")
# print("3 - lifecell")

# to_operator = int(input("Ваш вибір: "))

# if from_operator == to_operator:
#     result = cost
# elif from_operator == 1 and to_operator == 2:
#     result = cost * 1.2
# elif from_operator == 1 and to_operator == 3:
#     result = cost * 1.3
# elif from_operator == 2 and to_operator == 1:
#     result = cost * 1.2
# elif from_operator == 2 and to_operator == 3:
#     result = cost * 1.3
# elif from_operator == 3 and to_operator == 1:
#     result = cost * 1.2
# elif from_operator == 3 and to_operator == 2:
#     result = cost * 1.2
# else:
#     print("Помилка! Невірно обраний оператор.")
#     result = 0

# print("Вартість розмови:", result)


# завдання 3
# number = int(input("Введіть число від 1 до 100: "))

# if number < 1 or number > 100:
#     print("Помилка! Число повинно бути від 1 до 100.")
# elif number % 3 == 0 and number % 5 == 0:
#     print("Fizz Buzz")
# elif number % 3 == 0:
#     print("Fizz")
# elif number % 5 == 0:
#     print("Buzz")
# else:
#     print(number)


# завдання 4
# Базова зарплата кожного менеджера — 200$

# Вводимо рівень продажів для трьох менеджерів
# sales1 = float(input("Введіть продажі першого менеджера: "))
# sales2 = float(input("Введіть продажі другого менеджера: "))
# sales3 = float(input("Введіть продажі третього менеджера: "))


# # Розрахунок зарплати першого менеджера
# if sales1 < 500:
#     salary1 = 200 + sales1 * 0.03
# elif sales1 <= 1000:
#     salary1 = 200 + sales1 * 0.05
# else:
#     salary1 = 200 + sales1 * 0.08


# # Розрахунок зарплати другого менеджера
# if sales2 < 500:
#     salary2 = 200 + sales2 * 0.03
# elif sales2 <= 1000:
#     salary2 = 200 + sales2 * 0.05
# else:
#     salary2 = 200 + sales2 * 0.08


# # Розрахунок зарплати третього менеджера
# if sales3 < 500:
#     salary3 = 200 + sales3 * 0.03
# elif sales3 <= 1000:
#     salary3 = 200 + sales3 * 0.05
# else:
#     salary3 = 200 + sales3 * 0.08


# # Визначаємо найкращого менеджера
# if sales1 >= sales2 and sales1 >= sales3:
#     best = 1
#     salary1 += 200
# elif sales2 >= sales1 and sales2 >= sales3:
#     best = 2
#     salary2 += 200
# else:
#     best = 3
#     salary3 += 200

# print("Зарплата першого менеджера:", salary1, "$")
# print("Зарплата другого менеджера:", salary2, "$")
# print("Зарплата третього менеджера:", salary3, "$")
# print("Найкращий менеджер:", best)


# завдання 5
# Вводимо суму кредиту та термін
# credit = float(input("Введіть суму кредиту в $: "))
# years = int(input("Введіть термін кредиту в роках: "))

# # Визначаємо процентну ставку
# if credit <= 10000:
#     if years <= 3:
#         rate = 8
#     else:
#         rate = 10

# elif credit <= 50000:
#     if years <= 3:
#         rate = 12
#     else:
#         rate = 15

# else:
#     rate = 20

# # Розраховуємо суму відсотків
# interest = credit * rate / 100

# # Загальна сума до виплати
# total = credit + interest

# # Кількість місяців
# months = years * 12

# # Щомісячний платіж
# monthly_payment = total / months

# print("Процентна ставка:", rate, "%")
# print("Сума відсотків:", round(interest, 2), "$")
# print("Загальна сума до виплати:", round(total, 2), "$")
# print("Щомісячний платіж:", round(monthly_payment, 2), "$")



# завдання 6
# Ціни меню
salad = 5
soup = 7
chicken = 10
fish = 12
ice_cream = 3
fruit = 4

# Вибір клієнта
snack = input("Оберіть закуску (Салат / Суп): ")
main_dish = input("Оберіть основну страву (Курка / Риба): ")
dessert = input("Оберіть десерт (Морозиво / Фрукти): ")

# Статус клієнта
regular = input("Ви постійний клієнт? (так / ні): ")

# Визначаємо ціну закуски
if snack == "Салат":
    snack_price = salad
elif snack == "Суп":
    snack_price = soup
else:
    snack_price = 0

# Визначаємо ціну основної страви
if main_dish == "Курка":
    main_price = chicken
elif main_dish == "Риба":
    main_price = fish
else:
    main_price = 0

# Визначаємо ціну десерту
if dessert == "Морозиво":
    dessert_price = ice_cream
elif dessert == "Фрукти":
    dessert_price = fruit
else:
    dessert_price = 0

# Початкова сума
total = snack_price + main_price + dessert_price

# Визначаємо основну знижку
discount = 0

# Якщо замовлені всі три позиції
if snack_price > 0 and main_price > 0 and dessert_price > 0:

    # Якщо сума більше 20$ — знижка 15%
    if total > 20:
        discount = 15
    else:
        discount = 10

# Додаткова знижка для постійного клієнта
if regular == "так":
    discount = discount + 5

# Сума знижки
discount_amount = total * discount / 100

# Спеціальна пропозиція: Суп + Риба
special_discount = 0

if snack == "Суп" and main_dish == "Риба":
    special_discount = 2

# Безкоштовний напій: Курка + Морозиво
if main_dish == "Курка" and dessert == "Морозиво":
    print("Вам додається безкоштовний напій: Чай")

# Підсумкова вартість
final_price = total - discount_amount - special_discount

print("Вартість замовлення:", round(total, 2), "$")
print("Знижка:", discount, "%")
print("Спеціальна знижка:", special_discount, "$")
print("Підсумкова вартість:", round(final_price, 2), "$")
