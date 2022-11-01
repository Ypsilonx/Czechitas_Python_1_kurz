baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
# kod_baliku = ''
# while kod_baliku not in baliky:
#     kod_baliku = input('Zadej kód balíku: ')
#     if True == baliky.get(kod_baliku):
#         print('Balík byl předán kurýrovi')
#     elif False == baliky.get(kod_baliku):
#         print('Balík zatím nebyl předán kurýrovi')
#     else:
#         print('Zadal si špatné číslo balíku.')

cislo_baliku = input('Zadej kód balíku: ')
if cislo_baliku in baliky:
    na_sklade = baliky[cislo_baliku]
    if na_sklade == True:
        print('Balík byl předán kurýrovi.')
    else:
        print('Balík nebyl ještě předán kurýrovi.')
else:
    print(f'Balík {cislo_baliku} není v přepravě.')