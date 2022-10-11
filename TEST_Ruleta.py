import random

def ruleta(cislo_rady, sazka):
    # hozeno = random.randint(0, 36)
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

def srajtofla_start(bank, min_zustatek):
    if (bank - min_zustatek) <= 0:
        print('Našetři si a pak se vrať.')
        exit()
    else:
        print('Máš v banku dostatek peněz pro začátek hry.')
    return bank

def srajtofla_konec(bank, sazka, vyhra):
    bank -= sazka
    bank += vyhra
    print(f'Aktuální stav tvé peněženky je {bank},- Kč.')
    return bank
    
#__________________________________________________________

print('Vítám tě ve hře "Ruleta".')
penezenka = int(input('Kolik máš celkem peněz v banku: '))
limitbanku = int(input('Kolik peněz nechceš prohrát: '))

while penezenka > 0:
    bank1 = srajtofla_start(penezenka, limitbanku)

    vybrana_rada = int(input('Na kterou řadu sázíš? (1-3): '))
    vsazeno = int(input('Kolik sázíš?: '))
    if vsazeno > (penezenka - limitbanku):
        print(f'Chceš vsadit o {vsazeno - (penezenka - limitbanku)},- Kč víc než si plánoval.')
        vsazeno = int(input(f'Změň svou sázku banku, tvůj limit je {limitbanku}: '))
    vyhra = ruleta(vybrana_rada, vsazeno)
    bank2 = srajtofla_konec(penezenka, vsazeno, vyhra)
    penezenka = bank2








# if penezenka != 0:
#     print('Máš v banku dostatek peněz pro začátek hry.')
# else:
#     print('Našetři si a pak se vrať.')
#     exit()

# vybrana_rada = int(input('Na kterou řadu sázíš? (1-3): '))
# vsazeno = int(input('Kolik sázíš?: '))
# penezenka -= vsazeno
# if penezenka < 0:
#     print('Pro takovou sázku nemáš dostatek peněz.')
# else:
#     vyhra = ruleta(vybrana_rada, vsazeno)
#     penezenka += vyhra
#     print(f'Aktuální stav tvé peněženky je {penezenka},- Kč.')