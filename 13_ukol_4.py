class Recept:
    def __init__(self, nazev: str, narocnost: int, url_adresa: str):
        self.nazev = nazev
        self.narocnost = narocnost
        self.url_adresa = url_adresa
        self.vyzkouseno = False
    
    def __str__(self):
        if self.vyzkouseno:
            zkouska = 'vyzkoušeno'
        else:
            zkouska = 'nevyzkoušeno'
        return f'{self.nazev} (náročnost: {self.narocnost}), najdu: {self.url_adresa} - {zkouska}'
    
    # def __repr__(self):
    #     if self.vyzkouseno:
    #         zkouska = 'vyzkoušeno'
    #     else:
    #         zkouska = 'nevyzkoušeno'
    #     return f'{self.nazev} (náročnost: {self.narocnost}), najdu: {self.url_adresa} - {zkouska}'

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
        if len(self.recepty) > 0:
            pocet_recept = f'{Kucharka.pocet_receptu(self)} recep.'
        else:
            pocet_recept = 'neobsahuje recepty'
        return f'{self.nazev} od {self.autor} - {pocet_recept} - seznam: {[Recept.nazev for Recept in self.recepty]}'
    
    def pocet_receptu(self):
        return len(self.recepty)
        
    def pridej_recept(self, recept):
        return self.recepty.append(recept)
    
    def vyzkousene_recepty(self):
        return [Recept.nazev for Recept in self.recepty if Recept.vyzkouseno]

        
muj_recept1 = Recept('Babovka', 1, 'babovky.cz')
muj_recept2 = Recept('Štrůdl', 2, 'strudly.eu')
muj_recept3 = Recept('Muffin', 2, 'muffins.com')
muj_recept1.zmen_narocnost(3)
muj_recept1.zkusit()
print(muj_recept1)
print(muj_recept2)
print(muj_recept3)
print('___________________________________')
moje_kucharka1 = Kucharka('Domací kuchařka', 'Tom')
print(moje_kucharka1)
moje_kucharka1.pridej_recept(muj_recept1)
moje_kucharka1.pridej_recept(muj_recept2)
moje_kucharka1.pridej_recept(muj_recept3)
print(moje_kucharka1)
print('___________________________________')

muj_recept2.zkusit()
print(moje_kucharka1.vyzkousene_recepty())