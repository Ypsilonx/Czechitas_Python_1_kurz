# 1. část

# sales = {
#     "Zkus mě chytit": 4165,
#     "Vrah zavolá v deset": 5681,
#     "Zločinný steh": 2565,
#     "Ucho belzebuba": 3585,
# }

# for key in sales:
#     print(key)
    
# for key, value in sales.items():
#     print("Knihy", key, "bylo prodáno", value, "výtisků.")
#     # Použití f-stringu
#     print(f"Knihy {key} bylo prodáno {value} výtisků.")

# total_sales = 0
# for key, value in sales.items():
#     # print("Knihy", key, "bylo prodáno", value, "výtisků.")
#     # Použití f-stringu
#     print(f"Knihy {key} bylo prodáno {value} výtisků.")
#     total_sales += value
# print(f"Celkem bylo prodáno {total_sales} výtisků.")

# 2. část

# books = [
#     {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
#     {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
#     {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
#     {"title": "Bidnici", "sold": 3549, "price": 669, "year": 2018},
#     {"title": "Šoupátka", "sold": 6843, "price": 429, "year": 2020},
# ]

#-- POZOR! - slovníky vložené do seznamu

# sales = 0
# for item in books:
#     sales += item['sold']
# print(f'Celkem bylo prodáno {sales} knih.')

# timeYear = int(input('Zadej jaký rok byly knihy vydány: '))

# sales = 0
# for item in books:
#     if item['year'] == timeYear:
#         sales += item['sold'] * item['price']
# print(f'Celkem bylo prodáno knih v roce {timeYear} za {sales} Kč.')

# sales = 0
# for item in books:
#     sales += item['sold'] * item['price']
# print(f'Celkem bylo prodáno knih za {sales} kč.')