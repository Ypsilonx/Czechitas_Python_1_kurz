import pandas
#jobs = pandas.read_csv('DataAnalyst.csv')

# print(jobs.columns)

# print(jobs.shape[0])

# print(jobs.iloc[9])

# print(jobs.iloc[11:21, 6:8])

# names = pandas.read_csv('jmena.csv')
# print(names.loc[97])

# 1.úkol
# names = names.set_index('jméno')
# print(names)

# print(names.loc['Jiří'])

# print(names.loc[['Martin', 'Josef', 'Zuzana']])

# print(names.loc[: 'Martin'])

# print(names.loc['Martin':'Tereza', 'věk'])

# print(names.loc['Libor':, ['věk', 'původ']])

# print(names.loc[:, 'věk': 'původ']) # nemusím dávat druhé závorky hranaté

# 2.úkol:
# jmena = names[names['věk'] > 60]
# print(jmena)

# jmena = names[(names['četnost'] > 80000)& (names['četnost'] < 100000)]
# print(jmena['jméno'])

# jmena = names[(names['původ'] == 'hebrejský') | (names['původ'] == 'slovanský')]
# print(jmena['jméno'])

# jmena = names[names['původ'].isin(['hebrejský', 'slovanský'])]
# print(jmena[['jméno', 'četnost']])
# print(jmena.shape[0])

# jmena = names[names['svátek'].isin(['1.12', '2.12', '3.12'])]
# print(jmena['jméno'])

# prosinec = names[names['svátek'].str.endswith('.12')]
# print(prosinec)


