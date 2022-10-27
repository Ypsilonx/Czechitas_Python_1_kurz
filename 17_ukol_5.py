class Nemoc:
    # poradi argumentu v radku nize si klidne preskladejte
    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni):
        self.jmeno = jmeno
        self.inkubacni_doba = inkubacni_doba
        self.pocet_obeti = pocet_obeti
        self.sireni = sireni

    def __str__(self):
        return f'Jmeno: {self.jmeno}'

    def zmen_pocet_obeti(self, pocet_obeti):
        self.pocet_obeti = pocet_obeti

class Koronavirus(Nemoc):
    def __init__(self, jmeno, varianta):
        super().__init__(jmeno)
        self.varianta = []
    
    def zmen_pocet_obeti(self, pocet_obeti):
        super().zmen_pocet_obeti(pocet_obeti)
        
    def pridej_variantu(self, varianta):
        
