##  Napíš funkciu spoj(zoznam),
##  ktorá z daného zoznamu vyrobí (a vráti) znakový reťazec.
##  V tomto reťazci budú všetky prvky zoznamu oddelené medzerami.
##  Funkcia nemodifikuje vstupný zoznam a nič nevypisuje.
##  Napríklad:
##    >>>ret = spoj(['vysledok', 23, '+', 321, 'je', 23+321])
##    >>>ret
##        'vysledok 23 + 321 je 344'
##    >>>spoj(list(range(100, 200, 13)))
##        '100 113 126 139 152 165 178 191'


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - SEZNAM NA TEXT')
print('''funkce vytvoří ze seznamu znakový řetězec,
kde jednotlivé položky seznamu,
jsou oddělené mezerou''')
print()


#definování funkce:
def spoj(seznam):
    vysledek = ''
    for i in seznam:
        vysledek += str(i) + ' '
    return vysledek


#intro:
print('Seznam pro ukázku použití funkce:')
print("['vysledok', 23, '+', 321, 'je', 23+321]")
print()
input('zmáčkni [enter] pro zobrazení textového řetězce')
print()

#výstup:
ret = spoj(['vysledok', 23, '+', 321, 'je', 23+321])
print(ret)
     

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
