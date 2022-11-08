# Základní dotazy

# import pandas
# staty = pandas.read_json('staty.json')
# staty = staty.set_index('name')

# print(staty.index)

# print(staty.info())

# print(staty.loc['Czech Republic'])

# print(staty.loc['Czech Republic', 'population'])

# print(staty.loc['Czech Republic': 'Dominican Republic'])

# print(staty.loc[['Czech Republic', 'Slovakia']])

# print(staty.loc[['Czech Republic', 'Slovakia'], ['area', 'population']])

# print(staty.loc[['Dominican Republic', 'Poland'], ['area', 'population']])

# print(staty[['population', 'area']])

# # sloupec populace
# populace = staty['population']
# print(populace)
# # sečte hodnoty
# populace = staty['population'].sum()
# print(populace)
# # ukáže max
# populace = staty['population'].max()
# print(populace)

# print(staty['population'] < 1000)

# malestaty = staty[staty['population'] < 1000]
# print(malestaty.info)

# malestaty = staty[staty['population'] < 1000]
# print(malestaty[['population', 'area']])

# maleevropske = staty[(staty['population'] < 1000) & (staty['region'] == 'Europe')]
# print(maleevropske['population'])

# maleevropske = staty[(staty['population'] < 1000) | (staty['region'] == 'Europe')]
# print(maleevropske['population'])

# print(staty[staty['subregion'].isin(['Western Europe', 'Eastern Europe', 'Eastern Asia'])])

# AGREGACE

# u202 = pandas.read_csv("https://kodim.cz/cms/assets/kurzy/python-data-1/python-pro-data-1/agregace-a-spojovani/u202.csv")
# u203 = pandas.read_csv("https://kodim.cz/cms/assets/kurzy/python-data-1/python-pro-data-1/agregace-a-spojovani/u203.csv")
# u302 = pandas.read_csv("https://kodim.cz/cms/assets/kurzy/python-data-1/python-pro-data-1/agregace-a-spojovani/u302.csv")

# u202 = pandas.read_csv('u202.csv')
# u203 = pandas.read_csv('u203.csv')
# u302 = pandas.read_csv('u302.csv')

# složení tabulek bez prázdných hodnot:
# u202 = pandas.read_csv('u202.csv').dropna()
# u203 = pandas.read_csv('u203.csv').dropna()
# u302 = pandas.read_csv('u302.csv').dropna()
# Přidání do tabulky sloupčku z jaké tabulky jsou daná data:
# u202 = pandas.read_csv('u202.csv').dropna()
# u202['mistnost'] = 'u202'
# u203 = pandas.read_csv('u203.csv').dropna()
# u203['mistnost'] = 'u203'
# u302 = pandas.read_csv('u302.csv').dropna()
# u302['mistnost'] = 'u302'

# print(u202['znamka'].isnull())

# print(u202[u202['znamka'].isnull()])

# print(u202.shape)
# maturita = pandas.concat([u202, u203, u302], ignore_index=True) #ignore_index mi přečísluje spojené tabulky
# print(maturita.shape)
# print(maturita.tail())
# print(maturita)

# studenti = pandas.read_csv('studenti.csv')
# maturita = pandas.concat([u202, u203, u302], ignore_index=True)
# maturita = pandas.merge(maturita, studenti)
# print(maturita.tail())
# print(maturita.shape) # pokud mi zmizí řádky v tabulce po MERGE znamená to, že v nové tabulce nebyli hodnoty obsaženy pro data v původní ztabulce - první
# maturita = pandas.merge(maturita, studenti, how='left') # přidám parametr, kterou tabulku zachovat celou?
# print(maturita.shape)
# preds = pandas.read_csv('predsedajici.csv')
# preds['den'] = preds['den'].str.strip()
# maturita = pandas.merge(maturita, preds, on=['den']) # pokud nejde spojit - musím přiradiut parametr podle čeho přidat
# print(maturita.tail())
# print(maturita.shape)
# print(preds) # zjišťuji, že 'po' má mezeru za
# maturita = maturita.rename(columns={'jmeno_x': 'jmeno', 'jmeno_y': 'predseda'}) # přejmenování sloupce
# print(maturita.head())

# výpočty z tabulky
# maturita_agreg = maturita.groupby('predmet').mean()
# maturita_agreg = maturita.groupby('predmet')['znamka'].mean()

# print(maturita_agreg)

# staty['population_density'] = staty['population'] / staty['area']
# staty = staty.sort_values('population_density', ascending=False) # ascending je parametr pro řazení
# print(staty.head())

