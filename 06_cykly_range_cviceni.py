# 1. Tombola
# V tombole bylo prodáno celkem 1000 lístků. Naším úkolem je vylosovat náhodně tři výherce. 
# Napište program, který vygeneruje a vypíše tři čísla mezi 1 a 1000. Využijte funkci *randint*, nezapomeňte ale, že si ji musíte importovat z modulu *random*.
# Neřešte, že jedno číslo může být vygenerováno dvakrát.

# import random

# prodane_listky = int(input('Zadej kolik se prodalo lístků: '))
# for i in range(1, 4):
#     vyherni_los = random.randint(1, (prodane_listky + 1))
#     print(f'{i}. výherní los je číslo {vyherni_los}.')

# 2. Dělitelnost více čísly
# Vypišme si čísla z nějakého rozsahu na základě jejich dělitelnosti dvěma čísly.
# a) Zkuste z nějakého rozsahu čísel vypsat čísla, která jsou dělitelná 3 i 4 současně.
# b) Zkuste z nějakého rozsahu čísel vypsat čísla, která jsou dělitelná 5 nebo 6. Stačí vypsat text: "Číslo je dělitelné 5 nebo 6."

# a)
# rozsah_start = int(input('Zadej začátek rozsahu: '))
# rozsah_konec = int(input('Zadej konec rozsahu: '))
# delitel = [3, 4]
# for cislo in range(rozsah_start, rozsah_konec):
#     if cislo % delitel[0] == 0 and cislo % delitel[1] == 0:
#         print(cislo)
# b)
# rozsah_start = int(input('Zadej začátek rozsahu: '))
# rozsah_konec = int(input('Zadej konec rozsahu: '))
# delitel = [(int(input('Zadej dělitele číslo 1: '))), (int(input('Zadej dělitele číslo 2: ')))]
# for cislo in range(rozsah_start, rozsah_konec):
#     if cislo % delitel[0] == 0 or cislo % delitel[1] == 0:
#         print(f'Čísla jsou dělitelná {delitel[0]} a {delitel[1]}.')
#         break

# 3. Seznam hostů na party
# Vraťte se k příkladu se zadáváním seznamu hostu na párty a zkopírujte si kód k sobě do editoru. 
# Upravte program tak, že pokud uživatel v průběhu zadávání jmen napíše "konec", cyklus na zadávání jmen se ukončí.

# number_of_guests = int(input("Zadej počet hostů: "))
# guest_list = []
# for i in range(number_of_guests):
#     new_guest = input("Zadej jméno hosta: ")
#     if new_guest == 'konec':
#         break
#     guest_list.append(new_guest)
# print(guest_list)

# BONUS
# Požádej uživatele o zadání celého čísla. Následně urči, zda je toto číslo prvočíslo.
# Prvočíslo je číslo, které je dělitelné beze zbytku pouze 2 čísly - 1 a sebou samotným.
# - Například 5 je prvočíslo, protože je dělitelná pouze 1 a 5.
# - Naopak 4 není prvočíslo, protože je dělitelná 1, 2 a 4.

# zadane_cislo = int(input('Zadej jakékoliv číslo: '))
# delitele = []
# prvocislo = True
# for delitel in range(1, (zadane_cislo + 1)):
#     if 1 < (zadane_cislo / delitel) < zadane_cislo and (zadane_cislo % delitel == 0):
#         delitele.append(delitel)
#         print(f'{delitele}')
# if zadane_cislo > 1:    
#     for delitel in range(2, zadane_cislo):
#         if (zadane_cislo % delitel) == 0:
#             prvocislo = False
#             break
# if prvocislo:
#     print(f'{zadane_cislo} je prvočíslo, protože je dělitelné 1 a {zadane_cislo}.')
# else:
#     print(f'{zadane_cislo} není prvočíslo, protože je dělitelné 1, {delitele} a {zadane_cislo}.')

# od lektorky (ale upravil jsem):

# zadane_cislo = int(input("Zadej cislo: "))
# if zadane_cislo == 1:
#     print(f'{zadane_cislo} není prvočíslo.')
# else:
#     je_prvocislo = True

# if zadane_cislo > 1:
#     for i in range(2, zadane_cislo):
#         if (zadane_cislo % i) == 0:
#             je_prvocislo = False
#             break
#     if je_prvocislo:
#         print(f'{zadane_cislo} je prvočíslo.')
#     else:
#         print(f'{zadane_cislo} není prvočíslo.')

# for c in range(1, 10):
#     if (10 % c) == 0:
#         print(c)

# cvičení WHILE:

#import random

# zadane_cislo = int(input("Zkus trefit tajné číslo: "))
# tajne_cislo = random.randint(1,(100 + 1))
# print(tajne_cislo)
# while zadane_cislo != tajne_cislo:
#     print("Aj, vedle zkus to znova.")
#     zadane_cislo = int(input("Zadej číslo znovu: "))
# print("Hurá trefa!!! ;-)")
import random

def hra():
    dolni_hranice = int(input('Zadej spodní hranici pro hádání: '))
    horni_hranice = int(input('Zadej horní hranici pro hádání: '))
    pocet_pokusu = int(input('Zadej kolik šancí dáš hráči k uhádnutí: '))
    zadane_cislo = int(input('Zkus hádat tajné číslo: '))
    tajne_cislo = random.randint(dolni_hranice,(horni_hranice))
    print(tajne_cislo)
    progres = 'Jsi mimo. Tajné číslo je'
    porovnani = ''
    pokus = 0
    while zadane_cislo != tajne_cislo:
        pokus += 1
        if pokus == pocet_pokusu:
            print(f'Prohrál jsi hru, tajné číslo je {tajne_cislo}.')
            zadane_cislo = tajne_cislo
            break
        if zadane_cislo > tajne_cislo:
            porovnani = 'menší'
            print(f'{progres} {porovnani}.')
        elif zadane_cislo < tajne_cislo:
            porovnani = 'větší'
            print(f'{progres} {porovnani}.')
        zadane_cislo = int(input('Zadej číslo znovu: '))
        if zadane_cislo == tajne_cislo:
            print('Hurá trefa!!! ;)')


start_hry = input('Chceš si zahrát? Ano/Ne: ')
if start_hry in ['Ano', 'A', 'ano', 'Jo', 'jo', 'a']:
    print('Tak se připrav...')
    hra()
else:
    print('Hra skončila.')