# Завдання 1
# Користувач вводить висоту трикутника і символ для заповнення. Програма повинна
# вивести трикутник, вирівняний по правому краю.

# try:
#     height = int(input("Введіть висоту трикутника: "))

#     if height == 0:
#         raise ValueError("Висота не може дорівнювати 0")

#     symbol = input("Введіть символ: ")

#     for row in range(1, height + 1):

#         print(" " * (height - row), end="")

#         for col in range(row):
#             print(symbol, end="")

#         print() 

# except ValueError:
#     print("Висота повинна бути цілим числом!")  

 
# Завдання 2
# Користувач вводить розміри дошки (ширину і висоту) і два символи для клітинок.
# Програма повинна відобразити шахову дошку, використовуючи ці символи.

# try:
#     height = int(input("Введіть висоту дошки: "))
#     width = int(input("Введіть ширину дошки: "))
#     symbol1 = input("Введіть символ 1: ")
#     symbol2 = input("Введіть символ 2: ")

#     if height == 0 or width == 0:
#         raise ValueError

#     for row in range(height):

#         for col in range(width):

#             if (row + col) % 2 == 0:
#                 print(symbol1, end=" ")
#             else:
#                 print(symbol2, end=" ")

#         print()      

# except ValueError:
#     print("Висота і ширина дошки повинна бути цілим числом!")    



# Завдання 3
# Програма випадковим чином загадує чотиризначне число без цифр, що повторюються. Користувач повинен спробувати вгадати це число, вводячи свої
# варіанти. Після кожного введення програма повідомляє:
# - Кількість цифр, які стоять на своїх місцях (бики).
# - Кількість цифр, які є в числі, але стоять не на своїх місцях (корови).

# import random

# a = random.randint(0, 9)
# b = random.randint(1, 9)

# while a == b:
#     b = random.randint(0, 9)

# c = random.randint(0, 9)

# while a == c or b == c:
#     c = random.randint(0, 9)

# d = random.randint(0, 9)

# while a == d or b == d or c == d:
#     d = random.randint(0, 9)

# number = a*1000 + b*100 + c*10 + d

# print("Чотиризначне число загадано!")

# while True:
#     guess = int(input("Введіть ваше число: "))

#     if guess < 1000 or guess > 9999:
#         print("Потрібно ввести чотиризначне число!")
#         continue

#     x = guess // 1000
#     y = guess // 100 % 10
#     z = guess // 10 % 10
#     w = guess % 10    

#     # Кількість биків
#     bulls = 0

#     if x == a:
#         bulls += 1

#     if y == b:
#         bulls += 1

#     if z == c:
#         bulls += 1

#     if w == d:
#         bulls += 1

#     # Перевіряємо, скільки цифр взагалі є в загаданому числі
#     matches = 0

#     if x == a or x == b or x == c or x == d:
#         matches += 1

#     if y == a or y == b or y == c or y == d:
#         matches += 1

#     if z == a or z == b or z == c or z == d:
#         matches += 1

#     if w == a or w == b or w == c or w == d:
#         matches += 1                 

#     # Корови = усі знайдені цифри відняти бики
#     cows = matches - bulls

#     print("Бики(кількість цифр, які стоять на своїх місцях): ", bulls)
#     print("Корови(кількість цифр, які є в числі, але стоять не на своїх місцях): ", cows)

#     if bulls == 4:
#         print("Вітаю! Ви вгадали число!")
#         break




# Завдання 4
# Напишіть консольну гру “Битва з босом”.
# Програма повинна:
# 1. Створити здоров’я гравця — 100.
# 2. Створити здоров’я боса — 150. 
# 3. Запустити цикл гри.
# 4. Кожен раунд показувати HP гравця і HP боса.
# 5. Давати гравцю вибір дії:
# o 1 — атакувати;
# o 2 — лікуватися;
# o 3 — втекти.
# 6. Якщо гравець атакує — бос втрачає випадкову кількість HP від 10 до 30.
# 7. Якщо гравець лікується — гравець відновлює випадкову кількість HP від 10 до 25.
# 8. Якщо гравець тікає — гра завершується.
# 9. Після дії гравця бос атакує і завдає випадкову шкоду від 5 до 20.
# 10. Якщо HP боса стало 0 або менше — гравець переміг.
# 11. Якщо HP гравця стало 0 або менше — гравець програв.

import random

try:
    
    player_hp = 100
    boss_hp = 150

    while True:
        print()
        print("*** НОВИЙ РАУНД ***")
        print("HP гравця:", player_hp)
        print("HP боса:", boss_hp)

        print()
        print("1 — Атакувати")
        print("2 — Лікуватися")
        print("3 — Втекти")

        choice = int(input("Виберіть дію: "))

        match choice:
            case 1:

                damage = random.randint(10, 30)
                boss_hp -= damage

                print("Ви завдали босу", damage, "шкоди!")  
                    
            case 2: 

                heal = random.randint(10, 25)
                player_hp += heal

                print("Ви відновили", heal, "HP!")

            case 3:
                print("Ви втекли з бою!")
                break

            case _:

                print("Невірний вибір!")
                continue   

        # перевірка , чи переміг гравець
        if boss_hp <= 0:
            print()
            print("Ви перемогли боса!")
            break

        # бос атакує
        boss_damage = random.randint(5, 20)
        player_hp -= boss_damage

        print("Бос завдав вам", boss_damage, "урону!")

        # eчи програв гравець
        if player_hp <= 0:
            print()
            print("Ви програли!")
            break

except ValueError:
    print("Потрібно вводити тільки числа!")
