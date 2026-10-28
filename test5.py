hour = int(input("Введіть кількість годин: "))

if 0 <= hour < 6:
    print("Good Night")

elif 6 <= hour < 13:
    print("Good Morning")

elif 13 <= hour < 17:
    print("Good Day")

elif 17 <= hour < 24:
    print("Good Evening")

else:
    print("Некоректне значення")