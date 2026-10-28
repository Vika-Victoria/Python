temperature = float(input("Введіть температуру в °C: "))

if temperature < -10:
    print("Дуже холодно")

elif -10 <= temperature < 0:
    print("Холодно")

elif 0 <= temperature < 15:
    print("Прохолодно")

elif 15 <= temperature < 25:
    print("Тепло")

else:
    print("Спекотно")