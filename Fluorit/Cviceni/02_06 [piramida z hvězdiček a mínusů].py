##  Aj v tejto úlohe treba napísať program, ktorý vytvorí pyramídu z hviezdičiek,
##  len z hviezdičiek bude len obvod trojuholníka,
##  vnútro trojuholníka bude zo znakov mínus ('-').
##
##  Môžeš dostať takýto výstup:
##
##    zadaj n: 7
##          *
##         *-*
##        *---*
##       *-----*
##      *-------*
##     *---------*
##    *************


#úvodní a prázdný řádek:
print('PYRAMIDA Z HVĚZDIČEK A MÍNUSŮ')
print()


#vstupní data:
a = int(input('Zadej POČET ŘÁDKŮ a po té zmáční [Enter]: '))


#prázdný řádek
print()


#počítadla:
b = 2                                           #počítadlo mezer v cyklu
c = 1                                           #počet mínusů mezi hvězdičkami


#výpočet:
print ((a - 1) * ' ' + '*')                     #výpis prvního řádku

for i in range(a - 2):                          #cyklus
    print((a - b) * ' ' + '*' + c * '-' + '*')  #výpis druhého až předposledního řádku
    b += 1                                      #přípočet k počítadlu mezer
    c += 2                                      #přípočet k počítadlu mínusů

print ((a * 2 - 1) * '*')                       #výpis posledního řádku
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
