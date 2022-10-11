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
# def month_of_birth(rodne_cislo):
#     mesic_narozeni = str(rodne_cislo)
#     mesic = (mesic_narozeni[2: 4])
#     mesic = int(mesic)
#     if mesic >= 50:
#         mesic -= 50
#     return mesic

# rodne_cislo = input('Zadej rodne cislo: ')
# print(month_of_birth(rodne_cislo))

# # 2.varianta:
# def month_of_birth(rodne_cislo):
#     mesic = int(rodne_cislo[2: 4])
#     if mesic >= 50:
#         mesic -= 50
#     return mesic

# rodne_cislo = input('Zadej rodne cislo: ')
# print(month_of_birth(rodne_cislo))

# BONUS cvičení - Ruleta:

# import random

# print('První řada 1, 4, 7 atd., druhá řada 2, 5, 8 atd.,třetí řada 3, 6, 9 atd.')
# sada = int(input('Jakou řadu čísel sis vybral? 1/2/3: '))
# sazka = int(input('Kolik vsadíš na tyto čísla? '))

# def roulette(sada, sazka):
#     rady = [
#     range(1, 37, 3),
#     range(2, 37, 3),
#     range(3, 37, 3),
#     ]
#     #losovane_cislo = random.randint(0, 36+1)
#     losovane_cislo = 9
#     print(f'Vylosované číslo v ruletě je: {losovane_cislo}.')
    
#     if losovane_cislo in rady[sada - 1]:
#         sazka *= 2
#         rada = sada
#     elif losovane_cislo == 0:
#         sazka = 0
#         rada = 0
#         print('Číslo 0 není v žádně řadě čísel.')
#     else:
#         sazka = 0
        
#         print('Netrefil ses.')
#     return sazka

# vyhra = (roulette(sada, sazka))
# print(f'Vyhráváš {vyhra},- Kč.')

# import random

# vybrana_rada = int(input('Na kterou řadu sázíš? (1-3): '))
# vsazeno = int(input('Kolik sázíš?: '))

# def ruleta(cislo_rady, sazka):
#     rady = [
#         range(1, 37, 3),  # 1, 4, 7, ...
#         range(2, 37, 3),  # 2, 5, 8, ...
#         range(3, 37, 3),  # 3, 6, 9, ...
#         ]
#     hozeno = random.randint(0, 36)
#     print(f"Hozeno: {hozeno}")
#     # Ukázka jednořádkového zápisu if (elegantní, ale pro přehlednost by se možná vyplatilo rozepsat na víc řádků):
#     return 2 * sazka if hozeno in rady[cislo_rady - 1] else 0  # "- 1" kvůli indexování od nuly

# vyhra = ruleta(vybrana_rada, vsazeno)
# print(f"Vyhráváš {vyhra}")

# import random

# print('První řada 1, 4, 7 atd., druhá řada 2, 5, 8 atd.,třetí řada 3, 6, 9 atd.')
# sada = input('Jakou sadu čísel sis vybral? 1/2/3: ')
# sazka = int(input('Kolik vsadíš na tyto čísla? '))

# def roulette(sada, sazka):
#     losovane_cislo = random.randint(0, 36)
#     #losovane_cislo = 5
#     sada_one = range(1, 37, 3)
#     sada_two = range(2, 37, 3)
#     sada_three = range(3, 37, 3)
    
#     if ((sada == '1') and (losovane_cislo in sada_one)) or ((sada == '2') and (losovane_cislo in sada_two)) or ((sada == '3') and (losovane_cislo in sada_three)):
#         sazka *= 2
#         cislo_rady = sada
#         print(f'Vyhráváš dvojnásobek vsazené částky a to: {sazka},- Kč.')
#         print(f'Vylosované číslo v ruletě je: {losovane_cislo} a odpovídá č.řadě "{cislo_rady}".')
#     elif losovane_cislo == 0:
#         sazka = ''
#         cislo_rady = '0'
#         print('Nevyhráváš a číslo 0 není v žádně řadě čísel.')
#     else:
#         sazka = ''
#         if losovane_cislo in sada_one:
#             cislo_rady = '1'
#         elif losovane_cislo in sada_two:
#             cislo_rady = '2'
#         elif losovane_cislo in sada_three:
#             cislo_rady = '3'
#         print('Všechno si prohrál.')
#         print(f'Vylosované číslo v ruletě je: {losovane_cislo} a odpovídá č.řadě "{cislo_rady}".')
#     return ''

# print(roulette(sada, sazka))

import random

vybrana_rada = int(input('Na kterou řadu sázíš? (1-3): '))
vsazeno = int(input('Kolik sázíš?: '))

def ruleta(cislo_rady, sazka):
    #hozeno = random.randint(0, 36)
    hozeno = 1
    print(f"Hozeno: {hozeno}")
    if hozeno == 0:
        print('Nula nevyhrává.')
        return hozeno
    
    zbytek = hozeno % 3
    rady = {
        1: cislo_rady == 1 and zbytek == 1,
        2: cislo_rady == 2 and zbytek == 2,
        3: cislo_rady == 3 and zbytek == 0,
    }
    
    print(f'Číslo {hozeno} patří do {3 if zbytek == 0 else zbytek} řady.')
    
    if rady.get(cislo_rady, False):
        print(f'Vyhráváš {sazka * 2}!')
        return sazka * 2

    print(f'Nevyhráváš protože sis tipnul {cislo_rady} radu.')
    return 0
    
ruleta(vybrana_rada, vsazeno)
