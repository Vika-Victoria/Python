price = float(input("Введіть вартість однієї приставки: "))
quantity = int(input("Введіть кількість приставок: "))
discount = float(input("Введіть відсоток знижки: "))

print("1. Загальна сума замовлення")
print("2. Вартість однієї приставки зі знижкою")

choice = int(input("Ваш вибір: "))

match choice:
    case 1:
        total = price * quantity
        total = total - (total * discount / 100)
        print("Загальна сума замовлення:", total)

    case 2:
        discounted_price = price - (price * discount / 100)
        print("Вартість однієї приставки зі знижкою:", discounted_price)

    case _:
        print("Невідомий пункт меню")

