# 1. STOP
# Виводити числа від 1 до 100, але завершити цикл на 25.

# for i in range(1, 101):
#     if i == 25:
#         break

#     print(i)

# 2. Пропусти
# Вивести числа від 1 до 50, крім чисел, які діляться на 5.

# for i in range(1, 51):
#     if i % 5 == 0:
#         continue

#     print(i)

# 3. Введення
# Користувач вводить числа до 0.
# Потрібно:
# від'ємні пропускати;
# додатні перемножувати;
# після 0 показати кількість додатних чисел.

# product = 1
# count = 0

# while True:
#     number = int(input("Введіть число: "))

#     if number == 0:
#         break

#     if number < 0:
#         continue

#     product *= number
#     count += 1

# print("Добуток додатних чисел:", product)
# print("Кількість додатних чисел:", count)


# Завдання 3
# Користувач вводить із клавіатури дві межі діапазону і число. Якщо число не потрапляє в діапазон, програма просить користувача повторно ввести число,
#  і так доти, доки він не введе число правильно. Програма відображає всі числа діапазону, виділяючи число знаками оклику. Наприклад:
# Plain Text
# 1 2 3 !4! 5 6 7

# start = int(input("Введіть початок діапазону: "))
# end = int(input("Введіть кінець діапазону: "))

# number = int(input("Введіть число: "))

# while number < start or number > end:
#     print("Число не входить у діапазон!")
#     number = int(input("Введіть число ще раз: "))

# for i in range(start, end + 1):
#     if i == number:
#         print("!" + str(i) + "!", end=" ")
#     else:
#         print(i, end=" ")


# Завдання 5
# Користувач вводить N чисел (наприклад, 5). Програма повинна:
# Послідовно запитувати N чисел.
# Знайти та вивести максимальне із введених чисел.

# N = int(input("Скільки чисел будите вводити ?"))

# max = int(input("введіть число: "))

# for i in range(N - 1):
#     number = int(input("Введіть число: "))

#     if number > max:
#         max = number

# print("Максимальне число: ", max)      
 

from random import randint

score = 0
game_exit = False

while True:
    magic_num = randint(1, 100)
    user_num = 0
    tries = 0

    print(magic_num)

    while True:
        user_num = int(input("Guess num 1-100 (0 - exit) = "))

        if user_num == 0:
            print("Game over")
            game_exit = True
            break

        tries += 1

        if tries == 5:
            print("Game over")
            score -= 500
            break

        if user_num == magic_num:
            print("You win!")
            break
        elif user_num > magic_num:
            print("Your guess is too high")
        else:
            print("Your guess is too low")

    # користувач ввів 0
    if game_exit:
        break

    if tries < 5:
        print(f"You guessed {tries} times!")

    match tries:
        case 1:
            score += 1000
        case 2:
            score += 600
        case 3:
            score += 400
        case 4:
            score += 200
        case 5:
            pass

    print("Score: " + str(score))

    check = input("Do you wanna continue? (y/n): ")

    if check == "y":
        continue
    else:
        break



#  Завдання 7

# Необхідно написати програму, яка малює заповнену фігуру — квадрат або прямокутник — залежно від вибору користувача. Програма повинна виконувати такі кроки:

# Запитати в користувача тип фігури (квадрат або прямокутник).
# Запросити розміри фігури:
# Якщо обрано квадрат, запитати довжину сторони;
# Якщо обрано прямокутник, запитати ширину та висоту.
# Запросити символ, яким буде заповнена фігура.
# Вивести заповнену фігуру на екран.