# Завдання 1. Працівники компанії
# Створіть абстрактний клас Employee.
# Атрибути: name, salary
# Абстрактний метод: work()
# Звичайний метод: show_info()
# Створіть класи:
# Programmer
# Designer
# Manager
# Реалізуйте work():
# Programmer пише код.
# Designer створює дизайн.
# Manager керує командою.
# Додатково додайте абстрактний метод:
# calculate_bonus()

# Наприклад:
# Programmer — 15% зарплати;
# Designer — 10%;
# Manager — 20%.

from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def calculate_bonus(self):
        pass

    def show_info(self):
        print(f'Ім’я: {self.name}')
        print(f'Зарплата: {self.salary} грн')
        print(f'Премія: {self.calculate_bonus()} грн')


class Programmer(Employee):
    def work(self):
        print('Пише код.')

    def calculate_bonus(self):
        return self.salary * 0.15


class Designer(Employee):
    def work(self):
        print('Створює дизайн.')

    def calculate_bonus(self):
        return self.salary * 0.10


class Manager(Employee):
    def work(self):
        print('Керує командою.')

    def calculate_bonus(self):
        return self.salary * 0.20


employees = [
    Programmer('Олександр', 50000),
    Designer('Марія', 40000),
    Manager('Андрій', 60000)
]

for employee in employees:
    employee.show_info()
    employee.work()
    print()



# Завдання 2 (Додаткове) : Реалізація системи перевірки правил для класів за допомогою метакласів
# Опис завдання:

# Вам потрібно створити систему, яка забезпечує автоматичну перевірку, чи відповідають створені класи певним вимогам. 
# Для цього потрібно використовувати метакласи.

# Вимоги до завдання:

# Створіть метаклас ValidationMeta:

# Перевіряйте, чи всі методи класу починаються зі слова do_ (наприклад, do_task, do_something_else).
# Перевіряйте, чи є в класі атрибут description, і чи є він рядком.

# Створіть базовий клас ValidatedClass:
# Визначте цей клас із використанням метакласу ValidationMeta.
# Створіть кілька класів, які наслідують ValidatedClass:

# Один клас повинен відповідати всім правилам.
# Інший клас має порушувати одне з правил (наприклад, методи не починаються з do_ або відсутній атрибут description).
# Додайте виключення:

# Якщо клас порушує правила метакласу, має бути викликана помилка ValueError із поясненням, що саме не відповідає вимогам.
# Реалізуйте програму, яка створює об'єкти цих класів:

# У програмі виведіть інформацію про те, чи успішно створено кожен клас, або ж, якщо є помилка, виведіть її текст.
# Додаткові вимоги:

# Використовуйте модуль abc для визначення базового класу.
# Додайте можливість автоматичного створення відсутнього атрибуту description з дефолтним значенням, якщо його немає.


from abc import ABC, ABCMeta


class ValidationMeta(ABCMeta):
    def __new__(mcs, name, bases, attrs):

        if 'description' not in attrs:
            attrs['description'] = 'Опис відсутній'

        if not isinstance(attrs['description'], str):
            raise ValueError(
                f"Клас {name}: атрибут description повинен бути рядком"
            )

        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and not attr_name.startswith('do_'):
                if not attr_name.startswith('__'):
                    raise ValueError(
                        f"Клас {name}: метод '{attr_name}' "
                        f"повинен починатися з do_"
                    )

        return super().__new__(mcs, name, bases, attrs)


class ValidatedClass(ABC, metaclass=ValidationMeta):
    @abstractmethod
    def do_task(self):
        pass


# клас відповідає всім правилам
class GoodClass(ValidatedClass):
    description = 'Клас для виконання завдань'

    def do_task(self):
        print('Виконую завдання')

    def do_something(self):
        print('Виконую іншу дію')


# клас порушує правило назви методу
try:
    class BadClass(ValidatedClass):
        description = 'Некоректний клас'

        def task(self):
            print('Завдання')
except ValueError as error:
    print(error)


class DefaultDescriptionClass(ValidatedClass):
    def do_task(self):
        print('Виконую завдання')


try:
    obj1 = GoodClass()
    print('GoodClass успішно створено')
    print(obj1.description)

    obj2 = DefaultDescriptionClass()
    print('DefaultDescriptionClass успішно створено')
    print(obj2.description)

except ValueError as error:
    print(error)



