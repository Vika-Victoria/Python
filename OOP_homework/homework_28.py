# Домашня робота. Пов’язані списки
# Рівень 1
# Завдання 1. Ланцюжок міст

# Створіть клас Node.Створіть вручну 4 вузли зі значеннями:
# Київ
# Львів
# Одеса
# Харків
# Пов’яжіть їх у такому порядку:Київ → Львів → Одеса → Харків → None

# Виведіть:
# перше місто;
# друге місто;
# третє місто;
# четверте місто.

# При цьому для виведення використовуйте тільки змінну першого вузла.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


first = Node('Київ')
second = Node('Львів')
third = Node('Одеса')
fourth = Node('Харків')

first.next = second
second.next = third
third.next = fourth

print('Перше місто:', first.data)
print('Друге місто:', first.next.data)
print('Третє місто:', first.next.next.data)
print('Четверте місто:', first.next.next.next.data)



# Завдання 2. Пройдіть по всьому списку
# Створіть однозв’язний список:10 → 25 → 40 → 55 → 70 → None
# Не виводьте кожен вузол окремо через:node1.next.next...
# Замість цього використайте змінну:current та цикл while.
# Програма повинна вивести:
# 10
# 25
# 40
# 55
# 70
# Додатково: порахуйте кількість вузлів у списку.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


first = Node(10)
second = Node(25)
third = Node(40)
fourth = Node(55)
fifth = Node(70)


# пов'язуємо вузли
first.next = second
second.next = third
third.next = fourth
fourth.next = fifth

current = first

count = 0

while current is not None:
    print(current.data)

    count += 1
    current = current.next

print('Кількість вузлів:', count)


# Рівень 2 Завдання 3. Список улюблених фільмів

# Створіть класи:Node LinkedList
# У класі LinkedList реалізуйте метод:add_first()
# Додайте до списку:Interstellar Dune Avatar Titanic
# Після цього виведіть весь список.
# Перед запуском програми напишіть у коментарі, в якому порядку, на вашу думку, будуть розташовані фільми.
# Наприклад:# Я думаю, що результат буде:# ...

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

        while current is not None:
            print(current.data)
            current = current.next


# Я думаю, що результат буде:
# Titanic
# Avatar
# Dune
# Interstellar

movies = LinkedList()

movies.add_first('Interstellar')
movies.add_first('Dune')
movies.add_first('Avatar')
movies.add_first('Titanic')

movies.show()



# Завдання 4. Пошук студента
# Створіть однозв’язний список студентів:Анна → Максим → Ірина → Олексій → Марія
# Додайте до класу LinkedList метод:contains(value)
# Метод повинен повертати:True якщо значення знайдено, та:False якщо його немає.
# Приклад:students.contains("Ірина") Результат: True
# А: students.contains("Денис") Результат: False
# Додатково: зробіть так, щоб користувач сам вводив ім’я для пошуку.


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

    def contains(self, value):
        current = self.head

        while current is not None:
            if current.data == value:
                return True

            current = current.next

        return False


students = LinkedList()

students.add_first('Марія')
students.add_first('Олексій')
students.add_first('Ірина')
students.add_first('Максим')
students.add_first('Анна')

name = input('Введіть ім’я студента: ')

if students.contains(name):
    print('Студента знайдено')
else:
    print('Студента не знайдено')



# Рівень 3 Завдання 5. Плейлист
# Створіть власний однозв’язний список для зберігання назв пісень.
# У класі LinkedList реалізуйте методи:add_first()add_last()show()count()
# Користувач повинен додати щонайменше 5 пісень.
# Наприклад:
# Numb
# Believer
# Take On Me
# Zombie
# Thunder

# Програма повинна:
# Вивести весь плейлист.
# Вивести кількість пісень.
# Додати нову пісню на початок.
# Додати нову пісню в кінець.
# Знову показати плейлист.
# Додатково для сильніших: реалізуйте метод:contains(song)для пошуку пісні.    


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # додавання пісні на початок
    def add_first(self, song):
        new_node = Node(song)

        new_node.next = self.head
        self.head = new_node

    # додавання пісні в кінець
    def add_last(self, song):
        new_node = Node(song)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def show(self):
        if self.head is None:
            print('Плейлист порожній')
            return

        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    def count(self):
        current = self.head
        total = 0

        while current is not None:
            total += 1
            current = current.next

        return total

    # пошук пісні
    def contains(self, song):
        current = self.head

        while current is not None:
            if current.data == song:
                return True

            current = current.next

        return False


playlist = LinkedList()

for i in range(5):
    song = input(f'Введіть назву пісні {i + 1}: ')
    playlist.add_last(song)

т
print('\n--- МІЙ ПЛЕЙЛИСТ ---')
playlist.show()

print('\nКількість пісень:', playlist.count())


new_song = input('\nВведіть пісню для додавання на початок: ')
playlist.add_first(new_song)

new_song = input('Введіть пісню для додавання в кінець: ')
playlist.add_last(new_song)

print('\n--- ОНОВЛЕНИЙ ПЛЕЙЛИСТ ---')
playlist.show()

print('\nКількість пісень:', playlist.count())

song = input('\nВведіть назву пісні для пошуку: ')

if playlist.contains(song):
    print('Пісню знайдено!')
else:
    print('Пісню не знайдено!')




# Завдання 6. Потяг
# Уявіть, що кожен вузол однозв’язного списку — це вагон потяга.
# Кожен вузол повинен зберігати номер вагона:1 → 2 → 3 → 4 → 5 → None
# Створіть клас Train, який використовує однозв’язний список.
# Реалізуйте методи:add_wagon(number)show_train()count_wagons()
# Приклад:train = Train()
# train.add_wagon(1)
# train.add_wagon(2)
# train.add_wagon(3)
# train.show_train()
# Результат можна оформити так:[1] → [2] → [3] → None

# Метод:count_wagons()повинен повернути:3
# Для сильніших: додайте метод:find_wagon(number)який повідомляє, чи є вагон з таким номером.
# Додаткове завдання для сильних«Заміна значення»
# До класу LinkedList додайте метод:replace(old_value, new_value)
# Наприклад, маємо:10 → 20 → 30 → 40 → None
# Виконуємо:numbers.replace(30, 100)
# Отримуємо:10 → 20 → 100 → 40 → None
# Якщо значення не знайдено, метод повинен повідомити:Елемент не знайдено


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Train:
    def __init__(self):
        self.head = None

    def add_wagon(self, number):
        new_node = Node(number)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def show_train(self):
        current = self.head

        while current is not None:
            print(f'[{current.data}]', end=' → ')
            current = current.next

        print('None')

    def count_wagons(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next

        return count

    def find_wagon(self, number):
        current = self.head

        while current is not None:
            if current.data == number:
                return True

            current = current.next

        return False


train = Train()

train.add_wagon(1)
train.add_wagon(2)
train.add_wagon(3)
train.add_wagon(4)
train.add_wagon(5)

print('Наш потяг:')
train.show_train()

print('Кількість вагонів:', train.count_wagons())

number = int(input('\nВведіть номер вагона для пошуку: '))

if train.find_wagon(number):
    print('Такий вагон є у потязі')
else:
    print('Такого вагона немає у потязі')

# ДОДАТКОВЕ ЗАВДАННЯ: ЗАМІНА ЗНАЧЕННЯ
class LinkedList:
    def __init__(self):
        self.head = None

    def add_last(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def show(self):
        current = self.head

        while current is not None:
            print(current.data, end=' → ')
            current = current.next

        print('None')

    def replace(self, old_value, new_value):
        current = self.head

        while current is not None:
            if current.data == old_value:
                current.data = new_value
                return

            current = current.next

        print('Елемент не знайдено')


numbers = LinkedList()

numbers.add_last(10)
numbers.add_last(20)
numbers.add_last(30)
numbers.add_last(40)

print('\nПочатковий список:')
numbers.show()

numbers.replace(30, 100)

print('Список після заміни:')
numbers.show()
