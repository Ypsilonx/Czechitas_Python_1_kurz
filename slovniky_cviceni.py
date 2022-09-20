# 1. úkol:

# vysvedceni = {'Matematika': 1, 'Biologie': 2, 'Chemie': 1}
# print('Známky z předmětů:', 'Matika - ', vysvedceni['Matematika'], 'Biologie - ', vysvedceni['Biologie'], 'Chemie - ', vysvedceni['Chemie'])

# 2. úkol:

# sales = {
#     "Zkus mě chytit": 4165,
#     "Vrah zavolá v deset": 5681,
#     "Zločinný steh": 2565
# }
# print(sales)
# sales["Noc, která mě zabila"] = 0
# print(sales)
# sales["Vrah zavolá v deset"] += 100
# print(sales)

# 3. úkol:

# tombola = {
#     7: "Láhev kvalitního vína Château Headache",
#     15: "Pytel brambor z místního družstva",
#     23: "Čokoládový dort",
#     47: "Kniha o historii města",
#     55: "Šiška salámu",
#     67: "Vyhlídkový let balónem",
#     79: "Moderní televizor",
#     91: "Roční předplatné městského zpravodaje",
#     93: "Společenská hra Sázky a dostihy",
# }
# listek = int(input('Zadej své číslo lístku: '))

#1. varianta:

# if listek in tombola:
#     vyhra = tombola[listek]
#     tombola.pop(listek)
# else:
#     vyhra = "Bohužel nevyhráváš nic."

#2. varianta:

# vyhra = tombola.get(listek, 'Bohužel nevyhráváš nic.')
# tombola.pop(listek)

#3. varianta:

# vyhra = tombola.pop(listek, 'Bohužel nevyhráváš nic.')

# print(vyhra)
# print(tombola)

# BONUS:

passwords = {
    "Jiří": "tajne-heslo", 
    "Natálie": "jeste-tajnejsi-heslo", 
    "Klára": "nejtajnejsi-heslo"
}
login = input('Zadej své jméno: ')
if login in passwords:
    heslo = input('Napiš HESLO: ')
    if heslo == passwords.get(login):
        print('Smíš vstoupit.')
    else:
        print('Špatné heslo.')
else:
    print('Špatné jméno.')