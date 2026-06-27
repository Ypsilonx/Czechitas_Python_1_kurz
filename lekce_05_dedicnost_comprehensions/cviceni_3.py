# 1 Částečný úvazek (zapni hlavu)
# Naše firma se rozhodla zaměstnávat i pracovníky na částečné úvazky, pro které bude vytvořena zvláštní třída.
# Vytvoř novou třídu Brigadnik, která bude dědit od třídy Zamestnanec a bude mít navíc atribut uvazek,
# který reprezentuje velikost úvazku oproti plnému.
# Přidej informaci o úvazku k výpisu informací do funkce __str__.

class Zamestnanec:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.uvazek = 'plný'
        
    def __str__(self):
        return f'{self.jmeno} má v naší firmě {self.uvazek} úvazek.'

class Brigadnik(Zamestnanec):
    def __init__(self, jmeno):
        super().__init__(jmeno)
        self.uvazek = 'částečný'

    def __str__(self):
        return super().__str__()
    
tom = Brigadnik('Tom')
print(tom)
vaclav = Zamestnanec('Václav')
print(vaclav)

# 2 Balík (zapni hlavu)
# Pokračuj ve své práci pro zásilkovou společnost. Společnost nově doručuje i cenné balíky, které mají zadanou určitou hodnotu.

# Trida Balik z minuleho cviceni
class Balik:
    def __init__(self, adresa, hmotnost, hodnota=0):
        self.adresa = adresa
        self.hmotnost = hmotnost
        self.doruceno = False

    def doruc(self):
        self.doruceno = True

    def __str__(self):
        vypis = f'{self.adresa} ({self.hmotnost} kg) - {self.doruceno}'
        return vypis

# Vytvoř třídu CennyBalik, která dědí od třídy Balik.
# CennyBalik má navíc atribut hodnota, ostatní atributy dědí od třídy Balik.
# Atribut hodnota nastav pomocí funkce __init__. Ostatní parametry předej funkci __init__ třídy Balik.
# Vytvoř si alespoň jeden objekt a zkus volání jeho funkcí.

class CennyBalik(Balik):
    def __init__(self, adresa, hmotnost, hodnota):
        super().__init__(adresa, hmotnost)
        self.hodnota = hodnota
        
    def __str__(self):
        return f'{super().__str__()} /{self.hodnota},- Kč.'
        
balik1 = CennyBalik('Valmez', 5, 350)
print(balik1)
balik1.doruc()
print(balik1)
balik2 = Balik('Vsetín', 2)
print(balik2)
balik2.doruc()
print(balik2)