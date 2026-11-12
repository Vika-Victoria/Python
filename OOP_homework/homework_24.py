# Завдання 1. Створення класу Car
# Створіть клас Car, який описує автомобіль.
# Атрибути:
# - brand — марка автомобіля.
# - model — модель автомобіля.
# - __mileage — приватний пробіг автомобіля.
# - total_cars = 0 — атрибут класу, який зберігає кількість створених автомобілів.
# Методи:
# - show_info() — виводить марку, модель та пробіг.
# - drive(km) — збільшує пробіг на вказану кількість кілометрів.
# - @property mileage — дозволяє отримати поточний пробіг.
# - @staticmethod validate_mileage(km) — перевіряє, чи передане значення більше
# нуля.
# - @classmethod show_total_cars() — виводить кількість створених автомобілів.
# Перевірка: створіть два автомобілі, збільште пробіг одного на 150 км та виведіть загальну
# кількість автомобілів.

class Car:
    total_cars = 0

    def __init__(self, brand, model, mileage):
        if not self.validate_mileage(mileage):
            raise ValueError('Пробіг не може бути від’ємним або нульовим.')
        
        self.brand = brand
        self.model = model
        self.__mileage = mileage
        Car.total_cars += 1

    def show_info(self):
        print(f"Марка автомобілю: {self.brand}") 
        print(f"Модель автомобілю: {self.model}")
        print(f"Пробіг автомобілю: {self.__mileage} км")

    def drive(self, km):
        if not self.validate_mileage(km):
            raise ValueError('Кількість кілометрів має бути більше нуля.')
        
        self.__mileage += km

    @property
    def mileage(self):
        return self.__mileage

    @staticmethod
    def validate_mileage(km):
        return isinstance(km, (int, float)) and km > 0

    @classmethod
    def show_total_cars(cls):
        print(f'Кількість автомобілів: {cls.total_cars}')

    @classmethod
    def from_string(cls, text):
        brand, model, mileage = text.split(',')
        return cls(brand, model, int(mileage))



car1 = Car('Toyota', 'Camry', 50000)
car2 = Car('BMW', 'X5', 30000)

car1.drive(150)

car1.show_info()
print(f'Поточний пробіг: {car1.mileage} км')

Car.show_total_cars()

# Завдання 2.
# Створіть дочірній клас ElectricCar(Car).
# Додайте:
# - battery — заряд батареї у відсотках (від 0 до 100).
# - charge(amount) — збільшує заряд батареї, але не більше 100%.
# - Перевизначте show_info(), щоб додатково виводився заряд батареї.
# - Використайте super() для виклику конструктора та методу базового класу.
# Перевірка: створіть електромобіль із зарядом 60%, зарядіть його на 30%, виведіть
# інформацію. Спробуйте зарядити ще на 50% і перевірте, що заряд не перевищує 100%.

class ElectricCar(Car):
    def __init__(self, brand, model, mileage, battery):
        super().__init__(brand, model, mileage)
        self.battery = battery

    def charge(self, amount):
        self.battery += amount

        if self.battery > 100:
            self.battery = 100

    def drive(self, km):
        if not self.validate_mileage(km):
            raise ValueError('Відстань має бути більше нуля.')

        max_distance = self.battery * 5

        if km > max_distance:
            raise ValueError('Недостатньо заряду батареї.')
        
        super().drive(km) 

        self.battery -= (km + 4) // 5      

    def show_info(self):
        super().show_info()
        print(f'Заряд батареї: {self.battery}%')

      

tesla = ElectricCar('Tesla', 'Model 3', 20000, 60)

tesla.charge(30)
tesla.show_info()

tesla.charge(50)
tesla.show_info()                



# Завдання 3.
# Додайте до класу Car метод класу:
# @classmethod from_string(cls, text)
# Він повинен створювати автомобіль із рядка формату:
# "BMW,320,50000"
# Де BMW — марка, 320 — модель, 50000 — початковий пробіг.
# Приклад очікуваного використання:
# car = Car.from_string("BMW,320,50000") car.show_info()
# Перевірте, що створений таким способом автомобіль також враховується в total_cars.


# Створення автомобіля з рядка
car = Car.from_string("BMW,320,50000")

car.show_info()
Car.show_total_cars()


# Додаткове завдання
# Додайте до класу ElectricCar метод drive(km), який:
# - Збільшує пробіг автомобіля.
# - Зменшує заряд батареї на 1% за кожні 5 км.
# - Не дозволяє проїхати більшу відстань, ніж дозволяє поточний заряд.
# - Не допускає від'ємного заряду батареї.
# Наприклад, якщо заряд становить 20%, автомобіль може проїхати максимум 100 км

tesla = ElectricCar('Tesla', 'Model 3', 20000, 20)

tesla.drive(50)
tesla.show_info()
