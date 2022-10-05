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

# BONUS cvičení - Ruleta:

def roulette(sada, sazka):
    losovane_cislo = random.randint(0, 36+1)
    #losovane_cislo = 5
    sada_one = range(1, 36, 3)
    sada_two = range(2, 36, 3)
    sada_three = range(3, 36, 3)
    
    if ((sada == '1') and (losovane_cislo in sada_one)) or ((sada == '2') and (losovane_cislo in sada_two)) or ((sada == '3') and (losovane_cislo in sada_three)):
        sazka *= 2
        cislo_rady = sada
        print(f'Vyhráváš dvojnásobek vsazené částky a to: {sazka},- Kč.')
        print(f'Vylosované číslo v ruletě je: {losovane_cislo} a odpovídá č.řadě "{cislo_rady}".')
    elif losovane_cislo == 0:
        sazka = ''
        cislo_rady = '0'
        print('Nevyhráváš a číslo 0 není v žádně řadě čísel.')
    else:
        sazka = ''
        if losovane_cislo in sada_one:
            cislo_rady = '1'
        elif losovane_cislo in sada_two:
            cislo_rady = '2'
        elif losovane_cislo in sada_three:
            cislo_rady = '3'
        print('Všechno si prohrál.')
        print(f'Vylosované číslo v ruletě je: {losovane_cislo} a odpovídá č.řadě "{cislo_rady}".')
    return ''

print('První řada 1, 4, 7 atd., druhá řada 2, 5, 8 atd.,třetí řada 3, 6, 9 atd.')
sada = input('Jakou sadu čísel sis vybral? 1/2/3: ')
sazka = int(input('Kolik vsadíš na tyto čísla? '))
print(roulette(sada, sazka))
