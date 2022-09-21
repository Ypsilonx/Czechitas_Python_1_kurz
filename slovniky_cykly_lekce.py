sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
    "Ucho belzebuba": 3585,
}

for key in sales:
    print(key)
    
for key, value in sales.items():
    print("Knihy", key, "bylo prodáno", value, "výtisků.")
    # Použití f-stringu
    print(f"Knihy {key} bylo prodáno {value} výtisků.")

total_sales = 0
for key, value in sales.items():
    # print("Knihy", key, "bylo prodáno", value, "výtisků.")
    # Použití f-stringu
    print(f"Knihy {key} bylo prodáno {value} výtisků.")
    total_sales += value
print(f"Celkem bylo prodáno {total_sales} výtisků.")

