# class BankAccount:
#     def __init__(self, owner, balance):
#         self._owner = owner
#         self.__balance = balance

#     @property
#     def balance(self):
#         return self.__balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"поповнення {amount} uah")

#     def show_info(self):
#         print(f"owner: {self._owner}, Balance: {self.__balance}")        



# class PremiumAccount(BankAccount):
#     def __init__(self, owner, balance, cashback):
#         super().__init__(owner, balance) 
#         self.cashback = cashback

#         def show_info(self):
#             super().show_info()
#             print(f"owner: {self._owner}, cashback: {self._cashback}")

#         def show_bonus(self):
#             super().deposit(self._cashback)  
#             print(f"{self._cashback}")  


# account = PremiumAccount('Max', 5000, 5)
# account.deposit(1000)
# account.show_info() 

# print(account.balance)
# account.show_bonus()

# class User:
#     @staticmethod
#     def validate_pass(password):
#         return len(password) >= 8 and any(c.isdigit() for c in password)

# print(User.validate_pass("hello"))


# class Player:
#     total_players = 0
#     def __init__(self, name):
#         self._name = name
#         Player.total_players += 1

#     @classmethod
#     def show_total(cls):
#         print(f"players: " {cls.total_players}) 

# pl = Player("bobby")           




# Завдання 1. Конвертер температур 
 
# Створіть клас TemperatureConverter, який містить два статичні методи:
# - celsius_to_fahrenheit(c) -  перетворює градуси Цельсія у Фаренгейти.
# - fahrenheit_to_celsius(f) - перетворює Фаренгейти у градуси Цельсія.

 
class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9


# print(TemperatureConverter.celsius_to_fahrenheit(25))
# print(TemperatureConverter.fahrenheit_to_celsius(77))



# Додатково: реалізуйте статичний метод is_valid_temperature(c), який перевіряє, чи температура не нижча за −273,15°C.

class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9

    @staticmethod
    def is_valid_temperature(c):
        return c >= -273.15


# print(TemperatureConverter.celsius_to_fahrenheit(25))
# print(TemperatureConverter.fahrenheit_to_celsius(77))

# print(TemperatureConverter.is_valid_temperature(20))
# print(TemperatureConverter.is_valid_temperature(-300))



# class Player:
#     max_health = 100

#     def __init__(self, name, health):
#         self.name = name
#         self.__health = min(self.max_health, max(health, 0))

#         @property
#         def health(self):
#             return self.__health

#         def show_info(self):
#             print(f"name:  {self.name}, health: {self.health}")

#         @staticmethod
#         def is_valid_name(name):
#             return len(name) >= 3

#         @classmethod
#         def create_default(cls, name):
#             return cls(name, cls.max_health)


# name = "q"

# if Player.is_valid_name(name):
#     warrior = Player(name, 300)
#     warrior.show_info()


# class Elf(Player):
#     max_health = 200

#     def attack(self):
#         print(f"elf attack with bowl!")


# class Humen(Player):
#     def attack(self):
#         print(f"elf attack with sword!")

# player1 = Elf("elfius", 200)
# player2 = Humen("Artur", 100)

# for player in (player1, player2):
#     player.show_info()
#     player.attack()




# Завдання 3. Система користувачів 
 
# Створіть клас User.
 
# Атрибути:
# - username — ім'я користувача.
# - __password — приватний пароль.
# - total_users = 0 — лічильник створених користувачів.
# Методи:
# - check_password(password) — перевіряє правильність пароля.
# - @staticmethod validate_password(password) — перевіряє, чи пароль містить щонайменше 8 символів і хоча б одну цифру.
# - @classmethod show_total_users() — виводить кількість створених користувачів.
# Створіть клас Admin(User) з методом delete_user(username), який поки що лише виводить повідомлення про видалення користувача.
 
# Вимоги:
# 1. Створіть двох користувачів.
# 2. Створіть одного адміністратора.
# 3. Перевірте правильний і неправильний пароль.
# 4. Викличте метод адміністратора.
# 5. Виведіть загальну кількість створених об'єктів.
# 6. Використайте super() у конструкторі Admin.
# Підказка: лічильник можна збільшувати через User.total_users += 1 після успішної перевірки пароля.
    

class User:
    total_users = 0

    def __init__(self, username, password):
        if not User.validate_password(password):
            raise ValueError('Пароль має містити мінімум 8 символів і одну цифру.')

        self.username = username
        self.__password = password
        User.total_users += 1

    def check_password(self, password):
        return self.__password == password

    @staticmethod
    def validate_password(password):
        return len(password) >= 8 and any(char.isdigit() for char in password)

    @classmethod
    def show_total_users(cls):
        print(f'Кількість користувачів: {cls.total_users}')


class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def delete_user(self, username):
        print(f'Користувача {username} видалено.')



user1 = User('Ivan', 'password123')
user2 = User('Olena', 'hello1234')

admin = Admin('Admin', 'admin1234')

print(user1.check_password('password123'))
print(user1.check_password('wrong123'))

admin.delete_user('Ivan')

User.show_total_users()   