# 1.Використовуючи функцію map, перетворіть список рядків на список їх довжин. Вихідний список:
# ["apple", "banana", "cherry"].

# fruits = ["apple", "banana", "cherry"]

# lengths = list(map(lambda fruit: len(fruit), fruits))

# print(lengths)



# 2.Використовуючи функцію filter, відфільтруйте список рядків, залишивши лише рядки, що
# починаються з літери "a". Вихідний список: ["apple", "banana", "cherry"].

# fruits = ["apple", "banana", "cherry"]

# result = list(filter(lambda fruit: fruit.startswith("a"), fruits))

# print(result)


# 3.Використовуючи функції map і filter, створіть новий список, у якому залишаться лише числа, що
# поділяються на 3. Вихідний список: [1, 2, 3, 4, 5].

# numbers = [1, 2, 3, 4, 5]

# result = list(map(lambda x: x*1, filter(lambda x: x % 3 == 0, numbers)))

# print(result)


# 4.Використовуючи функцію zip, об'єднайте два списки чисел до списку пар чисел. Вихідні списки:
# [1, 2, 3] та [4, 5, 6].

# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]

# result = list(zip(numbers1, numbers2))

# print(result)


# 5.Використовуючи функцію map, перетворіть два списки чисел на список їх творів. Вихідні списки:
# [1, 2, 3] та [4, 5, 6].


# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]

# result = list(map(lambda x, y: x * y, numbers1, numbers2))

# print(result)


# 6.Використовуючи функцію filter, відфільтруйте список пар чисел, залишивши лише пари, в яких
# перше число більше за друге.

# numbers = [(1, 2), (3, 1), (4, 4), (5, 3)]

# result = list(filter(lambda number: number[0] > number[1], numbers))

# print(result)


# 7.Даний список чисел, відфільтрувати тільки позитивні

# numbers = [1, -2, 3, 4, 5, -10, 10, 0]

# result = list(filter(lambda number: number > 0, numbers))

# print(result)


# 8.Даний список чисел, відфільтрувати числа в діапазоні вказаним користувачем

# numbers = [1, 5, 8, 12, 15, 20, 25, 30]

# start = int(input("Введіть початок діапазону: "))
# end = int(input("Введіть кінець діапазону: "))

# result = list(filter(lambda number: start <= number <= end, numbers))

# print(result)


# 9.Даний список чисел, відфільтрувати всі цілі значення


# numbers = [1, 2.5, 3, 4.7, 5.0, 6.2, 8]

# result = list(filter(lambda x: type(x) == int, numbers))

# print(result)


# 10.Даний список логінів користувачів, додайте кожному логіну приставку "$"

# logins = ["anna", "ivan", "olena", "maksym"]

# result = list(map(lambda login: "$" + login, logins))

# print(result)


# 11.На основі трьох списків різних значень, сформувати список, елемент якого містить набір із
# елементів інших списків

list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
list3 = [True, False, True]

result = list(zip(list1, list2, list3))

print(result)