# Завдання 1. Електронний гаманець
# Створіть клас Wallet, який моделює електронний гаманець користувача.

# Атрибути:
# - owner — ім'я власника.
# - __balance — приватний баланс гаманця.
# Методи:
# - add_money(amount) — поповнює баланс.
# - spend_money(amount) — списує кошти.
# - show_info() — виводить ім'я власника та баланс.
# Вимоги:
# 1. Баланс задається під час створення об'єкта й не може бути від'ємним.
# 2. Не можна поповнювати гаманець на нульову або від'ємну суму.
# 3. Не можна витратити більше коштів, ніж є на балансі.
# 4. Створіть властивість balance через @property тільки для читання.
# 5. При некоректній операції виводьте повідомлення про помилку.
# Приклад перевірки:
# wallet = Wallet("Олександр", 1000)

# wallet.add_money(500)
# wallet.spend_money(300)
# wallet.spend_money(2000)

# wallet.show_info()

# Власник: Олександр
# Баланс: 1200

class Wallet:
    def __init__(self, owner, balance):
        if balance < 0:
            raise ValueError('Початковий баланс не може бути від’ємним.')
        
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance          

    def add_money(self, amount):
        if amount <= 0:
            raise ValueError('Сума поповнення повинна бути більшою за 0.')

        self.__balance += amount
        print(f'Поповнено на {amount} грн.')


    def spend_money(self, amount):
        if amount <= 0:
            raise ValueError('Сума списання повинна бути більшою за 0.')

        if amount > self.__balance:
            raise ValueError('Недостатньо коштів.')

        self.__balance -= amount
        print(f'Списано {amount} грн.')

    def show_info(self):
        print(f'Власник: {self.owner}')
        print(f'Баланс: {self.__balance}') 


wallet = Wallet('Олександр', 1000) 

try:
    wallet.add_money(500)
    wallet.spend_money(300)
    wallet.spend_money(2000)

except ValueError as error:
    print(f'Помилка: {error}')

wallet.show_info()     

# Завдання 2. Система керування товаром 
# Створіть клас Product, який зберігає інформацію про товар у магазині.

# Атрибути:
# - name — назва товару.
# - _price — ціна товару.
# - _quantity — кількість на складі.
# Вимоги:
# 1. Створіть конструктор для ініціалізації всіх атрибутів.
# 2. Реалізуйте властивості price і quantity за допомогою @property та сетерів.
# 3. Ціна не може бути від'ємною.
# 4. Кількість товару не може бути від'ємною та повинна бути цілим числом.
# 5. Метод sell(amount) зменшує кількість товару на складі.
# 6. Метод restock(amount) збільшує кількість товару.
# 7. Метод total_value() повертає загальну вартість усіх одиниць товару на складі.
# Приклад перевірки:
# product = Product("Навушники", 1500, 10)

# product.sell(3)
# product.restock(5)

# print(product.quantity)     # 12
# print(product.total_value()) # 18000

# product.price = -100
# # Помилка: ціна не може бути від'ємною
# У методах sell() та restock() також перевіряйте коректність кількості. Не можна продавати більше товарів, ніж є на складі.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self._price = 0
        self._quantity = 0

        self.price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError('Ціна повинна бути числом.')

        if value < 0:
            raise ValueError('Ціна не може бути від’ємною.')

        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError('Кількість повинна бути цілим числом.')

        if value < 0:
            raise ValueError('Кількість не може бути від’ємною.')

        self._quantity = value

    def sell(self, amount):
        if not isinstance(amount, int) or isinstance(amount, bool):
            raise TypeError('Кількість для продажу повинна бути цілим числом.')

        if amount <= 0:
            raise ValueError('Кількість для продажу повинна бути більшою за 0.')

        if amount > self._quantity:
            raise ValueError('Недостатньо товару на складі.')

        self._quantity -= amount
        print(f'Продано {amount} шт. товару {self.name}.')

    def restock(self, amount):
        if not isinstance(amount, int) or isinstance(amount, bool):
            raise TypeError('Кількість для поповнення повинна бути цілим числом.')

        if amount <= 0:
            raise ValueError('Кількість для поповнення повинна бути більшою за 0.')

        self._quantity += amount
        print(f'Додано {amount} шт. товару {self.name}.')

    def total_value(self):
        return self._price * self._quantity


product = Product('Навушники', 1500, 10)

try:
    product.sell(3)
    product.restock(5)

    print('Кількість:', product.quantity)
    print('Ціна:', product.price)
    print('Загальна вартість:', product.total_value())

    product.price = -100

except (ValueError, TypeError) as error:
    print(f'Помилка: {error}')

try:
    product.quantity = -5
except (ValueError, TypeError) as error:
    print(f'Помилка: {error}')

try:
    product.sell(100)
except (ValueError, TypeError) as error:
    print(f'Помилка: {error}')

try:
    product.restock(2.5)
except (ValueError, TypeError) as error:
    print(f'Помилка: {error}')


# Завдання 3. Система керування персонажем
# Створіть клас GameCharacter для комп'ютерної гри.

# Атрибути:
# - name — ім'я персонажа.
# - __health — приватний рівень здоров'я.
# - __level — приватний рівень персонажа.
# Вимоги:
# 1. При створенні персонажа здоров'я дорівнює 100, рівень — 1.
# 2. Створіть властивості health та level тільки для читання.
# 3. Метод take_damage(amount) зменшує здоров'я.
# 4. Метод heal(amount) відновлює здоров'я.
# 5. Метод level_up() підвищує рівень персонажа на 1.
# 6. Здоров'я повинно залишатися в діапазоні від 0 до 100.
# 7. Шкода та лікування повинні бути додатними числами.
# Приклад перевірки:
# hero = GameCharacter("Knight")

# hero.take_damage(40)
# print(hero.health)  # 60

# hero.heal(20)
# print(hero.health)  # 80

# hero.level_up()
# print(hero.level)   # 2

# hero.take_damage(200)
# print(hero.health)  # 0


class GameCharacter:
    def __init__(self, name):
        self.name = name
        self.__health = 100
        self.__level = 1

    @property
    def health(self):
        return self.__health

    @property
    def level(self):
        return self.__level

    def take_damage(self, amount):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError('Шкода повинна бути числом.')

        if amount <= 0:
            raise ValueError('Шкода повинна бути більшою за 0.')

        self.__health -= amount

        if self.__health < 0:
            self.__health = 0

        print(f'{self.name} отримав шкоду: {amount}.')
        print(f'Здоров’я: {self.__health}')

    def heal(self, amount):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError('Кількість відновлення повинна бути числом.')

        if amount <= 0:
            raise ValueError('Кількість відновлення повинна бути більшою за 0.')

        self.__health += amount

        if self.__health > 100:
            self.__health = 100

        print(f'{self.name} відновив здоров’я на {amount}.')
        print(f'Здоров’я: {self.__health}')

    def level_up(self):
        self.__level += 1
        print(f'{self.name} підвищив рівень до {self.__level}!')


character = GameCharacter('Лицар')

# Отримання шкоди
try:
    character.take_damage(40)
except (ValueError, TypeError) as error:
    print(f'Помилка: {error}')

# Відновлення здоров'я
try:
    character.heal(20)
except (ValueError, TypeError) as error:
    print(f'Помилка: {error}')


character.level_up() # Підвищення рівня

# Отримання великої шкоди
try:
    character.take_damage(200)
except (ValueError, TypeError) as error:
    print(f'Помилка: {error}')


print('Ім’я:', character.name)
print('Здоров’я:', character.health)
print('Рівень:', character.level)