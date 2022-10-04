# 1. cvičení:

# def mult(a, b):
#     vysledek = a * b
#     return vysledek

# a = int(input('prvni číslo: '))
# b = int(input('druhe číslo: '))
# print(mult(a, b))

# 2. cvičení:

# def total_price(persons, breakfast = False):
#     cena_noc = 850 * persons
#     cena_snidane = 125 * persons
#     if breakfast:
#         cena = cena_noc + cena_snidane
#     else:
#         cena = cena_noc
#     return cena

# print(total_price(3))
# print(total_price(2, True))

# BONUS cvičení:

# 1.varianta:
def month_of_birth(rodne_cislo):
    mesic_narozeni = str(rodne_cislo)
    mesic = (mesic_narozeni[2: 4])
    mesic = int(mesic)
    if mesic >= 50:
        mesic -= 50
    return mesic

rodne_cislo = input('Zadej rodne cislo: ')
print(month_of_birth(rodne_cislo))

# 2.varianta:
def month_of_birth(rodne_cislo):
    mesic = int(rodne_cislo[2: 4])
    if mesic >= 50:
        mesic -= 50
    return mesic

rodne_cislo = input('Zadej rodne cislo: ')
print(month_of_birth(rodne_cislo))
