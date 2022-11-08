# with open('mereni.txt', 'r', encoding='utf-8') as file:
#     radky = file.readlines()
#     for radek in radky:
#         print(radek)

# with open('mereni.txt', 'r', encoding='utf-8') as file:
#     radky = file.readlines()    
    
# for radek in radky:
#     print(radek)

# for radek in radky:
#     print(radek.replace('.', ','))
#     print(radek.replace('\n', ''))
    
# radky_bez_newline = [radek.replace('\n', '').replace('\t', ' ') for radek in radky]
# print(radky_bez_newline)

# radky = [radek.split('\t') for radek in radky]
# print(radky)
# radky = [[radek[0], float(radek[1])] for radek in radky]
# print(radky)

jmena = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']

# with open('uzivatele.txt', mode='w', encoding='utf-8') as vystup:
#     vystup.writelines(jmena)
    
with open('uzivatele.txt', mode='w', encoding='utf-8') as vystup:
    # jmena_radky = [jmeno + '\n' for jmeno in jmena]
    # vystup.writelines(jmena_radky)
    
    for jmeno in jmena:
        vystup.write(jmeno + ' :D\n')