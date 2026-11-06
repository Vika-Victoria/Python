
# class Car:
#     pass


# car1 = Car()
# car1.brand = 'BMW'
# car1.color = 'black'
# print(car1.brand)
# print(car1.color)

# car2 = Car()

# print(car1)
# print(type(car1))
# print(car1.__dict__) #словник __dict__



# class Student:
#     shool = 'Itstep'

#     def __init__(self, name):
#         self.name = name
#         self.age = 0

#     def show_info(self):
#         print(self.name) 
#         print(self.age) 

#     def change_age(self, new_age):
#         self.age = new_age



# std1 = Student('Max')
# std1.age = 20
# std1.show_info()

# std2 = Student('Ben')
# std2.age = 23


# Створіть клас Counter.
 
# Додайте:
# - атрибут value;
# - метод increase(), який збільшує значення на 1;
# - метод decrease(), який зменшує значення на 1;
# - метод show(), який виводить поточне значення.
# Перевірте роботу методів.

# class Counter:
#     value = 0

#     def increase(self):
#         self.value += 1

#     def decrease(self):
#         self.value -= 1

#     def show(self):
#         print(self.value)


# counter = Counter()
# counter.show()       

# counter.increase()
# counter.show()       

# counter.increase()
# counter.increase()
# counter.show()       

# counter.decrease()
# counter.show()           



# Створіть клас Book.
 
# Атрибути:
# - title — назва;
# - author — автор;
# - pages — кількість сторінок.
# Методи:
# - show_info() — виводить інформацію про книгу;
# - is_long() — повертає True, якщо книга має більше 300 сторінок.
# Створіть два об'єкти й перевірте методи.

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def show_info(self):
#         print(f'Назва: {self.title}')
#         print(f'Автор: {self.author}')
#         print(f'Кількість сторінок: {self.pages}')

#     def is_long(self):
#         return self.pages > 300

# book1 = Book('Гаррі Поттер', 'Джоан Роулінг', 400)
# book2 = Book('Маленький принц', 'Антуан де Сент-Екзюпері', 120)

# book1.show_info()
# print('Довга книга:', book1.is_long())

# print('-------------------')

# book2.show_info()
# print('Довга книга:', book2.is_long())


# Створіть клас BankAccount.
# Атрибути:
# - owner — власник рахунку;
# - balance — баланс.
# Методи:
# - deposit(amount) — поповнення рахунку;
# - show_balance() — виведення балансу.

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def show_balance(self):
#         print(f'Власник рахунку: {self.owner}')
#         print(f'Баланс: {self.balance} грн.')


# account = BankAccount('Олена', 1000)

# account.show_balance()

# print('-------------------')

# account.deposit(500)
# account.show_balance() 
       


# class BankAccount:
#     def __init__(self, balance):
#         if balance < 0:
#             raise ValueError("balance cannot be engative")
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount <= 0:
#             print("amount cannot negative")
#             return

#         self.__balance += amount


#     def withraw(self, amount):
#         if amount <= 0:
#             print("amount cannot negative")
#             return

#         if amount > self.balance:
#             print("amount cannot be greater than balance")
#             return
#         self.__balance -= amount

#     def show_balanse(self):
#         return f"balance: {self.balance}"  


# account = BankAccount(100)

# account.deposit(500)
# account.withraw(300)
# print(account.show_balanse())


# Створіть клас Temperature.
# Вимоги:
# - Зберігати температуру в атрибуті __celsius.
# - Створити властивість celsius.
# - Заборонити температуру нижче −273.15 °C.
# - Додати метод to_fahrenheit().

# class Temperature:
#     def __init__(self, celsius):
#         self.celsius = celsius

#     @property
#     def celsius(self):
#         return self.__celsius

#     @celsius.setter
#     def celsius(self, value):
#         if value < -273.15:
#             print('Помилка! Температура не може бути нижче -273.15 °C')
#         else:
#             self.__celsius = value

#     def to_fahrenheit(self):
#         return self.__celsius * 9 / 5 + 32


# temp = Temperature(25)

# print('Температура:', temp.celsius, '°C')
# print('За Фаренгейтом:', temp.to_fahrenheit(), '°F')

# temp.celsius = 100
# print('Нова температура:', temp.celsius, '°C')

# temp.celsius = -300
# print('Температура:', temp.celsius, '°C')



# Створіть клас Student, який зберігає інформацію про студента.
# Атрибути:
# __grade — приватний атрибут оцінки.
# name — ім'я студента.
# Методи:
# show_info() — виводить ім'я та оцінку.
# set_grade(value) — змінює оцінку.
# get_grade() — повертає оцінку. 
# Умови: оцінка повинна бути в діапазоні від 0 до 100. Некоректні значення не повинні змінювати поточну оцінку. Початкова оцінка також має перевірятися.
#  має контекстне меню


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = 0
        self.set_grade(grade)

    def show_info(self):
        print(f'Ім’я студента: {self.name}')
        print(f'Оцінка: {self.__grade}')

    def set_grade(self, value):
        if 0 <= value <= 100:
            self.__grade = value
        else:
            print('Помилка! Оцінка повинна бути від 0 до 100.')

    def get_grade(self):
        return self.__grade


student = Student('Олена', 85)

student.show_info()
student.set_grade(95)

print('Нова оцінка:', student.get_grade())

student.set_grade(120)

print('Поточна оцінка:', student.get_grade())

student2 = Student('Андрій', 150)
student2.show_info()
