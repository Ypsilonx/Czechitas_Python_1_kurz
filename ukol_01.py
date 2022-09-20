baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
kod_baliku = input('Zadej kód balíku: ')
if True == baliky.get(kod_baliku):
    print('Balík byl předán kurýrovi')
else:
    print('Balík zatím nebyl předán kurýrovi')