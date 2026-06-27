import pandas

jmena = pandas.read_csv('soubory_k_praci/jmena.csv')
s1 = pandas.read_csv('soubory_k_praci/studenti1.csv')
s2 = pandas.read_csv('soubory_k_praci/studenti2.csv')

set_studenti = pandas.concat([s1, s2], ignore_index=True)
print(set_studenti)

nestudenti = set_studenti[set_studenti['ročník'].isnull()]
print(nestudenti.shape)
dalkove_studium = set_studenti[set_studenti['kruh'].isnull()]
print(dalkove_studium.shape)

nuly = set_studenti[(set_studenti["ročník"].isnull() | set_studenti["kruh"].isnull())]
print(nuly.shape)

s1 = pandas.read_csv("soubory_k_praci/studenti1.csv").dropna()
s2 = pandas.read_csv("soubory_k_praci/studenti2.csv").dropna()

prezencni_stud = pandas.concat([s1, s2], ignore_index=True)
print(prezencni_stud)

prezencni_obory = prezencni_stud.groupby('obor').count()
print(prezencni_obory['jméno'])

prezencni_obory = prezencni_stud.groupby('obor')['prospěch'].mean()
print(prezencni_obory)

prezencni_stud = pandas.merge(prezencni_stud, jmena)
print(prezencni_stud)
pohlavi = prezencni_stud.groupby('pohlaví')['jméno'].count()
print(pohlavi)