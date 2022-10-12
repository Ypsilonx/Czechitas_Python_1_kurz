# ukol-03: SMS brána
# Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

#Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
#Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
#Tvůj program bude obsahovat dvě funkce:

#První funkce ověří délku telefonního čísla. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). 
#Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili. 
#Pokud je číslo platné, funkce vrátí hodnotu True, jinak vrátí hodnotu False.
#Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
#Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. 
# Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

#Nápověda
#Pokud chcete zkontrolovat předvolbu, stačí využít podmínku+420 in cislo, alternativně můžete využít indexy: Python umožňuje kromě jednoho znaku z řetězce získat i více znaků, a to pomocí dvojtečky. Pokud budete chtít získat první čtyři znaky, napište cislo[0:4]. Pak můžete vytvořit podmínku cislo[0:4] == "+420".

# Bonus:
# Zkus svoji první funkci vytunit tak, že si bude umět poradit s mezerami v telefonním čísle. 
# Mezer se zbavíš tak, že použiješ replace() a tečkovou notaci. 
# První parametr je znak, který chceš nahradit, a druhý parametr nový znak. 
# Níže je příklad použití.

#tel_cislo = "+420 734 123 456"
#tel_cislo = tel_cislo.replace(" ", "")

tel_cislo = input('Zadej tel. číslo: ')

for i in tel_cislo:
    if i == ' ':
        tel_cislo = tel_cislo.replace(' ', '')

def cert_number(cislo):
    delka_cisla = len(cislo)
    return 'Ano' if (delka_cisla == 9) or (delka_cisla == 13) else 'Ne'
print(f'Číslo bylo zadáno správně? {cert_number(tel_cislo)}.')

sms_zprava = input('Text zprávy: ')

def cena(zprava):
    delka_zpravy = len(zprava)
    cena = int(delka_zpravy / 180) + 1
    return cena * 3

print(f'Cena zprávy je: {cena(sms_zprava)},- Kč.')
