pisemky = [0, 2, 0, 1, 1, 3]

# pisemky_1 = []
# for znamka in pisemky:
#     pisemky_1.append(znamka + 1)
    
# print(pisemky_1)

# list comprehension:
# print([znamka + 1 for znamka in pisemky])
# mohu volat funkci pro prvky

# vložení podmínek:
pisemky_1 = []
for znamka in pisemky:
    nova_znamka = znamka
    if znamka == 0:
        nova_znamka += 1
    pisemky_1.append(nova_znamka)

print(pisemky_1)
print([znamka + 1 for znamka in pisemky if znamka == 0])

jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']

jmena_velka = [jmeno.upper() for jmeno in jmena]
print(jmena_velka)

#CVIČENI:
cisla = [1.12, 4.51, 2.64, 13.1, 0.1]

print([cislo*2 for cislo in cisla])
print([cislo*(-1) for cislo in cisla])
print([cislo**2 for cislo in cisla])
print([str(cislo) for cislo in cisla])

jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']

print([len(jmeno) for jmeno in jmena])
print([jmeno.upper() for jmeno in jmena])
print([jmeno + 'a' for jmeno in jmena])
print([jmeno.lower() + '@email.cz' for jmeno in jmena])

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

