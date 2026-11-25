
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

# print(stack)

stack.pop()
# print(stack)


class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return None
        
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

st = Stack()
# st.push(10)
# st.push(20)
# print(st.peek())


class BrocketChecker:
    def __init__(self):
        self.stack = Stack()

    def check(self, text):
        pairs = {
            '(': ")",
            '[': "]",
            '{': "}"
        }    

        for symbol in text:
            if symbol in pairs:
                self.stack.push(symbol)
            elif symbol in pairs.values():
                if self.stack.is_empty():
                    return False
                if pairs[self.stack.peek()] != symbol:
                    return False

                self.stack.pop()
       
        return self.stack.is_empty()

cheker = BrocketChecker()
text = "(([[]]))"

# if cheker.check(text):
#     print("ok")
# else:
#     print("not ok")    
    


# Створіть стек книг.
# Послідовно додайте:
# Harry Potter
# The Hobbit
# 1984
# Dune
# Виведіть книгу, яка знаходиться зверху.
# Заберіть її зі стека.
# Після цього виведіть книгу, яка тепер знаходиться зверху.


class Stack:
    def __init__(self):
        self.books = []

    def push(self, book):
        self.books.append(book)

    def pop(self):
        if self.is_empty():
            return None
        return self.books.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.books[-1]

    def is_empty(self):
        return len(self.books) == 0


stack = Stack()

stack.push('Harry Potter')
stack.push('The Hobbit')
stack.push('1984')
stack.push('Dune')

# print('Верхня книга:', stack.peek())

removed_book = stack.pop()
# print('Забрали зі стека:', removed_book)

# print('Нова верхня книга:', stack.peek())


# додати метод:
# size()
# який повертає кількість елементів у стеку.

class Stack:
    def __init__(self):
        self.books = []

    def push(self, book):
        self.books.append(book)

    def pop(self):
        if self.is_empty():
            return None
        return self.books.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.books[-1]

    def is_empty(self):
        return len(self.books) == 0

    def size(self):
        return len(self.books)

stack = Stack()

stack.push('Harry Potter')
stack.push('The Hobbit')
stack.push('1984')
stack.push('Dune')

# print('Кількість книг:', stack.size())

stack.pop()

# print('Кількість книг після видалення:', stack.size())




class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None

        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def peek(self):
        if self.is_empty():
            return True

        return self.queue[0]


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)




class PrintJob:
    def __init__(self, document, pages, priority):
        self.document = document
        self.pages = pages
        self.priority = priority

    def __str__(self):
        return f"{self.document} | {self.pages}"

# class PrinterQueue:
#     def __init__(self):
#         self.jobs = []
#     def add_jobs(self, job):
#         self.jobs.append(job)

#     def print_next(self):
#         if self.is_empty():
#             print("empty")
#             return

#         hig_pr = 0
#         for i in range(1, len(self.jobs)):
#             if self.jobs[i].priority > self.jobs[hig_pr].priority:
#                 hig_pr = i
        
#         job = self.jobs.pop(0)
#         print(f"printing {job}")

#     def add_jobs(self, job):
#         if isinstance(job , PrintJob):
#             self.jobs.append(job)  

#     def show_job(self):
#         print("printing")
#         for job in self.jobs:

# завдання
# Розробіть консольний додаток для автоматизації роботи кафе. Клієнти роблять замовлення, які потрапляють у чергу на приготування. Кухар обробляє замовлення в порядку їх надходження.
# Кожне замовлення повинно містити:
# Для реалізації програми обов’язково використайте структуру даних Queue.
# Вартість замовлення.
# Назву страви.
# Ім’я клієнта.
# Унікальний номер замовлення.


class Order:
    def __init__(self, order_id, client_name, dish_name, price):
        self.order_id = order_id
        self.client_name = client_name
        self.dish_name = dish_name
        self.price = price

    def show(self):
        print(f'Номер замовлення: {self.order_id}')
        print(f'Клієнт: {self.client_name}')
        print(f'Страва: {self.dish_name}')
        print(f'Вартість: {self.price} грн')


class Queue:
    def __init__(self):
        self.orders = []
        self.next_order_id = 1

    def enqueue(self, client_name, dish_name, price):
        order = Order(
            self.next_order_id,
            client_name,
            dish_name,
            price
        )

        self.orders.append(order)
        self.next_order_id += 1

        print('Замовлення додано до черги!')

    def dequeue(self):
        if self.is_empty():
            print('Черга порожня')
            return

        order = self.orders.pop(0)

        print('\n--- ГОТУЄМО ЗАМОВЛЕННЯ ---')
        order.show()
        print('Замовлення виконано!')

    def show_orders(self):
        if self.is_empty():
            print('Черга порожня')
            return

        for order in self.orders:
            print('-------------------')
            order.show()

    def is_empty(self):
        return len(self.orders) == 0

    def size(self):
        return len(self.orders)


cafe = Queue()

while True:
    print('\n===== КАФЕ =====')
    print('1. Додати замовлення')
    print('2. Приготувати замовлення')
    print('3. Показати чергу')
    print('4. Кількість замовлень')
    print('0. Вихід')

    choice = input('Оберіть дію: ')

    if choice == '1':
        client_name = input('Ім’я клієнта: ')
        dish_name = input('Назва страви: ')

        try:
            price = float(input('Вартість замовлення: '))

            if price <= 0:
                print('Вартість повинна бути більшою за 0')
                continue

            cafe.enqueue(client_name, dish_name, price)

        except ValueError:
            print('Введіть вартість числом')

    elif choice == '2':
        cafe.dequeue()

    elif choice == '3':
        cafe.show_orders()

    elif choice == '4':
        print('Кількість замовлень:', cafe.size())

    elif choice == '0':
        print('Роботу кафе завершено!')
        break

    else:
        print('Невірний пункт меню')