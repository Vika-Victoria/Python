
# numbers = [3, 45, 46, 885]

# numbers.append(100)
# print(numbers)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(1)
n2 = Node(2)
n1.next = n2
n3 = Node(3)  
n2.next = n3

# print(n1.next.data)
# print(n2.data) 
# print(n3.data)   

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_first(self, data):
        new_noda = Node(data)
        new_noda.next = self.head
        self.head = new_noda

        self.size += 1

    def append(self, data):
        new_noda = Node(data)
        if self.head is None:
            self.head = new_noda
        else:
            current = self.head
            while current.next:
                current =current.next

            current.next = new_noda

            self.size += 1            

    def show(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

def contains(self, value):
    current = self.head

    while current:
        if current.data == value:
            return True
        current = current.next
    return False    

# nums = LinkedList()
# nums.add_first(10)
# nums.add_first(20)
# nums.add_first(30)
# nums.show()   
# print(nums.contains(60)) 


class DoudleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoudleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_last(self, data):
        new_data = DoudleNode(data)

        if self.head is None: 
            self.head = new_data
            self.tail = new_data
            return

        new_data.prev = self.tail

        self.tail.next = new_data
        self.tail = new_data

    def show_forward(self):
        current = self.tail
        while current:
            print(current.data)
            current = current.prev

# nums = DoudleLinkedList()
# nums.add_last(10)
# nums.add_last(20)  
# nums.add_last(30) 

# nums.show_forward()




# Завдання 1. Список студентів
# Створіть LinkedList.
# За допомогою:
# add_first()
# додайте:
# Anna
# Max
# Alex
# Kate
# Виведіть список.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def show(self):
        current = self.head

        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

students = LinkedList()

# students.add_first('Anna')
# students.add_first('Max')
# students.add_first('Alex')
# students.add_first('Kate')

# students.show()



# Завдання 2. Підрахунок елементів
# Додайте метод:
# count() який повертає кількість вузлів.
# Наприклад:
# print(students.count())

# counter = 0 — початковий лічильник.
# current = self.head — починаємо з першого вузла.
# while current — проходимо список, поки є вузли.
# counter += 1 — рахуємо кожен вузол.
# current = current.next — переходимо до наступного вузла.
# return counter — повертаємо загальну кількість.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def count(self):
        counter = 0
        current = self.head

        while current:
            counter += 1
            current = current.next
        return counter

    def show(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next

        print('None')


students = LinkedList()

# students.add_first('Anna')
# students.add_first('Max')
# students.add_first('Alex')
# students.add_first('Kate')

# students.show()
# print('Кількість студентів:', students.count())


# Створіть програму, яка імітує історію перегляду сторінок у браузері за допомогою двозв’язного списку.
# Кожен вузол списку повинен містити:
# prev — посилання на попередню сторінку.
# next — посилання на наступну сторінку.
# data — назву вебсторінки.
# має контекстне меню


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class BrowserHistory:
    def __init__(self):
        self.head = None
        self.current = None

    # відкрити нову сторінку
    def visit(self, data):
        new_node = Node(data)

        if self.current is None:
            self.head = new_node
        else:
            self.current.next = new_node
            new_node.prev = self.current

        self.current = new_node
        print(f'Відкрито сторінку: {data}')

    # назад
    def back(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            print(f'Поточна сторінка: {self.current.data}')
        else:
            print('Немає попередньої сторінки')

    # вперед
    def forward(self):
        if self.current and self.current.next:
            self.current = self.current.next
            print(f'Поточна сторінка: {self.current.data}')
        else:
            print('Немає наступної сторінки')

    # історія
    def show_history(self):
        current = self.head

        while current:
            if current == self.current:
                print(f'[{current.data}] <- поточна')
            else:
                print(current.data)

            current = current.next

    # видаляю поточну сторінку
    def delete_current(self):
        if self.current is None:
            print('Історія порожня')
            return

        if self.current.prev:
            self.current.prev.next = self.current.next
        else:
            self.head = self.current.next

        if self.current.next:
            self.current.next.prev = self.current.prev

        if self.current.prev:
            self.current = self.current.prev
        else:
            self.current = self.current.next

        print('Поточну сторінку видалено')


#історія браузера
# browser = BrowserHistory()

# while True:
#     print('\n--- ІСТОРІЯ БРАУЗЕРА ---')
#     print('1. Відкрити сторінку')
#     print('2. Назад')
#     print('3. Вперед')
#     print('4. Показати історію')
#     print('5. Видалити поточну сторінку')
#     print('0. Вихід')

#     choice = input('Оберіть дію: ')

#     if choice == '1':
#         page = input('Введіть назву сторінки: ')
#         browser.visit(page)

#     elif choice == '2':
#         browser.back()

#     elif choice == '3':
#         browser.forward()

#     elif choice == '4':
#         browser.show_history()

#     elif choice == '5':
#         browser.delete_current()

#     elif choice == '0':
#         print('Вихід із програми')
#         break

#     else:
#         print('Невірна команда')





# Завдання 2

# Користувач вводить з клавіатури набір рядків. Збережіть отримані рядки до двозв'язного списку. Після чого покажіть меню, в якому запропонуєте корис­ту­вачеві набір пунктів:

# 1. Додати елемент до списку.
# 2. Видалити елемент зі списку.
# 3. Показати вміст списку.
# 4. Перевірити, чи є значення у списку.
# 5. Замінити значення у списку.

# Дія виконується залежно від вибору користувача, після чого меню з'являється знову.

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def delete(self, data):
        current = self.head

        while current:
            if current.data == data:

                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev

                print('Елемент видалено')
                return

            current = current.next

        print('Елемент не знайдено')

    def show(self):
        if self.head is None:
            print('Список порожній')
            return

        current = self.head

        while current:
            print(current.data, end=' <-> ')
            current = current.next

        print('None')

    def search(self, data):
        current = self.head

        while current:
            if current.data == data:
                return True

            current = current.next

        return False

    # замінити значення
    def replace(self, old_data, new_data):
        current = self.head

        while current:
            if current.data == old_data:
                current.data = new_data
                print('Значення замінено')
                return

            current = current.next

        print('Елемент не знайдено')


my_list = DoublyLinkedList()

print('Введіть рядки (для завершення введіть 0):')

while True:
    value = input('Рядок: ')

    if value == '0':
        break

    my_list.add(value)

while True:
    print('\n--- МЕНЮ ---')
    print('1. Додати елемент')
    print('2. Видалити елемент')
    print('3. Показати список')
    print('4. Перевірити наявність елемента')
    print('5. Замінити значення')
    print('0. Вихід')

    choice = input('Оберіть дію: ')

    if choice == '1':
        value = input('Введіть новий рядок: ')
        my_list.add(value)

    elif choice == '2':
        value = input('Введіть рядок для видалення: ')
        my_list.delete(value)

    elif choice == '3':
        my_list.show()

    elif choice == '4':
        value = input('Введіть рядок для пошуку: ')

        if my_list.search(value):
            print('Значення є у списку')
        else:
            print('Значення відсутнє у списку')

    elif choice == '5':
        old_value = input('Яке значення замінити? ')
        new_value = input('На яке значення замінити? ')
        my_list.replace(old_value, new_value)

    elif choice == '0':
        print('Завершення програми')
        break

    else:
        print('Невірний пункт меню')
