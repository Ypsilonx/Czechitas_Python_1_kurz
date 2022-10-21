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
    
    def __repr__(self): # můžeme si zavolat str pro REPR - abychom nekopírovali kód
        return self.__str__()

    def zmen_narocnost(self, nova_hodnota: int):
        self.narocnost = nova_hodnota
    
    def zkusit(self):
        self.vyzkouseno = True

class Kucharka:
    def __init__(self, nazev: str, autor: str):
        self.nazev = nazev
        self.autor = autor
        self.recepty = []
    
    def __str__(self):
        # if len(self.recepty) > 0:
        #     pocet_recept = f'{Kucharka.pocet_receptu(self)} recep. - seznam:'
        # else:
        #     pocet_recept = 'neobsahuje recepty'
        # vypis = f'{self.nazev} od {self.autor} - {pocet_recept}'
        # print(vypis)
        # seznam = [[recept.nazev, recept.narocnost, recept.url_adresa] for recept in self.recepty]
        # for recep in seznam:
        #     seznam_recep = f'Recept: {recep[0]} /náročnost: {recep[1]} /adresa: {recep[2]}'
        #     print(seznam_recep)
        # return ''
        if len(self.recepty) > 0:
            pocet_recept = f'{Kucharka.pocet_receptu(self)} recep. - seznam:'
        else:
            pocet_recept = 'neobsahuje recepty'
        vypis = f'{self.nazev} od {self.autor} - {pocet_recept}\n'
        for recept in self.recepty:
            vypis += recept.__str__()+"\n"
        return vypis
    
    def pocet_receptu(self):
        return len(self.recepty)
        
    def pridej_recept(self, recept):
        self.recepty.append(recept)
    
    def vyzkousene_recepty(self):
        # odmazal jsem jenom .nazev a vypíše se vše co je v REPR
        return [zkouska for zkouska in self.recepty if zkouska.vyzkouseno]

#_____________________________________________________
        
muj_recept1 = Recept('Babovka', 1, 'babovky.cz')
muj_recept2 = Recept('Štrůdl', 2, 'strudly.eu')
muj_recept3 = Recept('Muffin', 2, 'muffins.com')
muj_recept4 = Recept('Buchta', 5, 'buchty.cz')
muj_recept1.zmen_narocnost(3)
muj_recept1.zkusit()
print(muj_recept1)
print(muj_recept2)
print(muj_recept3)
muj_recept4.zkusit()
print(muj_recept4)
print('___________________________________')
moje_kucharka1 = Kucharka('Domací kuchařka', 'Tom')
print(moje_kucharka1)
moje_kucharka1.pridej_recept(muj_recept1)
muj_recept2.zmen_narocnost(5)
moje_kucharka1.pridej_recept(muj_recept2)
moje_kucharka1.pridej_recept(muj_recept3)
moje_kucharka1.pridej_recept(muj_recept4)
print(moje_kucharka1)
print('___________________________________')

print(moje_kucharka1.vyzkousene_recepty())
