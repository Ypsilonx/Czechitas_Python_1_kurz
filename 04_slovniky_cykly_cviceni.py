# 1. úkol:
# import statistics

# school_report = {
#     "Český jazyk": 1,
#     "Anglický jazyk": 1,
#     "Matematika": 1,
#     "Přírodopis": 2,
#     "Dějepis": 1,
#     "Fyzika": 2,
#     "Hudební výchova": 4,
#     "Výtvarná výchova": 2,
#     "Tělesná výchova": 3,
#     "Chemie": 4,
# }

# pocet_jednicek = list(school_report.values()).count(1)
# print(pocet_jednicek)
# bez funkce list - máme pouze dict_values a nelze použit count

# 1.varianta:

# prumer_znamek = statistics.mean(school_report.values())
# print(prumer_znamek)

# predmety = len(school_report)
# print(predmety)
# znamky = sum(school_report.values())
# print(znamky)
# prumer_znamek = znamky/predmety
# print(f'Průměrná známka z vysvědčení je {prumer_znamek}.')

# celk_znamka = 0
# pocet_znamek = 0
# for predmet in school_report:
#     celk_znamka += school_report[predmet]
#     pocet_znamek += 1
#     print(f'{predmet}')
# avg_znamka = celk_znamka/pocet_znamek
# print(f'Průměrná známka z vysvědčení je {avg_znamka}.')

# celk_znamka = 0
# pocet_znamek = 0
# for predmet, znamka in school_report.items():
#     celk_znamka += znamka
#     pocet_znamek += 1
#     print(f'{predmet}')
# avg_znamka = celk_znamka/pocet_znamek
# print(f'Průměrná známka z vysvědčení je {avg_znamka}.')

# 2.varianta:

# celk_znamka = 0
# pocet_znamek = 0
# for predmet, znamka in school_report.items():
#     celk_znamka += znamka
#     pocet_znamek += 1
#     if znamka == 1:
#         print(f'Jedničku má z předmětu {predmet}.')
# avg_znamka = celk_znamka/pocet_znamek
# print(f'Průměrná známka z vysvědčení je {avg_znamka}.')

# 2. úkol:

# books = [
#     {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
#     {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
#     {"title": "Past", "pages": 390, "rating": 4},
#     {"title": "Popel popelu", "pages": 411, "rating": 10},
#     {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
#     {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
#     {"title": "Zločinný steh", "pages": 542, "rating": 8},
#     {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
#     {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
# ]

# 1.varianta:

# pocet_stranek = 0
# for stranky in books:
#     pocet_stranek += stranky['pages']
# print(f'Gustav přečetl celkem {pocet_stranek} stránek ze všech knížek.')

# 2.varianta:

# pocet_stranek = 0
# pocet_knih = 0
# for knihy in books:
#     pocet_stranek += knihy['pages']
#     if knihy['rating'] >= 8:
#         pocet_knih += 1
# print(f'Gustav přečetl celkem {pocet_stranek} stránek ze všech knížek. Knížek s hodnocením nad 8 je {pocet_knih}.')

# BONUS:

# plates = {
#     "4A2 3000": "František Novák",
#     "6P5 4747": "Jana Pilná",
#     "3B7 3652": "Jaroslav Sečkár",
#     "1P5 5269": "Marta Nováková",
#     "37E 1252": "Martina Matušková",
#     "2A5 2241": "Jan Král"
# }

# znak_plzen = 'P'
# for spz, jmeno in plates.items():
#     if spz[1] == znak_plzen:
#         print(f'Auto je registrováno v Plzni se jménem {jmeno}.')