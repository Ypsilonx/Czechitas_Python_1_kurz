# class Unicorn: # název třídy začíná velkým a při složeném jménu dávám velká písmena
#     def vypis_informace(self):
#         # print(f'Jmenuji se {self.jmeno} a má {self.barva} barvu.')
#         return f'Jmenuji se {self.jmeno} a má {self.barva} barvu.'


# karel = Unicorn()
# karel.jmeno = 'Karel'
# karel.barva = 'duhovou'

# lenka = Unicorn()
# lenka.jmeno = 'Lenka'
# lenka.barva = 'pruhovanou'

# print(karel.vypis_informace())
# print(lenka.vypis_informace())

# class Jednorozec:
#     def __init__(self, jmeno, barva, as_alive=False):
#         self.jmeno = jmeno
#         self.barva = barva
#         self.as_alive = as_alive

#     def vypis_informace(self):
#         vypis = f'{self.jmeno} má barvu {self.barva}'
#         if self.as_alive:
#             vypis += ' a je naživu.'
#         else:
#             vypis += ' a není naživu.'
#         print(vypis)


# karel = Jednorozec('Karel', 'duhovou')
# # print(karel.jmeno)
# # print(karel.barva)
# # print(karel.as_alive)    

# karel.vypis_informace()

class Jednorozec:
    def __init__(self, jmeno, barva, as_alive=False):
        self.jmeno = jmeno
        self.barva = barva
        self.as_alive = as_alive

    def __str__(self):
        return f'{self.jmeno} a má {self.barva} barvu'
    
    def __eq__(self, y):
        return self.jmeno == y.jmeno
    
    def vypis_informace(self):
        vypis = f'{self.jmeno} má barvu {self.barva}'
        if self.as_alive:
            vypis += ' a je naživu.'
        else:
            vypis += ' a není naživu.'
        print(vypis)


karel = Jednorozec('Karel', 'duhovou')

# print(karel.jmeno)
# print(karel.barva)
# print(karel.as_alive)    

karel.vypis_informace()
# karel1 = Jednorozec('Karel', 'duhovou')
# karel2 = Jednorozec('Karel', 'růžovou')

# print(karel)
# print (karel1 == karel2)