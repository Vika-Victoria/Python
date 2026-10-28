#age = int(input("Введіть ваш вік: "))

#if age < 12:
 #   print("Ви дитина")
#elif age < 18:
#    print("Ви підліток")
#elif age < 60:
#    print("Ви доросла людина")
#else:
 #   print("Ви людина похилого віку")


#num1 = 2
#num2 = 4

#operation = "+"

#match operation:
 #   case "+":
  #      print(num1 + num2)

#    case "-":
 #       print(num1 - num2)

  #  case "*":
   #     print(num1 * num2)

    #case "/":
     #   if num2 != 0:
      #      print(num1 / num2)
       # else:
        #    print("На 0 ділити не можна")

#    case _:
#        print("Невідома операція")


print("===== МЕНЮ =====")
print("1. Додати користувача")
print("2. Видалити користувача")
print("3. Показати користувачів")
print("4. Налаштування")
print("0. Вихід")

choice = int(input("Ваш вибір: "))

match choice:
    case 1:
        print("Додавання користувача...")
    case 2:
        print("Видалення користувача...")
    case 3:
        print("Показ користувачів...")
    case 4:
        print("Налаштування...")
    case 0:
        print("Вихід з програми...")
    case _:
        print("Невідомий пункт меню")        