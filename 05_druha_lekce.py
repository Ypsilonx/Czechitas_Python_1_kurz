# sales = {
#     "A": 4165,
#     "B": 5681,
#     "C": 2565,
# }

# str - řetězec
# int - číslo
# float - destinné číslo
# list - seznam
# dict - slovník
# bool - pravdivost
# tuple - dvojička

# for book in sales.values():
#     print(book)

# for book in sales:
#     print(book)

# for book in sales.items():
#     print(book)
    
# for key, value in sales.items():
#     print(f'Klíč {key} -- {value}.')

# slovnik = {1: 'a', 2: 'b',3: 'c'}

# for item in 'Andrea':
#     print(item)

# stop = int(input("Zadej konec: "))
# for i in range(stop):
#     print(i)

# start = int(input("Zadej začátek: "))
# stop = int(input("Zadej konec: "))
# for i in range(start, stop):
#     print(i)

# start = int(input("Zadej začátek: "))
# stop = int(input("Zadej konec: "))
# for i in range(start, stop):
#     if i % 3 == 0:
#         print(i)

# number_of_guests = int(input("Zadej počet hostů: "))
# guest_list = []
# for i in range(number_of_guests):
#     new_guest = input("Zadej jméno hosta: ")
#     guest_list.append(new_guest)
# print(guest_list)

# list_of_items = [
#     {"title": "Modrá kravata", "price": 239, "in_stock": True},
#     {"title": "Luxusní psací pero", "price": 1599, "in_stock": True},
#     {"title": "Degustační balíček kávy", "price": 599, "in_stock": True},
#     {"title": "Parfém", "price": 559, "in_stock": False},
#     {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True},
#     {"title": "Sklenice na víno", "price": 799, "in_stock": True},
#     {"title": "Fitness náramek", "price": 2399, "in_stock": False},
# ]

# for item in list_of_items:
#     if 500 <= item["price"] <= 1000 and item["in_stock"]:
#         print(f"Vybraný dárek je {item['title']}")
#         break

purchase_list = [
    {"person": "Petr", "item": "Prací prášek", "value": 399},
    {"person": "Ondra", "item": "Savo", "value": 80},
    {"person": "Petr", "item": "Toaletní papír", "value": 65},
    {"person": "Libor", "item": "Pivo", "value": 124},
    {"person": "Petr", "item": "Pytel na odpadky", "value": 75},
    {"person": "Míša", "item": "Utěrky na nádobí", "value": 130},
    {"person": "Ondra", "item": "Toaletní papír", "value": 120},
    {"person": "Míša", "item": "Pečící papír", "value": 30},
    {"person": "Zuzka", "item": "Savo", "value": 80},
    {"person": "Pavla", "item": "Máslo", "value": 50},
    {"person": "Ondra", "item": "Káva", "value": 300},
]

sum_per_person = {}
for item in purchase_list:
    person = item["person"]
    value = item["value"]
    if person in sum_per_person:
        sum_per_person[person] += value
    else:
        sum_per_person[person] = value

total_value = 0
for person, value in sum_per_person.items():
    total_value += value
    print(f"{person} utratil(a) za společné nákupy {value} Kč.")

average_value = total_value / len(sum_per_person)
print(f"Průměrná hodnota na osobu je {round(average_value)} Kč.")

# cvičení "Spolubydlící":

for person, value in sum_per_person.items():
    rozdil = value - average_value
    if rozdil >= 0:
        print(f'{person} by měl dostat {round(rozdil)},- Kč.')
    else:
        print(f'{person} by měl doplatit {-(round(rozdil))},- Kč.')