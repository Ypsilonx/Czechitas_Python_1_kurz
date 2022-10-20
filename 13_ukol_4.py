class Recept:
    def __init__(self, nazev: str, narocnost: int, url_adresa: str):
        self.nazev = nazev
        self.narocnost = narocnost
        self.url_adresa = url_adresa
        self.vyzkouseno = False
    
    def __str__(self):
        return f'{self.nazev} je recept s náročností {self.narocnost} na drese {self.url_adresa} a máme vyzkoušeno? {self.vyzkouseno}'

    def zmen_narocnost(self, nova_hodnota: int):
        self.narocnost = nova_hodnota
        return self.narocnost

    def zkusit(self):
        self.vyzkouseno = True
        return self.vyzkouseno

class Kucharka:
    def __init__(self, nazev: str, autor: str):
        self.nazev = nazev
        self.autor = autor
        self.recepty = []
    
    def __str__(self):
        return f'{self.nazev} od {self.autor} - {len(self.recepty)} receptů -> seznam: {self.recepty}'
    
    def pocet_receptu(self):
        return len(self.recepty)
        
    def pridej_recept(self, recept):
        return self.recepty.append(recept)
        
        
#muj_recept1 = Recept('Babovka', 1, 'blablabla')
#muj_recept1.zmen_narocnost(3)
#muj_recept1.zkusit()
#print(muj_recept1)        
