import pandas
nakupy = pandas.read_csv('nakupy.csv')
# Zjištění počtu řádků
# print(nakupy.shape[0])
# Výběr sloupců
# print(nakupy[['Jméno', 'Částka v korunách']])
# Výběr řádků (0:5 - jsou řádky 0-4 /stejné jako- :5- od začátku seznamu/ nebo od do konce seznamu 8:)
# print(nakupy.iloc[3:5])
# print(nakupy.iloc[8:])
# print(nakupy.iloc[-3:]) # záporné číslo odpočítává od konce
# print(nakupy.head()) # začátek a konec (tail) seznamu
# Výběr řádků a sloupců
# print(nakupy.iloc[:5, 0])
# print(nakupy.iloc[:5, [0, 3]])