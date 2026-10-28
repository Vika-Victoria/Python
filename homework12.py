# Завдання 1
# Користувач з клавіатури вводить список цілих чисел. Необхідно визначити кількість елементів у списку, які більші за попередній елемент. 
# Результат вивести на екран.

# numbers = []

# while True:
#     try:
#         number = int(input("Введіть число (0 — завершити): "))

#         if number == 0:
#             break

#     except ValueError:
#         print("Потрібно ввести ціле число!")

#     numbers.append(number)

# count = 0

# for num in range(1, len(numbers)):
#     if numbers[num] > numbers[num - 1]:
#         count += 1

# print("Кількість елементів:", count)       


# Завдання 2
# Користувач вводить список цілих чисел. Необхідно вивести тільки ті елементи, які зустрічаються у списку рівно один раз, зберігаючи порядок їхньої появи.

# numbers = []

# while True:
#     try:
#         number = int(input("Введіть число (0 — завершити): "))

#         if number == 0:
#             break

#     except ValueError:
#         print("Потрібно ввести ціле число!")

#     numbers.append(number)

# result = []

# for number in numbers:
#     if numbers.count(number) == 1:
#         result.append(number)

# print("Початковий список:", numbers)
# print("Елементи, які зустрічаються один раз:", result)


# Завдання 3
# Користувач з клавіатури вводить список чисел. Необхідно знайти у списку найдовшу послідовність елементів, 
# що зростають, і вивести її довжину та самі елементи.

# numbers = []

# while True:
#     try:
#         number = int(input("Введіть число (0 — завершити): "))

#         if number ==0:
#             break

#         numbers.append(number)

#     except ValueError:
#         print("Потрібно ввести ціле число!")

# # поточна послідовність з першого елемента
# current = [numbers[0]]

# # вважаємо перший елемент найдовшою послідовністю
# longest = [numbers[0]]

# for num in range(1, len(numbers)):
#     # чи поточний елемент більший за попередній
#     if numbers[num] > numbers[num - 1]:
#         current.append(numbers[num])
#     else:
#         # якщо зростання закінчилось,перевіряємо, чи поточна послідовність довша за найдовшу
#         if len(current) > len(longest):
#             longest = current    

#         current = [numbers[num]]

# if len(current) > len(longest):
#     longest = current

# print("Довжина послідовності:", len(longest))
# print("Послідовність:", longest)     


# Завдання 4
# Користувач із клавіатури вводить список цілих чисел. Необхідно реалізувати циклічний зсув списку вправо на N позицій.
# Результат вивести на екран.

# numbers = []

# while True:
#     try:
#         number = int(input("Введіть число (0 — завершити): "))

#         if number == 0:
#             break

#         numbers.append(number)

#     except ValueError:
#         print("Потрібно ввести ціле число!") 

# while True:
#     try:
#         n = int(input("Введіть кількість позицій для зсуву(N позицій): "))
#         break

#     except ValueError:
#         print("Потрібно ввести ціле число!")

# # залишаємо тільки потрібну кількість зсувів
# n = n % len(numbers)

# # останні N елементів
# right_part = numbers[-n:]

# # всі елементи, крім останніх N
# left_part = numbers[:-n]

# # праву частину на початок, а ліву — після неї
# numbers = right_part + left_part

# print("Зсунутий список:", numbers)

# Завдання 5
# Два списки цілих заповнюються випадковими числами. Необхідно:

# Сформувати третій список, що містить елементи обох списків;
# Сформувати третій список, що містить елементи обох списків без повторень;
# Сформувати третій список, що містить елементи спільні для двох списків;
# Сформувати третій список, що містить тільки унікальні елементи кожного зі списків;
# Сформувати третій список, що містить тільки мінімальне і максимальне значення кожного зі списків.

import random


numbers1 = [random.randint(1, 10) for n in range(10)]
numbers2 = [random.randint(1, 10) for n in range(10)]

print("Перший список: ", numbers1)
print("Другий список: ", numbers2)

# усі елементи обох списків
numbers3 = numbers1 + numbers2

print("Усі елементи обох списків:", numbers3)

# без повторень
numbers3 = []

for number in numbers1:
    if number not in numbers3:
        numbers3.append(number)

for number in numbers2:
    if number not in numbers3:
        numbers3.append(number)

print("Елементи обох списків без повторень: ", numbers3)  

# спільні для двох списків
numbers3 = []

for number in numbers1:
    if number in numbers2 and number not in numbers3:
        numbers3.append(number)

print("Елементи спільні для двох списків;", numbers3) 

# є тільки в одному зі списків
numbers3 = []

for number in numbers1:
    if number not in numbers2 and number not in numbers3:
        numbers3.append(number)

for number in numbers2:
    if number not in numbers1 and number not in numbers3:
        numbers3.append(number)

print("Унікальні елементи кожного зі списків: ", numbers3)    

# min/max значення кожного списку
numbers3 = []

numbers3.append(min(numbers1))
numbers3.append(max(numbers1))

numbers3.append(min(numbers2))
numbers3.append(max(numbers2))

print("Мінімальні та максимальні значення кожного зі списків:", numbers3)


# Завдання 6
# Користувач вводить список цілих чисел. Необхідно відсортувати список так, щоб числа чергувалися: спочатку найменше, 
# потім найбільше, потім друге за величиною, друге за мінімальністю тощо.

# numbers = []

# while True:
#     try:
#         number = int(input("Введіть число (0 — завершити): "))

#         if number == 0:
#             break

#         numbers. append(number)
        
#     except ValueError:
#         print("Потрібно ввести ціле число!")   

# numbers.sort()

# result = []

# left = 0 #зліва направо
# right = len(numbers) - 1 #справа наліво (остан. елемент)

# while left <= right:
#     result.append(numbers[left])

#     if left != right:
#         result.append(numbers[right])

#     left += 1 #до наступного найменшого
#     right -= 1 #до наступного найбільшого   

# print("Початковий відсортований список:", numbers)
# print("Результат:", result)    
               