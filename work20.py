# import pickle

# students = [
#     {'name': 'max', 'age': 25, 'grade': [10, 9, 8]},
#     {'name': 'bob', 'age': 18, 'grade': [10, 12, 5]},
#     {'name': 'maria', 'age': 25, 'grade': [10, 12, 5]}
# ]

# # Зберігаємо список у файл
# with open('group.txt', 'wb') as f:
#     pickle.dump(students, f)

# # Завантажуємо список із файлу
# with open('group.txt', 'rb') as f:
#     data = pickle.load(f)

# print(data)  


# Завдання 1
# Користувач заповнює з клавіатури список цілих. Стисніть отримані дані та збе­ре­жіть їх у файл. Після цього завантажте дані з файлу в новий список.

# import pickle

# numbers = input('Введіть цілі числа через пробіл: ').split()

# numbers = [int(number) for number in numbers]

# with open('numbers.txt', 'wb') as file:
#     pickle.dump(numbers, file)

# with open('numbers.txt', 'rb') as file:
#     new_numbers = pickle.load(file)

# print('Початковий список:', numbers)
# print('Новий список:', new_numbers)


# Завдання 2
# При старті програми з'являється меню з наступними пунктами:
# Завантаження даних;
# Збереження даних;
# Додавання даних;
# Видалення даних.
# Використайте список цілих як сховища даних. Також застосуйте стиснення/роз­па­кування даних.

# import pickle

# numbers = []


# def load_data():
#     global numbers

#     try:
#         with open('numbers.txt', 'rb') as file:
#             numbers = pickle.load(file)

#         print('Дані завантажено:', numbers)

#     except FileNotFoundError:
#         print('Файл ще не існує. Спочатку збережіть дані.')


# def save_data():
#     with open('numbers.txt', 'wb') as file:
#         pickle.dump(numbers, file)

#     print('Дані збережено.')


# def add_data():
#     try:
#         number = int(input('Введіть ціле число: '))
#         numbers.append(number)
#         print('Число додано.')

#     except ValueError:
#         print('Потрібно ввести ціле число.')


# def delete_data():
#     print('Поточний список:', numbers)

#     try:
#         number = int(input('Введіть число для видалення: '))
#         numbers.remove(number)
#         print('Число видалено.')

#     except ValueError:
#         print('Такого числа немає у списку або введено некоректне значення.')


# while True:
#     print('\n--- МЕНЮ ---')
#     print('1. Завантаження даних')
#     print('2. Збереження даних')
#     print('3. Додавання даних')
#     print('4. Видалення даних')
#     print('5. Показати список')
#     print('0. Вихід')

#     choice = input('Виберіть пункт меню: ')

#     if choice == '1':
#         load_data()
#     elif choice == '2':
#         save_data()
#     elif choice == '3':
#         add_data()
#     elif choice == '4':
#         delete_data()
#     elif choice == '5':
#         print('Список:', numbers)
#     elif choice == '0':
#         print('Програму завершено.')
#         break
#     else:
#         print('Невірний пункт меню.')


# import pickle
# import json

# students = [
#     {'name': 'max', 'age': 25, 'grade': [10, 9, 8]},
#     {'name': 'bob', 'age': 18, 'grade': [10, 12, 5]},
#     {'name': 'maria', 'age': 25, 'grade': [10, 12, 5]}
# ]

# # Серіалізація через pickle
# with open('group.txt', 'wb') as f:
#     pickle.dump(students, f)

# # Десеріалізація через pickle
# with open('group.txt', 'rb') as f:
#     data = pickle.load(f)

# # Виведення даних
# for student in data:
#     for info, value in student.items():
#         print(info, value)
#     print('---')

# # Серіалізація через JSON
# with open('group.json', 'w', encoding='utf-8') as f:
#     json.dump(students, f, indent=4, ensure_ascii=False)




# Завдання 3
# Маємо певний словник з логінами і паролями користувачів. Логін використовується як ключ, пароль — як значення.
# Реалізуйте: додавання, видалення, пошук, реда­гу­вання, збереження та завантаження даних (використовуючи стиснення та розпа­кування).

                                                                                          
import json

users = {}


def add_user():
    login = input('Введіть логін: ')

    if login in users:
        print('Такий користувач вже існує.')
    else:
        password = input('Введіть пароль: ')
        users[login] = password
        print('Користувача додано.')


def delete_user():
    login = input('Введіть логін для видалення: ')

    if login in users:
        del users[login]
        print('Користувача видалено.')
    else:
        print('Користувача не знайдено.')


def find_user():
    login = input('Введіть логін для пошуку: ')

    if login in users:
        print('Логін:', login)
        print('Пароль:', users[login])
    else:
        print('Користувача не знайдено.')


def edit_user():
    login = input('Введіть логін користувача: ')

    if login in users:
        password = input('Введіть новий пароль: ')
        users[login] = password
        print('Пароль змінено.')
    else:
        print('Користувача не знайдено.')


def save_data():
    with open('users.json', 'w', encoding='utf-8') as file:
        json.dump(users, file, indent=4, ensure_ascii=False)

    print('Дані збережено.')


def load_data():
    global users

    try:
        with open('users.json', 'r', encoding='utf-8') as file:
            users = json.load(file)

        print('Дані завантажено.')

    except FileNotFoundError:
        print('Файл ще не існує. Спочатку збережіть дані.')

    except json.JSONDecodeError:
        print('Не вдалося прочитати JSON-файл.')


def show_users():
    if users:
        for login, password in users.items():
            print('Логін:', login, '| Пароль:', password)
    else:
        print('Список користувачів порожній.')


while True:
    print('\n========= МЕНЮ =========')
    print('1. Додати користувача')
    print('2. Видалити користувача')
    print('3. Знайти користувача')
    print('4. Редагувати пароль')
    print('5. Зберегти дані')
    print('6. Завантажити дані')
    print('7. Показати всіх користувачів')
    print('0. Вийти')
    print('========================')

    choice = input('Оберіть пункт меню: ')

    if choice == '1':
        add_user()
    elif choice == '2':
        delete_user()
    elif choice == '3':
        find_user()
    elif choice == '4':
        edit_user()
    elif choice == '5':
        save_data()
    elif choice == '6':
        load_data()
    elif choice == '7':
        show_users()
    elif choice == '0':
        print('Програму завершено.')
        break
    else:
        print('Невірний пункт меню.')



