# Завдання 1
# Створіть клас Device, який містить інформацію про пристрій.

# За допомогою механізму успадкування реалізуйте клас CoffeeMachine (містить інформацію про кавомашину), 
# клас Blender (містить інформацію про блендер), клас MeatGrinder (містить інформацію про м'ясорубку).

# Кожен із класів має містити необхідні для роботи методи.

class Device:
    def __init__(self, name, brand, power):
        self.name = name
        self.brand = brand
        self.power = power

    def show_info(self):
        print(f'Назва: {self.name}')
        print(f'Виробник: {self.brand}')
        print(f'Потужність: {self.power} Вт')


class CoffeeMachine(Device):
    def make_coffee(self):
        print('Кавомашина готує каву.')


class Blender(Device):
    def blend(self):
        print('Блендер подрібнює продукти.')


class MeatGrinder(Device):
    def grind_meat(self):
        print('М’ясорубка перемелює м’ясо.')



coffee = CoffeeMachine('Кавомашина', 'Philips', 1500)
blender = Blender('Блендер', 'Bosch', 800)
grinder = MeatGrinder('М’ясорубка', 'Moulinex', 1200)

coffee.show_info()
coffee.make_coffee()


blender.show_info()
blender.blend()

grinder.show_info()
grinder.grind_meat()


# Завдання 2
# Створіть клас Ship, який містить інформацію про кораблі. За допомогою механізму успадкування реалізуйте клас Frigate 
# (містить інформацію про фрегат), клас Destroyer (містить інформацію про есмінця), клас Cruiser (містить інформацію про крейсер).

# Кожен із класів має містити необхідні для роботи методи.


class Ship:
    def __init__(self, name, country, speed):
        self.name = name
        self.country = country
        self.speed = speed

    def show_info(self):
        print(f'Назва: {self.name}')
        print(f'Країна: {self.country}')
        print(f'Швидкість: {self.speed} вузлів')


class Frigate(Ship):
    def patrol(self):
        print('Фрегат патрулює територію.')


class Destroyer(Ship):
    def attack(self):
        print('Есмінець виконує бойове завдання.')


class Cruiser(Ship):
    def launch_missile(self):
        print('Крейсер запускає ракету.')



frigate = Frigate('Гетьман Сагайдачний', 'Україна', 30)
destroyer = Destroyer('Arleigh Burke', 'США', 32)
cruiser = Cruiser('Аврора', 'США', 30)

frigate.show_info()
frigate.patrol()


destroyer.show_info()
destroyer.attack()

cruiser.show_info()
cruiser.launch_missile()


# Завдання 3
# Запрограмуйте клас Money (об'єкт класу оперує однією валютою) для роботи з грошима. 

# У класі мають бути передбачені: поле для зберігання цілої частини грошей (долари, євро, гривні тощо) і поле для зберігання копійок 
# (центи, євроценти, копійки тощо).

# Реалізуйте методи виведення суми на екран, задання значень частин. 

# Створіть клас Product для роботи з продуктом або товаром беручи за основу клас Money. Реалізуйте метод для зменшення ціни на задане число.

# Для кожного з класів реалізуйте необхідні методи та поля.


class Money:
    def __init__(self, whole, cents):
        self.whole = whole
        self.cents = cents

    def show_amount(self):
        print(f'{self.whole} грн {self.cents} коп.')

    def set_amount(self, whole, cents):
        self.whole = whole
        self.cents = cents


class Product(Money):
    def __init__(self, name, whole, cents):
        super().__init__(whole, cents)
        self.name = name

    def show_product(self):
        print(f'Товар: {self.name}')
        self.show_amount()

    def reduce_price(self, amount):
        total = self.whole * 100 + self.cents
        total -= amount * 100

        if total < 0:
            print('Помилка: ціна не може бути від’ємною.')
            return

        self.whole = total // 100
        self.cents = total % 100

        print(f'Ціну зменшено на {amount} грн.')



money = Money(100, 50)
money.show_amount()

product = Product('Навушники', 1500, 50)

product.show_product()

product.reduce_price(200)

product.show_product()


# Завдання 4
# Використовуючи механізм множинного успадкування, розробіть клас "Людина". Мають бути класи "Мозок", "Серце", "Ноги" і т.д.


class Brain:
    def think(self):
        print('Людина думає.')


class Heart:
    def beat(self):
        print('Серце б’ється.')


class Legs:
    def walk(self):
        print('Людина ходить.')


class Arms:
    def move_arms(self):
        print('Людина рухає руками.')


class Human(Brain, Heart, Legs, Arms):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f'Ім’я: {self.name}')
        print(f'Вік: {self.age}')



person = Human('Олександр', 25)

person.show_info()
person.think()
person.beat()
person.walk()
person.move_arms()


# Завдання 5
# 1 Створіть базовий клас Instrument, який представлятиме загальні властивості та методи для всіх музичних інструментів.
# Визначте метод play, який має бути реалізований у підкласах.
# 2 Створіть підкласи StringInstrument, WindInstrument і PercussionInstrument, які представляють струнні, духові та ударні інструменти відповідно.
# Кожен із цих класів повинен успадковувати від Instrument та надавати свою реалізацію методу play.
# 3 Створіть додаткові підкласи для конкретних музичних інструментів, таких як Guitar, Flute та Drum.
# Ці класи повинні успадковувати від відповідних підкласів (StringInstrument, WindInstrument, або PercussionInstrument) та
# можуть додатково визначати свої унікальні методи та властивості, наприклад, метод tune для налаштування гітари.
# 4 Створіть екземпляри різних музичних інструментів та викличте метод play для кожного з них, щоб побачити,
# як кожний інструмент звучить.
# 5 Реалізуйте множинне спадкування, щоб створити новий клас HybridInstrument, який успадковує від кількох класів,
# які представляють різні види музичних інструментів. У цьому класі визначте свій метод play, що комбінує звуки від усіх успадкованих класів.
# 6 Створіть екземпляр HybridInstrument і викличте його метод play, щоб побачити, як множинне успадкування дозволяє комбінувати властивості та методи з кількох батьківських класів.


class Instrument:
    def play(self):
        pass


class StringInstrument(Instrument):
    def play(self):
        print('Грає струнний інструмент.')


class WindInstrument(Instrument):
    def play(self):
        print('Грає духовий інструмент.')


class PercussionInstrument(Instrument):
    def play(self):
        print('Грає ударний інструмент.')


class Guitar(StringInstrument):
    def tune(self):
        print('Гітару налаштовано.')


class Flute(WindInstrument):
    pass


class Drum(PercussionInstrument):
    pass


class HybridInstrument(StringInstrument, WindInstrument):
    def play(self):
        print('Гітара грає...')
        print('Флейта грає...')
        print('Комбіноване звучання!')


guitar = Guitar()
flute = Flute()
drum = Drum()
hybrid = HybridInstrument()

guitar.play()
guitar.tune()

flute.play()
drum.play()

hybrid.play()