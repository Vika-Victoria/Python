# class User:
#     __slots__ = ("name", "age", "email")

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# user = User("Bob", 20)
# print(user.name)
# print(user.age)
# # print(user.__dict__)
# user.email = "email@email.com"
# user.namee = "ffvv"


# class Worker(User):
#     __slots__ = ('salary',)
#     def __init__(self, name, age, email):
#         super().__init__(name, age)
#         self.email = email

# worker = Worker(name="bob", age=25, email="email@fdff.com")
# worker.salary = 1000
# print(worker.__dict__)   




# Створити клас GameCharacter зі слотами name, health, level 
# Перевірити зміну дозволених атрибутів і спробувати додати новий атрибут weapon.


# class GameCharacter:
#     __slots__ = ('name', 'health', 'level')

#     def __init__(self, name, health, level):
#         self.name = name
#         self.health = health
#         self.level = level


# player = GameCharacter('Warrior', 100, 1)

# player.health = 80
# player.level = 2

# # print(player.name)
# # print(player.health)
# # print(player.level)

# # player.weapon = 'Sword' 




# from dataclasses import dataclass

# @dataclass
# class Product:
#     name: str
#     price: float
#     quantity: int

#     def __post_init__(self):
#         if self.price < 0:
#             raise ValueError("erroe")
#         else:
#             raise ValueError("quantity")

# pr1 = Product(name="pepper", price=10,quantity=2)  
# pr2 = Product(name="pepper2", price=10,quantity=2) 
# print(pr1 == pr2)  



# @dataclass(slots=True)
# class Point:
#     x: int
#     y: int

# point = Point(x=10,y=20)
# print(point)


# @dataclass(frozen=True)
# class Coordinate:
#     lat: float
#     lon: float


# place = Coordinate(48.23, 43.12)
# print(place)    



# Завдання: створити клас Product з використанням @dataclass(slots=True).
 # Поля: name, price, quantity, category.
 # Реалізувати:
# 1. __post_init__() — перевірка ціни та кількості.
# 2. total_price() — загальна вартість товару.
# 3. apply_discount(percent) — застосування знижки від 0 до 100%.
# 4. Створити список із трьох товарів.
# 5. Обчислити загальну вартість товарів на складі.
# має контекстне меню


from dataclasses import dataclass

# @dataclass(slots=True)
# class Product:
#     name: str
#     price: float
#     quantity: int
#     category: str

#     def __post_init__(self):
#         if self.price < 0:
#             raise ValueError('Ціна не може бути від’ємною.')

#         if self.quantity < 0:
#             raise ValueError('Кількість не може бути від’ємною.')

#     def total_price(self):
#         return self.price * self.quantity

#     def apply_discount(self, percent):
#         if not 0 <= percent <= 100:
#             raise ValueError('Знижка має бути від 0 до 100%.')

#         self.price *= (1 - percent / 100)


# products = [
#     Product('Ноутбук', 30000, 5, 'Техніка'),
#     Product('Мишка', 800, 10, 'Аксесуари'),
#     Product('Клавіатура', 1500, 7, 'Аксесуари')
# ]

# products[0].apply_discount(10)

# for product in products:
#     print(product)
#     print('Вартість на складі:', product.total_price())
#     print()

# total = sum(product.total_price() for product in products)

# print(f'Загальна вартість складу: {total} грн')



class Car:
    pass

# car = Car()
# print(type(car))
# print(type(Car))



# Car = type(
#     'Car',
#     (),
#     {
#         'model':'bmw',
#         'year':2020,
#         'show_info':
#         lambda self:print(self.model),
#     }
# )

# new_car = Car()
# print(new_car.model)
# new_car.show_info()


# class CategoryMeta(type):
#     def __new__(cls, name, bases, attrs):
#         if name != 'BaseCar':
#             if 'category' not in attrs:
#                 raise AttributeError("category")
#         return super().__new__(name, bases, attrs)


# class BaseCar(metaclasss=CategoryMeta()):
#     pass

# class SportCar(BaseCar):
#     category = 'sport'


# class OffroadCar(BaseCar):
#     category = 'offroad'

# print(SportCar.category)
# print(OffroadCar.category)

# from abc import ABC, abstractmethod

# class Payment:
#     registry = {}

#     def __init_subclass__(cls, **kwargs):
#         super().__init_subclass__(**kwargs)
#         Payment.registry[cls.__new__] = cls

#     @abstractmethod
#     def pay(self, amount):
#         pass       

# class CardPayment(Payment):
#     def pay(self, amount):
#         print("pay card")

# class CriptoPayment(Payment):
#     def pay(self, amount):
#         print("pay cripto")        

# print(Payment.registry)
# card1 = CardPayment()
# card1.pay(120)



# Створіть абстрактний клас Delivery, який має:
# Атрибут address.
# Абстрактний метод calculate_cost(distance).
# Звичайний метод show_address(), який виводить адресу доставки.
# Створіть три дочірні класи:
# CarDelivery — вартість 20 грн за кілометр.
# BikeDelivery — вартість 10 грн за кілометр.

from abc import ABC, abstractmethod


class Delivery(ABC):
    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculate_cost(self, distance):
        pass

    def show_address(self):
        print(f'Адреса доставки: {self.address}')


class CarDelivery(Delivery):
    def calculate_cost(self, distance):
        return distance * 20


class BikeDelivery(Delivery):
    def calculate_cost(self, distance):
        return distance * 10


car = CarDelivery('Київ, вул. Хрещатик')
bike = BikeDelivery('Київ, вул. Саксаганського')

car.show_address()
print('Вартість доставки:', car.calculate_cost(10), 'грн')

bike.show_address()
print('Вартість доставки:', bike.calculate_cost(10), 'грн')

