# Завдання 1
# Створіть клас Airplane (Літак). За допомогою перевантаження операторів, реалі­зуйте: 

# перевірку на рівність типів літаків (операція = =); 
# збільшення та зменшення пасажирів у салоні літака (операції +, -, +=, -=);
# порівняння двох літаків за максимально можливою кількістю пасажирів на борту (операції >, <, <=, >=).



class Airplane:
    def __init__(self, plane_type, passengers, max_passengers):
        self.plane_type = plane_type
        self.passengers = passengers
        self.max_passengers = max_passengers

    def __eq__(self, other):
        return self.plane_type == other.plane_type

    def __add__(self, count):
        self.passengers += count
        return self

    def __sub__(self, count):
        self.passengers -= count
        return self

    def __iadd__(self, count):
        self.passengers += count
        return self

    def __isub__(self, count):
        self.passengers -= count
        return self

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def show_info(self):
        print(f'Тип літака: {self.plane_type}')
        print(f'Пасажирів: {self.passengers}')
        print(f'Максимум пасажирів: {self.max_passengers}')


plane1 = Airplane('Boeing', 100, 200)
plane2 = Airplane('Airbus', 150, 250)
plane3 = Airplane('Boeing', 80, 180)

print(plane1 == plane2)  # False
print(plane1 == plane3)  # True

plane1 + 20
plane1 - 10

plane2 += 30
plane2 -= 10

print(plane1 > plane2)
print(plane1 < plane2)
print(plane1 <= plane2)
print(plane1 >= plane2)

plane1.show_info()
plane2.show_info()




# авдання 2
# Створіть клас Flat (Квартира). Реалізуйте перевантажені оператори: 

# перевірку на рівність площ квартир (операція ==);
# перевірку на нерівність площ квартир (операція !=);
# порівняння двох квартир за ціною (операції >, <, <=, >=).

class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    # рівность площ
    def __eq__(self, other):
        return self.area == other.area

    #  нерівность площ
    def __ne__(self, other):
        return self.area != other.area

    # порівняння за ціною
    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price



flat1 = Flat(50, 50000)
flat2 = Flat(70, 70000)
flat3 = Flat(50, 60000)

# порівняння площ
print(flat1 == flat2)  # False
print(flat1 != flat3)  # False

# порівняння цін
print(flat1 > flat2)   # False
print(flat1 < flat2)   # True
print(flat1 <= flat3)  # True
print(flat2 >= flat3)  # True





# Завдання 3
# Створіть базовий клас Shape для рисування плоских фігур. Визначте методи: 
# Show() — виведення на екран інформації про фігуру;
# Save() — збереження фігури у файл;
# Load() — зчитування фігури з файлу.
# Визначте похідні класи: 
# Square — квадрат із заданими з координатами лівого верхнього кута та дов­жи­ною сторони.
# Rectangle — прямокутник із заданими координатами верхнього лівого кута та розмірами.
# Circle — коло із заданими координатами центру та радіусом.
# Ellipse — еліпс із заданими координатами верхнього кута описаного навколо нього прямокутника зі сторонами, паралельними осям координат, та розмірами цього прямокутника. 
# Створіть список фігур, збережіть фігури у файл, завантажте в інший список та відобразіть інформацію про кожну фігуру.


import json


class Shape:
    def show(self):
        pass

    def save(self, file):
        data = {
            'type': self.__class__.__name__,
            'coordinates': self.coordinates
        }
        file.write(json.dumps(data) + '\n')

    @staticmethod
    def load(file):
        shapes = []

        for line in file:
            data = json.loads(line)
            shape_type = data['type']
            coordinates = data['coordinates']

            if shape_type == 'Square':
                shapes.append(Square(*coordinates))
            elif shape_type == 'Rectangle':
                shapes.append(Rectangle(*coordinates))
            elif shape_type == 'Circle':
                shapes.append(Circle(*coordinates))
            elif shape_type == 'Ellipse':
                shapes.append(Ellipse(*coordinates))

        return shapes


class Square(Shape):
    def __init__(self, x, y, side):
        self.coordinates = [x, y, side]

    def show(self):
        print(f'Квадрат: x={self.coordinates[0]}, '
              f'y={self.coordinates[1]}, сторона={self.coordinates[2]}')


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.coordinates = [x, y, width, height]

    def show(self):
        print(f'Прямокутник: x={self.coordinates[0]}, '
              f'y={self.coordinates[1]}, ширина={self.coordinates[2]}, '
              f'висота={self.coordinates[3]}')


class Circle(Shape):
    def __init__(self, x, y, radius):
        self.coordinates = [x, y, radius]

    def show(self):
        print(f'Коло: центр=({self.coordinates[0]}, {self.coordinates[1]}), '
              f'радіус={self.coordinates[2]}')


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.coordinates = [x, y, width, height]

    def show(self):
        print(f'Еліпс: x={self.coordinates[0]}, y={self.coordinates[1]}, '
              f'ширина={self.coordinates[2]}, висота={self.coordinates[3]}')


shapes = [
    Square(10, 20, 5),
    Rectangle(15, 25, 10, 6),
    Circle(30, 40, 8),
    Ellipse(5, 10, 12, 7)
]

# збереження у файл
with open('shapes.txt', 'w', encoding='utf-8') as file:
    for shape in shapes:
        shape.save(file)

# завантаження з файлу
with open('shapes.txt', 'r', encoding='utf-8') as file:
    loaded_shapes = Shape.load(file)

# виведення інформації
for shape in loaded_shapes:
    shape.show()