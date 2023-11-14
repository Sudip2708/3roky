##  Napíš funkciu riadok(n, text=''),
##  ktorá vypíše n znakový reťazec hviezdičiek '*',
##  stred ktorého nahradí zadaným textom.
##  Ak je tento zadaný text neprázdny,
##  vloží na jeho začiatok aj koniec medzeru.
##
##  Napríklad pre volania:
##    sir = 40
##    riadok(sir)
##    riadok(sir, 'Ján Botto')
##    riadok(sir, 'Žltá ľalija')
##    riadok(sir, '‐')
##    riadok(sir, 'Stojí stojí mohyla')
##    riadok(sir, 'Na mohyle zlá chvíľa')
##    riadok(sir, 'na mohyle tŕnie chrastie')
##    riadok(sir, 'a v tom tŕní chrastí rastie')
##    riadok(sir)
##
##  dostaneme výstup:
##    ****************************************
##    ************** Ján Botto ***************
##    ************* Žltá ľalija **************
##    ****************** ‐ *******************
##    ********** Stojí stojí mohyla **********
##    ********* Na mohyle zlá chvíľa *********
##    ******* na mohyle tŕnie chrastie *******
##    ***** a v tom tŕní chrastí rastie ******
##    ****************************************


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - ŘÁDEK')
print('funkce do středu řádku vypíše zadaný text a kolem hvězdičky')
print()


#definování funkce:
def riadok(n, text=''):                             #parametry - šířka řádku, text
    if text == '':                                  #podmínka - když text není uveden
        print('*' * n)                              #vypiš hvězdičky násobené počtem "n"
    else:                                           #podmínka - když je text uveden
        a = len(text) + 2                           #zjisti délku textu a přičti k němu 2 volné mezery
        b = (n - a) // 2                            #zjisti délku hvězdiček před textem - odečti dálku textu od délky řádku a vyděl výsledek 2
        c = b + (n - a) % 2                         #zjisti délku hvězdiček před textem - k předchozímu výpočtu přičti zbytek po dělení
        print('*' * b, text, '*' * c)               #výstup
 

#vstup:
n = int(input('Zadej číslo šířky řádku: '))
b = input('Zadej text (pro * stačí zmáčknout [enter]): ')


#pomocný výpočet k vstupní hodnotě "b"
if b != '':
    text = b
else:
    text = ''


#výstup:
riadok(n, text)
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
    
