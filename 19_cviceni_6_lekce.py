# 1. úkol:

# with open('vykaz.txt', encoding='utf-8') as vykaz:
#     hodiny = vykaz.readlines()

# hodiny = [int(hodina.strip()) for hodina in hodiny]
# print(hodiny) # a)
    
# hodinovka = input('Zadej kolik máš hodinovou mzdu: ')
# mzda = [(int(hodina)*int(hodinovka)) for hodina in hodiny]
# print(mzda) # b)
# prum_mzda = int(sum(mzda)/len(mzda))
# print(prum_mzda) # b)

# 2. úkol:

# with open('praha.txt', encoding='utf-8') as slohovka:
#     radky = slohovka.readlines()

# # print(radky)
# radky = [radek.strip().split(' ') for radek in radky]
# print(radky)

# for radek in radky:
#     print(len(radek))
    
# celkem = sum([len(radek) for radek in radky])
# print(celkem)

# 3. úkol:
with open('vykaz.txt', 'r', encoding='utf-8') as vykaz:
    hodiny = vykaz.readlines()

hodinovka = input('Zadej kolik máš hodinovou mzdu: ')
mzda = [(int(hodina)*int(hodinovka)) for hodina in hodiny]
print(mzda) # b)
prum_mzda = int(sum(mzda)/len(mzda))
print(prum_mzda) # b)

mzda_zapis = [str(vyplata) + '\n' for vyplata in mzda]

with open('vykaz1.txt', mode='w', encoding='utf-8') as vyplaty:
    ohodnoceni = [(hodina + 'h - ') for hodina in hodiny]
    ohodnoceni2 = [(mzda_zapisy + ',-Kč') for mzda_zapisy in mzda_zapis]
    hodnota = ohodnoceni + ohodnoceni2
    vyplaty.writelines(hodnota)
        
# 4. úkol:
