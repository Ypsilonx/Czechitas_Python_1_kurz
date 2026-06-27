#odkaz na cvičení https://kodim.cz/kurzy/python-data-1/ziskavani-dat/regularni-vyrazy/regularni-vyrazy

# import re
# # 1
# cislo_uctu = re.compile(r'\d{0,6}-?\d{6-10}/\d{4}')
# # 2
# cislo_uctu_banky = re.compile(r'\d{0,6}-?[12][0-2]\d{4,8}/2100')
# # 3
# kontrola_spz = re.compile(r'\d\D[\w] \d{4}')
# # 4
# kontrola_spz_spec = re.compile(r'\d[ABCEHJKLMPSTUZ]\w \d{4}')

# odkaz na cvičení v pythonu: https://kodim.cz/kurzy/python-data-1/ziskavani-dat/regularni-vyrazy/python-re

# import re

# regex_login = re.compile(r'[a-z]{1,8}$')

# login = input('Zadej LOGIN: ')

# spravnost = regex_login.fullmatch(login)
# if spravnost:
#     print('Login je OK.')
# else:
#     print('Login není OK.')
# ________________________________________
# regex_email = re.compile(r"\w+\.?\w+@\w+\.cz")
# regex_email = re.compile(r"(\w+\.?)+\w+@\w+\.cz")
# email = "info@czechitas.cz"

# hledani = regex_email.fullmatch(email)
# if hledani:
#     print("E-mail je v pořádku!")
# else:
#     print("Nesprávný e-mail!")
# ________________________________________
