file_size = float(input("Введіть розмір файлу в ГБ: "))
speed = float(input("Введіть швидкість інтернету в біт/с: "))

print("1. Час у годинах")
print("2. Час у хвилинах")
print("3. Час у секундах")

choice = int(input("Ваш вибір: "))

file_bits = file_size * 8 * 1024 ** 3
seconds = file_bits / speed

match choice:
    case 1:
        print("Файл завантажиться за", seconds / 3600, "годин")

    case 2:
        print("Файл завантажиться за", seconds / 60, "хвилин")

    case 3:
        print("Файл завантажиться за", seconds, "секунд")

    case _:
        print("Невідомий пункт меню")