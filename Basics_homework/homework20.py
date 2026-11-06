# Завдання 1
# Напишіть програму, яка відкриває файл data.txt і замінює в ньому всі входження слова "Python" на "Java", потім зберігає зміни в тому самому файлі.

# with open('data.txt', encoding='utf-8') as file:
#     data = file.read()

#     data = data.replace('Python', 'Java')

# with open('data.txt', 'w', encoding='utf-8') as file:
#     file.write(data)

# print('Текст у файлі замінено!')    


# Завдання 2
# Напишіть програму, яка відкриває файл data.txt, підраховує кількість 
# символів у кожному рядку і записує результати в новий файл char_count.txt у форматі "Рядок X: Y символів".

# with open('data.txt', encoding='utf-8') as file:
#     lines = file.readlines()

# with open('char_count.txt', 'w', encoding='utf-8') as file:
#     for index, line in enumerate(lines, 1):
#         count = len(line.strip('\n'))
#         file.write(f'Рядок {index}: {count} символів\n')


# print('Результати записано у файл char_count.txt')


# Завдання 3
# Напишіть програму, яка порівнює два файли (old_version.txt і new_version.txt) і 
# створює файл differences.txt, у якому вказуються рядки, присутні в одному файлі, але відсутні в іншому.

# with open('old_version.txt', encoding='utf-8') as file:
#     old_lines = file.readlines()

# with open('new_version.txt', encoding='utf-8') as file:
#     new_lines = file.readlines()

# with open('differences.txt', 'w', encoding='utf-8') as file:
#     for line in old_lines:
#         if line not in new_lines:
#             file.write('Тільки в old_version.txt: ' + line)

#     for line in new_lines:
#         if line not in old_lines:
#             file.write('Тільки в new_version.txt: ' + line)

# print('Відмінності записано у differences.txt')                    


# Завдання 4
# Напишіть програму, яка зчитує два файли (source.txt і words.txt), замінює всі слова зі words.txt у source.txt на *** і зберігає результат у censored.txt.


# with open('source.txt', encoding='utf-8') as file:
#     text = file.read()

# with open('words.txt', encoding='utf-8') as file:
#     words = file.read().splitlines()

# for word in words:
#     text = text.replace(word, '***')

# with open('censored.txt', 'w', encoding='utf-8') as file:
#     file.write(text)

# print('Цензурування завершено!')   



# Завдання 5
# Напишіть програму, яка реалізує керування замовленнями інтернет-магазину за допомогою текстового файлу orders.txt. Програма повинна надавати користувачеві меню з можливими діями:

# Додати нове замовлення – користувач вводить номер замовлення, назву товару, кількість і ціну, після чого дані додаються у файл.
# Переглянути всі замовлення – програма завантажує і відображає всі замовлення, збережені у файлі.
# Пошук замовлення за номером – користувач вводить номер замовлення, програма виводить інформацію про нього.
# Оновити замовлення – користувач вводить номер замовлення, програма дає змогу оновити кількість і ціну товару.
# Видалити замовлення – користувач вводить номер замовлення, і програма видаляє його з файлу, якщо він існує.
# Вихід – завершує виконання програми.

# def load_orders():
#     orders = {}

#     try:
#         with open('orders.txt', encoding='utf-8') as file:
#             for line in file:
#                 data = line.strip().split('|')

#                 if len(data) == 4:
#                     number = data[0]
#                     orders[number] = {
#                         'product': data[1],
#                         'quantity': int(data[2]),
#                         'price': float(data[3])
#                     }
#     except FileNotFoundError:
#         pass

#     return orders


# def save_orders(orders):
#     with open('orders.txt', 'w', encoding='utf-8') as file:
#         for number, order in orders.items():
#             file.write(
#                 f"{number}|{order['product']}|"
#                 f"{order['quantity']}|{order['price']}\n"
#             )


# def add_order():
#     orders = load_orders()

#     number = input('Введіть номер замовлення: ')

#     if number in orders:
#         print('Таке замовлення вже існує.')
#     else:
#         product = input('Введіть назву товару: ')

#         try:
#             quantity = int(input('Введіть кількість: '))
#             price = float(input('Введіть ціну: ').replace(',', '.'))

#             if quantity <= 0 or price < 0:
#                 print('Кількість має бути більшою за 0, а ціна — не від’ємною.')
#             else:
#                 orders[number] = {
#                     'product': product,
#                     'quantity': quantity,
#                     'price': price
#                 }

#                 save_orders(orders)
#                 print('Замовлення додано!')

#         except ValueError:
#             print('Помилка! Кількість має бути цілим числом, а ціна — числом.')


# def show_orders():
#     orders = load_orders()

#     if not orders:
#         print('Замовлень поки немає.')
#     else:
#         for number, order in orders.items():
#             print('\nНомер замовлення:', number)
#             print('Товар:', order['product'])
#             print('Кількість:', order['quantity'])
#             print('Ціна за одиницю:', order['price'], 'грн')
#             print('Загальна сума:', order['quantity'] * order['price'], 'грн')


# def find_order():
#     orders = load_orders()

#     number = input('Введіть номер замовлення для пошуку: ')

#     if number in orders:
#         order = orders[number]

#         print('Номер замовлення:', number)
#         print('Товар:', order['product'])
#         print('Кількість:', order['quantity'])
#         print('Ціна за одиницю:', order['price'], 'грн')
#         print('Загальна сума:', order['quantity'] * order['price'], 'грн')
#     else:
#         print('Замовлення не знайдено.')


# def update_order():
#     orders = load_orders()

#     number = input('Введіть номер замовлення для оновлення: ')

#     if number in orders:
#         try:
#             quantity = int(input('Введіть нову кількість: '))
#             price = float(input('Введіть нову ціну: ').replace(',', '.'))

#             if quantity <= 0 or price < 0:
#                 print('Кількість має бути більшою за 0, а ціна — не від’ємною.')
#             else:
#                 orders[number]['quantity'] = quantity
#                 orders[number]['price'] = price

#                 save_orders(orders)
#                 print('Замовлення оновлено!')

#         except ValueError:
#             print('Помилка! Перевірте введені числа.')
#     else:
#         print('Замовлення не знайдено.')


# def delete_order():
#     orders = load_orders()

#     number = input('Введіть номер замовлення для видалення: ')

#     if number in orders:
#         orders.pop(number)
#         save_orders(orders)
#         print('Замовлення видалено.')
#     else:
#         print('Замовлення не знайдено.')


# running = True

# while running:
#     print('\n===== МЕНЮ ЗАМОВЛЕНЬ =====')
#     print('1. Додати нове замовлення')
#     print('2. Переглянути всі замовлення')
#     print('3. Знайти замовлення за номером')
#     print('4. Оновити замовлення')
#     print('5. Видалити замовлення')
#     print('6. Вихід')

#     choice = input('Оберіть дію: ')

#     if choice == '1':
#         add_order()
#     elif choice == '2':
#         show_orders()
#     elif choice == '3':
#         find_order()
#     elif choice == '4':
#         update_order()
#     elif choice == '5':
#         delete_order()
#     elif choice == '6':
#         running = False
#         print('Програму завершено.')
#     else:
#         print('Неправильний вибір. Спробуйте ще раз.')



# Завдання 6
# Напишіть програму, яка реалізує керування даними про студентів університету за допомогою текстового файлу students.txt. Програма повинна надавати користувачеві меню з можливими діями:
# Додати нового студента – користувач вводить ім'я, курс і середній бал, програма додає їх у файл.
# Переглянути всіх студентів – програма завантажує і відображає всіх студентів, збережених у файлі.
# Пошук студента за ім'ям – користувач вводить ім'я студента, програма виводить інформацію про нього.
# Оновити дані студента – користувач вводить ім'я студента, програма дає змогу оновити його курс і середній бал.
# Видалити студента – користувач вводить ім'я студента, і програма видаляє його з файлу, якщо він існує.
# Вихід – завершує виконання програми.


def load_students():
    students = {}

    try:
        with open('students.txt', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split('|')

                if len(data) == 3:
                    name = data[0]
                    students[name] = {
                        'course': int(data[1]),
                        'average_grade': float(data[2])
                    }

    except FileNotFoundError:
        pass

    return students    

def save_students(students):
    with open('students.txt', 'w', encoding='utf-8') as file:
        for name, student in students.items():
            file.write(
                f"{name}|{student['course']}|"
                f"{student['average_grade']}\n"
            )

def add_student():
    students = load_students()

    name = input('Введіть ім’я студента: ').strip()

    if not name:
        print('Ім’я не може бути порожнім.')
    elif name in students:
        print('Такий студент вже існує.')
    else:
        try:
            course = int(input('Введіть курс: '))
            average_grade = float(
                input('Введіть середній бал: ').replace(',', '.')
            )

            if course < 1 or average_grade < 0 or average_grade > 100:
                print('Курс має бути більшим за 0, а бал — від 0 до 100.')
            else:
                students[name] = {
                    'course': course,
                    'average_grade': average_grade
                }

                save_students(students)

                print('Студента додано!')  

        except ValueError:
            print('Помилка! Курс має бути цілим числом, а бал — числом.')


def show_students():
    students = load_students()

    if not students:
        print('Список студентів порожній.')
    else:
        for name, student in students.items():
            print('\nІм’я:', name)
            print('Курс:', student['course'])
            print('Середній бал:', student['average_grade'])


def find_student():
    students = load_students()

    name = input('Введіть ім’я студента для пошуку: ').strip()

    if name in students:
        student = students[name]
                           
        print('Ім’я:', name)
        print('Курс:', student['course'])
        print('Середній бал:', student['average_grade'])
    else:
        print('Студента не знайдено.')


def update_student():
    students = load_students()

    name = input('Введіть ім’я студента для оновлення: ').strip()

    if name in students:
        try:
            course = int(input('Введіть новий курс: '))
            average_grade = float(
                input('Введіть новий середній бал: ').replace(',', '.')
            )

            if course < 1 or average_grade < 0 or average_grade > 100:
                 print('Курс має бути більшим за 0, а бал — від 0 до 100.')
            else:
                students[name]['course'] = course
                students[name]['average_grade'] = average_grade

                save_students(students)
                print('Дані студента оновлено!')
     
        except TypeError:
            print('Помилка! Перевірте введені числа.')
    else:
        print('Студента не знайдено.')

def delete_student():
    students = load_students()

    name = input('Введіть ім’я студента для видалення: ').strip()

    if name in students:
        students.pop(name)
        save_students(students)
        print('Студента видалено.')
    else:
        print('Студента не знайдено.')


running = True

while running:
    print('\n===== МЕНЮ СТУДЕНТІВ =====')
    print('1. Додати нового студента')
    print('2. Переглянути всіх студентів')
    print('3. Знайти студента за ім’ям')
    print('4. Оновити дані студента')
    print('5. Видалити студента')
    print('6. Вихід')

    choice = input('Оберіть дію: ')

    if choice == '1':
        add_student()
    elif choice == '2':
        show_students()
    elif choice == '3':
        find_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        running = False
        print('Програму завершено.')
    else:
        print('Неправильний вибір. Спробуйте ще раз.')

