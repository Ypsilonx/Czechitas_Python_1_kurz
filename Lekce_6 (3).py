class Zamestnanec:
    def __init__(self, jmeno, pozice):
        self.jmeno = jmeno
        self.pozice = pozice
        self.pocet_dni_dovolene = 25

    def __str__(self):
        return f'{self.jmeno} pracuje na pozici {self.pozice}'
    
    def cerpani_dovolene(self, pocet_dni):
        if pocet_dni <= self.pocet_dni_dovolene:
            self.pocet_dni_dovolene -= pocet_dni
            return f'Zbyva dovolene: {self.pocet_dni_dovolene}'
        else:
            return f'Nemas dostatek dovolene: {self.pocet_dni_dovolene}'

# dědičnost (třída v třídě - podmnožina v množině, nadřazenost a podřazenost):
# funkce super() volá metody z nadřazené třídy
class Manazer(Zamestnanec):
    def __init__(self, jmeno, pozice, pocet_podrizenych):
        super().__init__(jmeno, pozice)
        self.pocet_podrizenych = pocet_podrizenych
        self.pocet_dni_dovolene = 30

    def __str__(self):
        return f'{super().__str__()} a má {self.pocet_podrizenych} podřízených'

frantisek1 = Zamestnanec('František', 'programátor')
frantisek2 = Manazer('Arnošt', 'programator', 10)
print(frantisek1)
print(frantisek2)
print(frantisek2.cerpani_dovolene(10))
# print(frantisek.cerpani_dovolene(5))
# print(frantisek.cerpani_dovolene(15))
# print(frantisek.cerpani_dovolene(10))