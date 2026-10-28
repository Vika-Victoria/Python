# count = 10

# while count > 0:
#     print(count)
#     count -= 1


# start = int(input("Введіть перше число: "))
# end = int(input("Введіть друге число: "))

# i = start

# while i <= end:
#     print(i, end=" ")
#     i += 1  


# start = int(input("Введіть перше число: "))
# end = int(input("Введіть друге число: "))

# i = start

# while i <= end:
#     if i % 2 != 0:
#         print(i, end=" ")
#     i += 1


# total_sum = 0 
# i = 1
# while i <= 3:
#     num = int(input("enter"))
#     total_sum += i
#     i += 1

#     print(total_sum)



# password = "" 

# while password != "admin":
#     password = input("enter password: ")

#     print("ok")


# password = "" 

# while password != "admin":
#     password = input("enter password: ")

#     print("ok")

# num = int(input("enter a number: "))

# while num != 0:
#     print(f"num: {num}")
#     total += num
#     num = int(input("enter a number: "))

#     print(f"total: {total}")


#1 Сума 1 + 2 + ... + n
# n = int(input("Введіть n: "))

# i = 1
# sum = 0

# while i <= n:
#     sum += i
#     i += 1

# print("Сума:", sum)

# 2. Добуток 1 × 2 × ... × n

# n = int(input("Введіть n: "))

# i = 1
# product = 1

# while i <= n:
#     product *= i
#     i += 1

# print("Добуток:", product)


# 3. Кількість введених чисел до 0

# count = 0

# number = int(input("Введіть число: "))

# while number != 0:
#     count += 1
#     number = int(input("Введіть число: "))

# print("Кількість чисел:", count)



# 5. Вивести цифри у зворотному порядку.

number = int(input("Введіть число: "))

while number > 0:
    print(number % 10, end="")
    number //= 10



# 4. Користувач вводить цілі числа з клавіатури. Введення продовжується доти, доки користувач не введе 0.
# Програма повинна окремо порахувати:
# кількість додатних чисел;
# кількість від’ємних чисел.
# Число 0 не враховується.    

positive = 0
negative = 0

number = int(input("Введіть число: "))

while number != 0:
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1

    number = int(input("Введіть число: "))

print("Додатних чисел:", positive)
print("Від'ємних чисел:", negative)