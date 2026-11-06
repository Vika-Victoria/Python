# file = open('text.txt', 'r', encoding='utf-8')
# text = file.read()
# print(text)
# file.close()

# file = open('text.txt', 'w', encoding='utf-8')
# file.write('new text add')
# file.close()

# students = [
#     'anna',
#     'max',
#     'den'
# ]

# with open('students.txt', 'r+', encoding='utf-8') as f:
#     for student in students:
#         f.write(student + '\n')

#     # st_list = f.readline()
#     # for student in st_list:
#     #     print(student)    

# product = {
#     'name': "iphone18",
#     'price': '1300',
#     'color': 'black'
# }    

# with open('text.txt', 'a', encoding='utf-8') as f:
#     for k, v in product.items():
#         f.write(k + ' ' + v + '\n')

# пошук і заміна інфи в файлі

# def replacrTextFile(fileName, originText, newText):
#     with open(fileName, encoding='utf-8') as f:
#         data = f.read()
#         data = data.replace(originText, newText)

#     with open(fileName, 'w', encoding='utf-8') as f:
#         f.write(data)


# def readFromFile(fileName):
#     with open(fileName, encoding='utf-8') as f:
#         data = f.read()
#         if data:
#             print("info from file")
#             print(data)


# file = 'python_info.txt'

# try:
#     readFromFile(file)
#     replacrTextFile(file, 'python', 'java')
#     readFromFile(file)
# except FileNotFoundError:  
#     print('file not found')

# def wordCounter(fileName):
#     nWords = 0
#     with open(fileName) as file:
#         data = file.read()
#         words = data.split()
#         for word in words:
#             if not word.isnumeric():
#                 nWords += 1
#     return nWords 

# print(wordCounter(file))           

# # дати можливість видаляти конкретний рядок з файла

# def removeLine(fileIn, fileOut, lineNumber):
#     with open(fileIn) as fileR:
#         lines = fileR.readlines()
#         counter = 1
#         with open(fileOut, 'w', encoding='utf-8') as fileW:
#             for line in lines:
#                 if counter !=lineNumber:
#                     fileW.write(line)
#                 counter += 1


# removeLine('students.txt', 'student.txt', 3)



# Завдання 1
# Напишіть програму, яка відкриває файл numbers.txt, читає числа з нього та обчислює їхню суму, потім записує результат у sum.txt. 

# with open('numbers.txt', encoding='utf-8') as file:
#     data = file.read()
#     numbers = data.split()

#     total = 0
#     for number in numbers:
#         total += int(number)

# with open('sum.txt', 'w', encoding='utf-8') as file:
#     file.write(str(total))

# print('Сума чисел:', total)


# Завдання 2
# Напишіть програму, яка запитує у користувача ім'я файлу і слово, потім підраховує кількість входжень цього слова у файлі і виводить результат.

# file_name = input('Введіть імʼя файлу: ')
# word = input('Введіть слово для пошуку: ')

# with open(file_name, encoding='utf-8') as file:
#     data = file.read()

#     count = data.count(word)

# print('Кількість входжень слова:', count)


# Завдання 3
# Напишіть програму, яка копіює вміст файлу data.txt у новий файл backup.txt.

# with open('data.txt', encoding='utf-8') as file:
#     data = file.read()

# with open('backup.txt', 'w', encoding='utf-8') as file:
#     file.write(data)

# print('Файл успішно скопійовано!')


# Завдання 4
# Напишіть програму, яка підраховує кількість рядків у файлі data.txt і виводить результат.

# with open('data.txt', encoding='utf-8') as file:
#     lines = file.readlines()

# print('Кількість рядків:', len(lines))
 

# Завдання 5
# Напишіть програму, яка відкриває файл data.txt, аналізує його вміст і створює звіт summary.txt, у якому вказується кількість рядків, слів і символів у файлі.


with open('data.txt', encoding='utf-8') as file:
    data = file.read()

lines = data.splitlines()
words = data.split()
characters = len(data)

summary = (
    f'Кількість рядків: {len(lines)}\n'
    f'Кількість слів: {len(words)}\n'
    f'Кількість символів: {characters}\n'
)

with open('summary.txt', 'w', encoding='utf-8') as file:
    file.write(summary)

print('Звіт створено!')


# Завдання 6
# Напишіть програму, яка читає вміст файлу data.txt, замінює кожну літеру на наступну в алфавіті (наприклад, a b, z a), а потім записує результат у encrypted.txt.
 
