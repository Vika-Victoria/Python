# numbers = [1, 2, 3]
# print(numbers)


# Завдання 1
# Створити список із п'яти улюблених фільмів.
# Вивести:
# весь список;
# перший фільм;
# третій;
# останній;
# кількість фільмів. 
 
# movies = ["Титанік", "Аватар", "Матриця", "Гладіатор", "Інтерстеллар"]
# print("Весь список:", movies)
# print("Перший фільм:", movies[0])
# print("Третій фільм:", movies[2])
# print("Останній фільм:", movies[-1])
# print("Кількість фільмів:", len(movies))


# Завдання 2
# Дано:
# grades = [7, 10, 8, 11, 9]
# Змінити першу оцінку на 10, а останню на 12.
# Вивести оновлений список.

# grades = [7, 10, 8, 11, 9]

# grades[0] = 10
# grades[-1] = 12

# print(grades)

# Завдання 3
# Є список:
# cities = ["Kyiv", "Dnipro", "Lviv", "Odesa"]
# Користувач вводить місто.
# Програма повинна повідомити, чи є воно у списку.

# cities = ["Kyiv", "Dnipro", "Lviv", "Odesa"]

# city = input("Введіть місто: ")

# if city in cities:
#     print("Місто є у списку")
# else:
#     print("Міста немає у списку")



# Завдання 1
# Користувач з клавіатури вводить елементи списку цілих чисел. Необхідно порахувати суму всіх елементів та їхнє середньоарифметичне. 
# Результати вивести на екран.(фактор обмеження придумати,  while True)

# numbers = []

# while True:
#     number = int(input("Введіть число (0 — завершити): "))

#     if number == 0:
#         break

#     numbers.append(number)

# sum_numbers = sum(numbers)
# aver = sum_numbers / len(numbers)

# print("Список:", numbers)
# print("Сума:", sum_numbers)
# print("Середньоарифметичне:", aver)




# Завдання 2
# Користувач з клавіатури вводить елементи списку цілих і деяке число. Необхідно порахувати скільки разів дане число присутнє у списку. 
# Результат вивести на екран.

# numbers = []

# while True:
#     number = int(input("Введіть число (0 — завершити): "))

#     if number == 0:
#         break

#     numbers.append(number)

# search_number = int(input("яке число потрібно порахувати?")) 

# count = 0

# for number in numbers:
#     if number == search_number:
#         count += 1

# print("Список:", numbers)
# print("Число", search_number, "зустрічається", count, "разів")        

# Завдання 3
# Користувач з клавіатури вводить список чисел. Необхідно знайти суму всіх додатних чисел у списку. Результат вивести на екран.

# numbers = []

# while True:
#     number = int(input("Введіть число (0 — завершити): "))

#     if number == 0:
#         break

#     numbers.append(number)

# sum_positive = 0

# for number in numbers:
#     if number > 0:
#         sum_positive += number

# print("Список:", numbers)
# print("Сума додатних чисел:", sum_positive)


# Завдання 4
# Користувач з клавіатури вводить список цілих чисел. Необхідно визначити індекси всіх парних чисел у списку. 
# Результат вивести на екран.


# numbers = []

# while True:
#     number = int(input("Введіть число (0 — завершити): "))

#     if number == 0:
#         break

#     numbers.append(number)

# even_indexes = []

# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         even_indexes.append(i)

# print("Список:", numbers)
# print("Індекси парних чисел:", even_indexes)


# Завдання 5
# Користувач з клавіатури вводить список цілих чисел. 
# Необхідно видалити зі списку всі елементи, що повторюються, залишивши тільки унікальні. 
# Результат вивести на екран.


numbers = []

while True:
    number = int(input("Введіть число (0 — завершити): "))

    if number == 0:
        break

    numbers.append(number)

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("Початковий список:", numbers)
print("Список без повторень:", unique_numbers)