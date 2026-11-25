# Домашня робота. Стек
# Рівень 1
# Завдання 1. Розвантаження вантажівки

# Коробки завантажували у вантажівку в такому порядку:

# Box 1
# Box 2
# Box 3
# Box 4
# Box 5

# Збережіть коробки у стек.

# Після цього розвантажте всі коробки, використовуючи pop().

# Програма повинна виводити:

# Розвантажено: Box 5
# Розвантажено: Box 4
# Розвантажено: Box 3
# Розвантажено: Box 2
# Розвантажено: Box 1

# Наприкінці виведіть: Вантажівка порожня
# Перед запуском програми поясніть у коментарі, чому Box 5 буде розвантажено першою.


class Stack:
    def __init__(self):
        self.items = []

    def push(self, box):
        self.items.append(box)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

truck = Stack()

truck.push('Box 1')
truck.push('Box 2')
truck.push('Box 3')
truck.push('Box 4')
truck.push('Box 5')

# Box 5 буде розвантажено першою,
# тому що стек працює за принципом LIFO:
# останній доданий елемент забирається першим.

while not truck.is_empty():
    box = truck.pop()
    print('Розвантажено:', box)

print('Вантажівка порожня')



# Завдання 2. Перевертач тексту
# Користувач вводить будь-який текст:Hello Python
# Додайте кожен символ рядка до стека.
# Потім, використовуючи тільки pop(), сформуйте рядок у зворотному порядку.
# Результат:nohtyP olleH
# Не можна використовувати: [::-1]
# Додатково Перевірте за допомогою стека, чи є введене слово паліндромом.

# Наприклад:
# level → паліндром
# python → не паліндром


class Stack:
    def __init__(self):
        self.items = []

    def push(self, char):
        self.items.append(char)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


text = input('Введіть текст: ')

stack = Stack()

for char in text:
    stack.push(char)

result = ''

while not stack.is_empty():
    result += stack.pop()

# print('Перевернутий текст:', result)

word = input('\nВведіть слово: ')

stack = Stack()

for char in word:
    stack.push(char)

reversed_word = ''

while not stack.is_empty():
    reversed_word += stack.pop()

if word == reversed_word:
    print('Слово є паліндромом')
else:
    print('Слово не є паліндромом')


# Завдання 3 
# Розробіть додаток, що імітує чергу запитів до сервера. Мають бути клієнти, 
# які надсилають запити на сервер, кожен з яких має свій пріоритет.
# Кожен новий клієнт потрапляє у чергу залежно від свого пріоритету.
# Зберігайте статистику запитів (користувач, час) в окремій черзі.
# Передбачте виведення статистики на екран. Вибір необхідних структур даних визначте самостійно.

from datetime import datetime


class Request:
    def __init__(self, user, priority):
        self.user = user
        self.priority = priority

    def show(self):
        print(f'Користувач: {self.user}')
        print(f'Пріоритет: {self.priority}')


class ServerQueue:
    def __init__(self):
        self.requests = []

    # додати запит з урахуванням пріоритету
    def enqueue(self, request):
        index = 0

        while index < len(self.requests):
            if self.requests[index].priority < request.priority:
                break
            index += 1

        self.requests.insert(index, request)

    # обробити перший запит
    def dequeue(self):
        if self.is_empty():
            print('Черга запитів порожня')
            return

        request = self.requests.pop(0)

        print('\n--- ОБРОБКА ЗАПИТУ ---')
        request.show()
        print('Запит оброблено сервером')

    def show_requests(self):
        if self.is_empty():
            print('Черга запитів порожня')
            return

        print('\n--- ЧЕРГА ЗАПИТІВ ---')

        for request in self.requests:
            request.show()

    # чи черга порожня
    def is_empty(self):
        return len(self.requests) == 0

    # к-ть запитів
    def size(self):
        return len(self.requests)


# черга статистики
class StatisticsQueue:
    def __init__(self):
        self.statistics = []

    # інформація про запит
    def add(self, user):
        current_time = datetime.now().strftime('%d.%m.%Y %H:%M:%S')

        record = {
            'user': user,
            'time': current_time
        }

        self.statistics.append(record)

    def show(self):
        if len(self.statistics) == 0:
            print('Статистика порожня')
            return

        print('\n--- СТАТИСТИКА ЗАПИТІВ ---')

        for record in self.statistics:
            print('Користувач:', record['user'])
            print('Час:', record['time'])


server = ServerQueue()
statistics = StatisticsQueue()

while True:
    print('\n===== СЕРВЕР =====')
    print('1. Надіслати запит')
    print('2. Обробити запит')
    print('3. Показати чергу запитів')
    print('4. Показати статистику')
    print('5. Кількість запитів')
    print('0. Вихід')

    choice = input('Оберіть дію: ')

    if choice == '1':
        user = input('Введіть ім’я користувача: ')

        try:
            priority = int(input('Введіть пріоритет (1-3): '))

            if priority < 1 or priority > 3:
                print('Пріоритет повинен бути від 1 до 3')
                continue

            request = Request(user, priority)

            server.enqueue(request)
            statistics.add(user)

            print('Запит додано до черги!')

        except ValueError:
            print('Пріоритет потрібно ввести числом')

    elif choice == '2':
        server.dequeue()

    elif choice == '3':
        server.show_requests()

    elif choice == '4':
        statistics.show()

    elif choice == '5':
        print('Кількість запитів у черзі:', server.size())

    elif choice == '0':
        print('Роботу сервера завершено!')
        break

    else:
        print('Невірний пункт меню')
