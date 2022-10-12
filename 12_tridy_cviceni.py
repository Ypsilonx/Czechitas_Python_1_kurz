# 1. úkol:

# class Balik:
#     def __init__(self, adresa, hmotnost):
#         self.adresa = adresa
#         self.hmotnost = hmotnost
#         self.doruceno = False
    
#     def doruc(self):
#         self.doruceno = True
    
#     def __str__(self):
#         if self.doruceno:
#             vypis = 'doručen'
#         else:
#             vypis = 'nedoručen'
#         return f'Balík na {self.adresa} o hmotnosti {self.hmotnost}kg byl {vypis}.'    

# balik1 = Balik('Valmez', 80)
# balik2 = Balik('Praha', 80)

# balik1.doruc()
# print(balik1)
# print(balik2)

# 2. úkol:

# class Kniha:
#     def __init__(self, nazev, pocet_stran, cena):
#         self.nazev = nazev
#         self.pocet_stran = pocet_stran
#         self.cena = cena
        
#     def __str__(self):
#         # if :
#         #     slevicka = f'a po slevě má cenu {self.cena},- Kč'
#         # else:
#         #     slevicka = f'má cenu {self.cena},- Kč'
#         # return f'Kniha {self.nazev} s počtem stran {self.pocet_stran} {slevicka}.'
#         return f'Kniha {self.nazev} s počtem stran {self.pocet_stran} a má cenu {self.cena},- Kč.'
        
#     def sleva(self, velikost_slevy=0):
#         self.cena = int(self.cena - (self.cena*(velikost_slevy/100)))

# kniha1 = Kniha('Stopař', 120, 390)
# kniha2 = Kniha('Dukla', 50, 150)

# print(kniha1)
# kniha1.sleva(20)
# print(kniha1)
# print(kniha2)

# 3. úkol:

# class Zamestnanec:
#     def __init__(self, jmeno, pozice, zkusebni_doba=False):
#         self.jmeno = jmeno
#         self.pozice = pozice
#         self.zkusebni_doba = zkusebni_doba

#     def __str__(self):
#         if self.zkusebni_doba:
#             vypis = f' ve zkušební době.'
#         else:
#             vypis = '.'
#         return f'{self.jmeno} pracuje na pozici {self.pozice}' + vypis

# frantisek = Zamestnanec("František Novák", "konstruktér", True)
# print(frantisek)