# student = {
#     "name": "vika",
#     "mail": "fdg@gmail.com"
# }

# print(type(student))

# for value in student:
#     print(value, student[value])


# user = {}

# user['name'] = "Anna"
# user['age'] = 100

# print(user)


# nums = dict([(1, 1), (2, 2)])
# print(nums)

# product = {
#     "name": "Iphone 18 pro",
#     "price": 1400
#     }
# name = product.get('name') 
# # name2 = product['name']
# # print(name2)

# del_item = product.popitem()
# print(del_item)

# if 'price' in product:
#     del product['price']

# product['description']  = "some text" 
# product.update([('price', 800), ('date', '19.10.2026')])

# print(product)

# for key, value in product.item():
#     print(key, value)


# Створіть програму, яка працює з інформацією про користувача.
# Створіть словник profile з полями name, age, city, email.
# Виведіть ім'я та місто користувача.
# Запитайте нове місто через input() і оновіть словник.
# Додайте ключ phone.
# Перевірте, чи є ключ email.
# Видаліть email за допомогою pop().
# Виведіть оновлений словник.

# 1
# profile = {
#     "name": "Вероніка",
#     "age": 30,
#     "city": "Київ",
#     "email": "user@gmail.com"
# }

# # 2 
# print("Ім'я:", profile["name"])
# print("Місто:", profile["city"])

# # 3 
# new_city = input("Введіть нове місто: ")
# profile["city"] = new_city

# # 4 
# profile["phone"] = "+380991234567"

# # 5
# if "email" in profile:
#     print("Ключ email існує")
# else:
#     print("Ключ email відсутній")

# # 6
# profile.pop("email")

# # 7
# print("Оновлений профіль:", profile)




player = {
    'name':'King',
    'level':1,
    'gold':100,
    'stats':{
        'hp':100,
        'attack':20,
        'defence':10,
        'max_hp':100,

    },
    'inventary':[
        {'name':'sword', 'damage':15, 'heal':0},
        {'name':'potion', 'damage':0, 'heal':30}
    ]
}

shop = {
    '1': {
        'name': "potion",
        'price': 30,
        'heal': 30
    },
    '2': {
        'name': 'shield',
        'price': 50,
        'defence': 15
    }
}


enemy = {
    'name':'goblin',
    'stats':{
        'hp':60,
        'attack':15,
        'defence':10,
        'max_hp':100,

    },
    'reward':{
        'gold':40,
        'experience':20
        }
}

def show_inventary():
    print("/n ==== Inventary ====")
    for index, item in enumerate(player['inventary'], 1):
        print(f"{index}, {item['name']}")

def use_potion():
    for item in player['inventary']:
        if item['name'] == 'potion':
            hp = player['stats']['hp']
            max_hp = player['stats']['max_hp']
            player['stats']['hp'] = min(hp + item['heal'], max_hp)
            player['inventary'].remove(item)
            print("Potion used")
            print("HP:", player['stats']['hp'])
            return

    print("No potion in inventary")


print("\n === SHOP ===")

for key, item in shop.items():
    print(key, item['name'], ' - ', item['price'], 'gold')

choice = input("choice product - ") 
if choice in shop:
    item = shop[choice]
    print(item)
    if player['gold'] >= item['price']:
        player['gold'] -= item['price']

        new_item =item.copy()
        new_item.pop('price')
        player['inventary'].append(new_item)
        print("item bought!")

    else:
        print("not enough gold!")       

show_inventary()



print('\ you attack with', enemy['name'])

while (player['stats']['hp'] > 0 and enemy['stats']['hp'] > 0):
    damage = max(1, player['stats']['attack'] - enemy['stats'['defense']])
    enemy['stats']['hp'] -= damage

    print("your damage, ", damage)

    if enemy['stats']['hp'] < 0:
        print("winnn!")
        player['gold'] += enemy['reward']['gold']
        break

    enemy_damage = max(1, enemy['stats']['atack'] - player['stats']['defense'])
    player['stats']['hp'] -= enemy_damage

    print("enemy damage: ", enemy_damage)
    
