# 1. úkol:

class Balik:
    def __init__(self, adresa, hmotnost):
        self.adresa = adresa
        self.hmotnost = hmotnost
        self.doruceno = False
    
    def doruc(self):
        self.doruceno = True
    
    def __str__(self):
        if self.doruceno:
            vypis = 'doručen'
        else:
            vypis = 'nedoručen'
        return f'Balík na {self.adresa} o hmotnosti {self.hmotnost}kg byl {vypis}.'    

balik1 = Balik('Valmez', 80)
balik2 = Balik('Praha', 80)

balik1.doruc()
print(balik1)
print(balik2)