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