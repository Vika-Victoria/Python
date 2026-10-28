# завдання 1
# first_number = float(input("Введіть перше число: "))
# second_number = float(input("Введіть друге число: "))
# third_number = float(input("Введіть третє число: "))

# total_sum = first_number + second_number + third_number
# product = first_number * second_number * third_number

# print("Загальна сума чисел: ", total_sum)
# print("Загальний добуток чисел: ", product)


# завдання 2
# first_diagonal = float(input("Введіть значення першої діагоналі ромбу: "))
# second_diagonal = float(input("Введіть значення другої діагоналі ромбу: "))

# square = (first_diagonal * second_diagonal)/2

# print("Площа ромба: ", square)


# завдання 3
# salary = float(input("Зарплата за місяць: "))
# credit = float(input("Сума місячного платежу за кредитом у банку: "))
# utilities = float(input("Заборгованість за комунальні послуги: "))

# remainder = salary - credit - utilities

# print("Залишок: ", remainder)


# завдання 4
# distance = float(input("Введіть відстань у кілометрах: "))
# fuel_consumption = float(input("Введіть витрату палива на 100 кілометрів: "))
# price_per_liter = float(input("Введіть ціну за літр бензину: "))

# total_cost = (distance / 100) * fuel_consumption * price_per_liter

# print("Підсумкову вартість поїздки: ", total_cost)


# завдання 5
# Константа для відсотка чайових (15%)
# TIP_PERCENTAGE = 0.15 

# total_bill = float(input("Введіть загальну суму рахунку в ресторані (грн): "))
# people_count = float(input("Введіть кількість осіб, які будуть ділити рахунок: "))

# tip_amount = total_bill * TIP_PERCENTAGE
# grand_total = total_bill + tip_amount
# share_per_person = grand_total / people_count

# print(f"Кожна людина має заплатити: {share_per_person:.2f} грн")


# завдання 6
daily_car_rental_cost = float(input("Введіть вартість оренди автомобіля за день: "))
rental_days = int(input("Введіть кількість днів оренди: "))
security_deposit = float(input("Введіть суму застави: "))

# Загальна вартість оренди БЕЗ застави
total_rental_cost = daily_car_rental_cost * rental_days

# Загальна сума до сплати(оренда + застава)
initial_payment = total_rental_cost + security_deposit

# Розрахунок вартості за один день (для перевірки, ділимо суму без застави на кількість днів)
calculated_daily_cost = total_rental_cost / rental_days

print(f"Загальна вартість оренди (без застави): {total_rental_cost} грн")
print(f"Сума до сплати спочатку (з урахуванням застави): {initial_payment} грн")
print(f"Сума, яка повертається вам після здачі авто (застава): {security_deposit} грн")
print(f"Чиста вартість оренди за один день: {calculated_daily_cost} грн")

