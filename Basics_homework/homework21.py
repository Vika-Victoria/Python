# Завдання 1. Робота з JSON
# Створіть словник з інформацією про себе:
# student = {
#  "name": "Іван",
#  "age": 20,
#  "city": "Київ",
#  "group": "ПЗ-23"
# }
# Необхідно:
# Записати словник у файл student.json.
# Зчитати дані з файлу.
# Вивести інформацію у форматі:
# Ім'я: Іван
# Вік: 20
# Місто: Київ
# Група: ПЗ-23

# import json

# student = {
#     "name": "Іван",
#     "age": 20,
#     "city": "Київ",
#     "group": "ПЗ-23"
# }

# with open('student.json', 'w', encoding='utf-8') as file:
#     json.dump(student, file, ensure_ascii=False, indent=4)

# with open('student.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)

# print('Ім’я:', data['name'])
# print('Вік:', data['age'])
# print('Місто:', data['city'])
# print('Група:', data['group'])


# Завдання 2. Робота з CSV
# Створіть файл products.csv.
# Користувач вводить інформацію про 5 товарів:
# назва;
# ціна;
# кількість.
# Після введення всі дані потрібно записати у CSV-файл.
# Після цього:
# прочитати файл;
# вивести всі товари у вигляді таблиці.

# import csv

# products = []

# for i in range(5):
#     print(f'\nТовар №{i + 1}')

#     name = input('Введіть назву товару: ')
#     price = input('Введіть ціну товару: ')
#     quantity = input('Введіть кількість товару: ')    

#     product = {
#         'name': name,
#         'price': price,
#         'quantity': quantity
#     }

#     products.append(product)

#     with open('products.csv', 'w', newline='', encoding='utf-8') as file:
#         fieldnames = ['name', 'price', 'quantity']

#         writer = csv.DictWriter(file, fieldnames=fieldnames)

#         writer.writeheader()
#         writer.writerows(products)

# print('\nДані записано у файл products.csv')

# with open('products.csv', 'r', newline='', encoding='utf-8') as file:
#     reader = csv.DictReader(file)

#     products = list(reader)

# # Виводимо товари у вигляді таблиці
# print('\n' + '-' * 55)
# print(f'{"Назва":<25} {"Ціна":<12} {"Кількість":<12}')
# print('-' * 55)


# for product in products:
#     print(
#         f'{product["name"]:<25} '
#         f'{product["price"]:<12} '
#         f'{product["quantity"]:<12}'
#     )

# print('-' * 30)



# Завдання 3 *. Каталог фільмів (JSON)
# Створіть програму «Каталог фільмів».
# Для збереження інформації використовуйте файл movies.json.
# Для кожного фільму зберігайте:
# назву;
# жанр;
# рік;
# рейтинг.
# Реалізуйте меню:
# 1. Додати фільм
# 2. Показати всі фільми
# 3. Знайти фільми за жанром
# 4. Видалити фільм
# 5. Вихід
# Усі зміни повинні автоматично зберігатися у JSON-файл.


# import json

# movies = []


# def save_movies():
#     with open('movies.json', 'w', encoding='utf-8') as file:
#         json.dump(movies, file, ensure_ascii=False, indent=4)


# def load_movies():
#     global movies

#     try:
#         with open('movies.json', 'r', encoding='utf-8') as file:
#             movies = json.load(file)

#     except FileNotFoundError:
#         movies = []


# def add_movie():
#     title = input('Введіть назву фільму: ')
#     genre = input('Введіть жанр: ')

#     try:
#         year = int(input('Введіть рік: '))
#         rating = float(input('Введіть рейтинг: '))

#         movie = {
#             'title': title,
#             'genre': genre,
#             'year': year,
#             'rating': rating
#         }

#         movies.append(movie)
#         save_movies()

#         print('Фільм додано!')

#     except ValueError:
#         print('Рік має бути цілим числом, а рейтинг — числом.')


# def show_movies():
#     if movies:
#         for movie in movies:
#             print('\nНазва:', movie['title'])
#             print('Жанр:', movie['genre'])
#             print('Рік:', movie['year'])
#             print('Рейтинг:', movie['rating'])
#             print('-' * 30)
#     else:
#         print('Каталог фільмів порожній.')


# def find_movies_by_genre():
#     genre = input('Введіть жанр для пошуку: ').lower()
#     found = False

#     for movie in movies:
#         if movie['genre'].lower() == genre:
#             print('\nНазва:', movie['title'])
#             print('Жанр:', movie['genre'])
#             print('Рік:', movie['year'])
#             print('Рейтинг:', movie['rating'])
#             print('-' * 30)

#             found = True

#     if not found:
#         print('Фільмів такого жанру не знайдено.')


# def delete_movie():
#     title = input('Введіть назву фільму для видалення: ').lower()

#     for movie in movies:
#         if movie['title'].lower() == title:
#             movies.remove(movie)
#             save_movies()
#             print('Фільм видалено!')
#             return

#     print('Фільм не знайдено.')


# load_movies()

# while True:
#     print('\n===== КАТАЛОГ ФІЛЬМІВ =====')
#     print('1. Додати фільм')
#     print('2. Показати всі фільми')
#     print('3. Знайти фільми за жанром')
#     print('4. Видалити фільм')
#     print('5. Вихід')

#     choice = input('Оберіть пункт меню: ')

#     if choice == '1':
#         add_movie()
#     elif choice == '2':
#         show_movies()
#     elif choice == '3':
#         find_movies_by_genre()
#     elif choice == '4':
#         delete_movie()
#     elif choice == '5':
#         print('До побачення!')
#         break
#     else:
#         print('Невірний пункт меню.')


# Завдання 4**. Електронний журнал (CSV)
# Створіть програму «Журнал оцінок».
# Інформацію зберігайте у файлі grades.csv.
# Для кожного студента потрібно записувати:
# ПІБ;
# групу;
# оцінку.
# Реалізуйте меню:
# 1. Додати студента
# 2. Показати всіх студентів
# 3. Знайти студента
# 4. Обчислити середній бал групи
# 5. Показати студентів із балом більше 90
# 6. Вихід
# Додатково (за бажанням)
# Під час виведення інформації відсортувати студентів за оцінкою (від більшої до меншої).

import csv

FILE_NAME = 'grades.csv'


def load_students():
    students = []

    try:
        with open(FILE_NAME, 'r', encoding='utf-8', newline='') as file:
            reader = csv.DictReader(file)

            for student in reader:
                student['grade'] = float(student['grade'])
                students.append(student)

    except FileNotFoundError:
        students = []

    return students


def save_students(students):
    with open(FILE_NAME, 'w', encoding='utf-8', newline='') as file:
        fieldnames = ['name', 'group', 'grade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(students)


def add_student(students):
    name = input('Введіть ПІБ студента: ')
    group = input('Введіть групу: ')

    try:
        grade = float(input('Введіть оцінку від 0 до 100: '))

        if grade < 0 or grade > 100:
            print('Оцінка має бути від 0 до 100.')
            return

        student = {
            'name': name,
            'group': group,
            'grade': grade
        }

        students.append(student)
        save_students(students)

        print('Студента додано!')

    except ValueError:
        print('Помилка! Оцінка має бути числом.')


def show_students(students):
    if not students:
        print('Журнал порожній.')
        return

    sorted_students = sorted(
        students,
        key=lambda student: student['grade'],
        reverse=True
    )

    print('\n' + '-' * 65)
    print(f"{'ПІБ':<30} {'Група':<15} {'Оцінка':>10}")
    print('-' * 65)

    for student in sorted_students:
        print(
            f"{student['name']:<30} "
            f"{student['group']:<15} "
            f"{student['grade']:>10.1f}"
        )

    print('-' * 65)


def find_student(students):
    search_name = input('Введіть ПІБ або частину імені: ').lower()
    found = False

    for student in students:
        if search_name in student['name'].lower():
            print(
                f"ПІБ: {student['name']}, "
                f"група: {student['group']}, "
                f"оцінка: {student['grade']}"
            )
            found = True

    if not found:
        print('Студента не знайдено.')


def calculate_group_average(students):
    group_name = input('Введіть назву групи: ').lower()

    total_grade = 0
    count = 0

    for student in students:
        if student['group'].lower() == group_name:
            total_grade += student['grade']
            count += 1

    if count > 0:
        average = total_grade / count
        print(f'Середній бал групи: {average:.2f}')
    else:
        print('Студентів цієї групи не знайдено.')


def show_students_above_90(students):
    found = False

    sorted_students = sorted(
        students,
        key=lambda student: student['grade'],
        reverse=True
    )

    for student in sorted_students:
        if student['grade'] > 90:
            print(
                f"ПІБ: {student['name']}, "
                f"група: {student['group']}, "
                f"оцінка: {student['grade']}"
            )
            found = True

    if not found:
        print('Студентів з оцінкою більше 90 немає.')


students = load_students()

while True:
    print('\n===== ЖУРНАЛ ОЦІНОК =====')
    print('1. Додати студента')
    print('2. Показати всіх студентів')
    print('3. Знайти студента')
    print('4. Обчислити середній бал групи')
    print('5. Показати студентів із балом більше 90')
    print('6. Вихід')

    choice = input('Оберіть пункт меню: ')

    if choice == '1':
        add_student(students)

    elif choice == '2':
        show_students(students)

    elif choice == '3':
        find_student(students)

    elif choice == '4':
        calculate_group_average(students)

    elif choice == '5':
        show_students_above_90(students)

    elif choice == '6':
        print('До побачення!')
        break

    else:
        print('Невірний пункт меню.')
