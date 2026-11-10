class Animal:
    def __init__(self, name, age, color):
        self._name = name
        self._age = age
        self._color = color

    def show_info(self):
        print(f'Ім’я: {self._name}')
        print(f'Вік: {self._age}')
        print(f'Колір: {self._color}')

    def make_sound(self):
        print('Тварина видає звук.')   

        


class Cat(Animal):
    def clean(self):
        print('Кіт вмивається.')

    def make_sound(self):
        print('Мяу-мяу!')     
           


class Dog(Animal):
    def bark(self):
        print('Собака гавкає.')

    def make_sound(self):
        print('Гав-гав!') 


# cat1 = Cat("Mursik", 10, "black")
# cat1.show_info() 
# cat1.make_sound()      


class Vehicle:
    def move(self):
        print('Транспорт рухається.')


class Car(Vehicle):
    def move(self):
        print('Автомобіль їде.')


class Bicycle(Vehicle):
    def move(self):
        print('Велосипед їде.')


# car = Car()
# bicycle = Bicycle()

# car.move()
# bicycle.move()      

import random
class Person:
    def __init__(self, name, number, group):
        self.name = name
        self.__id = random.randint(0, 100)
        self._number = self.number

    def show_info(self):
        print("name: ", self.name)
        print("phone: ", self._number)    


class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group


# st = Student("Ivan", '7777', 'itstep')
# st.show_info()        



class Camera:
    def take_scr(self):
        print("take scr")

    def open_camera(self):
        print("open camera")    

class Phone:
    def call(self):
        print("call phone") 

    def open_camera(self):
        print("open phone")         

class SmartPhone(Phone, Camera):
    def browse(self):
        print("Smart Phone")

# phone = SmartPhone()
# phone.call()
# phone.take_scr()
# phone.browse()
# phone.open_camera()



class Printer:
    def print_document(self):
        print('Документ надруковано.')


class Scanner:
    def scan_document(self):
        print('Документ відскановано.')


class MultiFunctionDevice(Printer, Scanner):
    pass


device = MultiFunctionDevice()

# device.print_document()
# device.scan_document()



# ЗАВДАННЯ 2. ПЕРСОНАЖІ ГРИ 
#
# Створіть клас Character.
#
# Атрибути:
# name — ім'я персонажа.
# health — здоров'я.
#
# Метод:
# show_info().
#
# Створіть клас Warrior(Character).
# Додайте метод attack().
#
# Створіть клас Mage(Character).
# Додайте метод cast_spell().
#
# Створіть клас BattleMage(Warrior, Mage).
#
# Вимоги:
# 1. Створіть об'єкт BattleMage.
# 2. Викличте attack().
# 3. Викличте cast_spell().
# 4. Викличте show_info().
# 5. Виведіть BattleMage.mro().
#
# У Warrior і Mage не потрібно
# перевизначати __init__.

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def show_info(self):
        print(f'Ім’я: {self.name}')
        print(f'Здоров’я: {self.health}')


class Warrior(Character):
    def attack(self):
        print(f'{self.name} атакує мечем!')


class Mage(Character):
    def cast_spell(self):
        print(f'{self.name} використовує магію!')


class BattleMage(Warrior, Mage):
    pass


hero = BattleMage('Артур', 100)

hero.attack()
hero.cast_spell()
hero.show_info()

print(BattleMage.mro())
