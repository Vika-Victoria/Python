# Написати:
# def power(number, degree):
# без використання **.
# Наприклад:
# power(2, 4)
# повинна повернути 16.

# def power(number, degree):
#     if degree == 0:
#         return 1

#     return number * power(number, degree - 1)


# number = int(input("Введіть число: "))
# degree = int(input("Введіть степінь: "))

# print(power(number, degree))


# Завдання 1 — map(): ціни зі знижкою
# Є список цін:
# Plain Text
# prices = [120, 350, 80, 500, 240]
# За допомогою map() створіть новий список, у якому кожна ціна буде зменшена на 10%.
# Очікуваний результат:
# Plain Text
# [108.0, 315.0, 72.0, 450.0, 216.0]


# prices = [120, 350, 80, 500, 240]

# new_prices = list(map(lambda price: price * 0.9, prices))

# print(new_prices)


# Завдання 2 — map(): форматування імен 
# HTML
# names = ["anna", "ivan", "olena", "maksym"] 
# За допомогою map() перетворіть імена так, щоб кожне починалося з великої літери. 
# HTML
# ["Anna", "Ivan", "Olena", "Maksym"]

# names = ["anna", "ivan", "olena", "maksym"]

# new_names = list(map(lambda name: name.capitalize(), names))

# print(new_names)


# Завдання 3 — filter(): відбір оцінок
# Є оцінки студентів:
 
# HTML
# grades = [4, 10, 7, 12, 3, 8, 11, 5]
 
# За допомогою filter() залиште тільки оцінки 8 і вище.
# Очікуваний результат:
 
# HTML
# [10, 12, 8, 11]

# grades = [4, 10, 7, 12, 3, 8, 11, 5]

# new_grades = list(filter(lambda grade: grade >= 8, grades))

# print(new_grades)


# Завдання 4 — filter(): товари в наявності
 
# HTML
# products = [    ("Laptop", 5),    ("Mouse", 0),    ("Keyboard", 3),    ("Monitor", 0),    ("Headphones", 8)]
 
# За допомогою filter() залиште тільки товари, кількість яких більша за 0.

# products = [
#     ("Laptop", 5),
#     ("Mouse", 0),
#     ("Keyboard", 3),
#     ("Monitor", 0),
#     ("Headphones", 8)
# ]

# available_products = list(
#     filter(lambda product: product[1] > 0, products)
# )

# print(available_products)



# Завдання 5 — zip(): студенти та оцінки
# Є два списки:
 
# HTML
# students = ["Anna", "Ivan", "Olena", "Maksym"]grades = [10, 7, 12, 9]
 
# За допомогою zip() об'єднайте їх.
# Результат:
 
# HTML
# Anna — 10
# Ivan — 7
# Olena — 12
# Maksym — 9
 
# Додатково визначте, що станеться, якщо в одному списку буде більше елементів, ніж в іншому.


# students = ["Anna", "Ivan", "Olena", "Maksym"]
# grades = [10, 7, 12, 9]

# for student, grade in zip(students, grades):
#     print(student, "—", grade)


# Завдання 6 — zip(): каталог товарів
 
# HTML
# products = ["Laptop", "Mouse", "Keyboard", "Monitor"]prices = [35000, 800, 2200, 9000]
 
# Створіть за допомогою zip() словник:
 
# HTML
# {    "Laptop": 35000,    "Mouse": 800,    "Keyboard": 2200,    "Monitor": 9000}

# products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
# prices = [35000, 800, 2200, 9000]

# catalog = dict(zip(products, prices))

# print(catalog)


# Завдання 7 — filter() + map()
# Є список температур:
 
# HTML
# temperatures = [-5, 3, 8, -2, 12, 0, 17, -8]
 
# За допомогою filter() залиште тільки температури вище 0.
# За допомогою map() збільште кожне отримане значення на 2 градуси.
# Очікуваний результат:
 
# HTML
# [5, 10, 14, 19]



temperatures = [-5, 3, 8, -2, 12, 0, 17, -8]

positive_temperatures = list(
    filter(lambda temperature: temperature > 0, temperatures)
)

new_temperatures = list(
    map(lambda temperature: temperature + 2, positive_temperatures)
)

print(new_temperatures)