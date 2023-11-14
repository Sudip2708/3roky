##    3. Týždenný projekt
##    L.I.S.T.
##    •	riešenie odovzdaj na úlohový server https://list.fmph.uniba.sk/
##
##    Napíš pythonovský skript, ktorý bude definovať tieto 4 funkcie:
##    •	funkcia pocet_dni_v_mesiaci(mesiac, priestupny=False) - vráti číslo od 28 do 31, pričom parameter mesiac je znakový reťazec, v ktorom sú dôležité len prvé tri znaky, tie sú 'jan', 'feb', 'mar', 'apr', 'maj', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'dec',
##    o	zrejme pocet_dni_v_mesiaci('feb', True) vráti 29
##    •	funkcia pocet_dni_medzi(datum1, datum2) - pre dva dátumy vypočíta počet dní, ktoré sú medzi nimi
##    o	oba dátumy sú zadané ako znakové reťazce v tvare 'mesiac.rok', pričom pre mesiac sú dôležité len prvé tri znaky
##    o	prvý dátum je vlastne 1.mesiac1.rok1, druhý dátum je 1.mesiac2.rok2
##    o	môžeš predpokladať, že prvý dátum je pred alebo rovný druhému dátumu; keď sa oba dátumy rovnajú, funkcia vráti 0
##    o	oba roky budú v intervale <1901, 2099>
##    o	napríklad:
##    o	>>> print(pocet_dni_medzi('sep.2020', 'okt.2020'))        # medzi 1.9.2020 a 1.10.2020
##    o	    30
##    o	>>> print(pocet_dni_medzi('okt.2019', 'okt.2020'))        # medzi 1.10.2019 a 1.10.2020
##    o	    366
##    o	>>> print(pocet_dni_medzi('januar.1999', 'oktober.2020')) # medzi 1.1.1999 a 1.10.2020
##    o	    7944
##    o	zrejme využiješ funkciu pocet_dni_v_mesiaci() a to, že priestupný rok (rok%4==0) má 366 dní a nepriestupný 365
##    •	funkcia den_v_tyzdni(datum), kde datum je znakový reťazec vo formáte 'den.mesiac.rok'
##    o	mesiac v tomto dátume je znakový reťazec, v ktorom sú dôležité len prvé tri znaky
##    o	funkcia vráti deň v týždni ako trojznakový reťazec, jeden z 'pon', 'uto', 'str', 'stv', 'pia', 'sob', 'ned'
##    o	môžeš to počítať tak, že najprv zistíš počet dní, ktoré uplynuli od dátumu 1.január.1901 a keďže vieme, že vtedy bol utorok, ľahko z toho vypočítaš deň v týždni (bude to nejaký zvyšok po delení 7)
##    o	môžeš predpokladať, že dátum bude zadaný korektne a bude z intervalu <1.jan.1901, 31.dec.2099>
##    o	napríklad:
##    o	>>> den_v_tyzdni('8.oktober.2021')
##    o	    'pia'
##    o	>>> den_v_tyzdni('1.jan.1901')
##    o	    'uto'
##    o	>>> den_v_tyzdni('23.jun.1912')
##    o	    'ned'
##    o	Vedel by si zistiť, čím je dátum 23. júna 1912 zaujímavý?
##    •	kalendar(datum) - vypíše (pomocou print()) kalendár pre jeden mesiac v takomto tvare
##    o	dátum je zadaný ako znakový reťazec v tvare 'mesiac.rok', pričom pre mesiac sú dôležité len prvé tri znaky
##    o	napríklad:
##    o	>>> kalendar('oktober.2021')
##    o	    pon uto str stv pia sob ned
##    o	                      1   2   3
##    o	      4   5   6   7   8   9  10
##    o	     11  12  13  14  15  16  17
##    o	     18  19  20  21  22  23  24
##    o	     25  26  27  28  29  30  31
##    o	>>> kalendar('maj.1945')
##    o	    pon uto str stv pia sob ned
##    o	          1   2   3   4   5   6
##    o	      7   8   9  10  11  12  13
##    o	     14  15  16  17  18  19  20
##    o	     21  22  23  24  25  26  27
##    o	     28  29  30  31
##    o	prvý riadok obsahuje mená dní v týždni presne v tomto tvare, ďalej nasledujú dni v mesiaci, ktoré sú naformátované presne do zodpovedajúcich stĺpcov
##    o	treba si dať pozor na medzery
##    Na otestovanie správnosti svojich funkcií môžeš využiť, napríklad tento štandardný modul:
##    >>> import calendar
##    >>> calendar.weekday(2021, 10, 8)      # 8.oktober 2021, vráti: 0=nedela, 1=pondelok, ...4=piatok
##        4
##    >>> calendar.day_name[calendar.weekday(2021, 10, 8)]
##        'Friday'
##    >>> calendar.prmonth(2021, 10, 3)      # oktober 2021, čísla na šírku 3 znaky
##                October 2021
##        Mon Tue Wed Thu Fri Sat Sun
##                          1   2   3
##          4   5   6   7   8   9  10
##         11  12  13  14  15  16  17
##         18  19  20  21  22  23  24
##         25  26  27  28  29  30  31
##    Tvoj odovzdaný program s menom riesenie.py musí začínať tromi riadkami komentárov (zmeň na svoje meno a dátum odovzdania):
##    # 3. zadanie: kalendár
##    # autor: Janko Hraško
##    # datum: 22.10.2021
##    V programe používaj len konštrukcie jazyka Python, ktoré sme sa učili na prvých 6 prednáškach. Nepoužívaj príkaz import.
##    Súbor riesenie.py odovzdaj na úlohový server https://list.fmph.uniba.sk/ najneskôr do 23:00 22. októbra, kde ho môžeš nechať otestovať. Môžeš zaň získať 5 bodov.


# 3. zadanie: kalendár
# autor: Dalibor Sova
# datum: 2.9.2022


#úvodní a prázdný řádek:
print('TÝDENNÍ PROJEKT PRO 6. LEKCI')
print('''program po zadání měsíce a roku v textové podobě
zobrazí příslušný měsíční kalendář''')
print()


#definice 1. funkce:
def pocet_dni_v_mesici(mesic, prestupny=False):
    if mesic == 'leden':                                            #podmínka - když je měsíc tato hodnota
        mesic = '031 000 031 000'                                   #začátek roku - 1.1.
    elif mesic == 'únor':
        mesic = '028 031 029 031'                                   #začátek roku - 1.2.
    elif mesic == 'březen':
        mesic = '031 059 031 060'                                   #začátek roku - 1.3.
    elif mesic == 'duben':
        mesic = '030 090 030 091'                                   #začátek roku - 1.4.
    elif mesic == 'květen':
        mesic = '031 120 031 121'                                   #začátek roku - 1.5.
    elif mesic == 'červen':
        mesic = '030 151 030 152'                                   #začátek roku - 1.6.
    elif mesic == 'červenec':
        mesic = '031 181 031 182'                                   #začátek roku - 1.7.
    elif mesic == 'srpen':
        mesic = '031 212 031 213'                                   #začátek roku - 1.8.
    elif mesic == 'září':
        mesic = '030 243 030 244'                                   #začátek roku - 1.9.
    elif mesic == 'říjen':
        mesic = '031 273 031 274'                                   #začátek roku - 1.10.
    elif mesic == 'listopat':
        mesic = '030 304 030 304'                                   #začátek roku - 1.11.
    else:
        mesic = '031 334 031 335'                                   #začátek roku - 1.12.

    if prestupny == True:                                           #podmínka - když je přestupný rok
        return mesic[8:]                                            #použij tyto hodnoty
    else:                                                           #jinak
        return mesic[:7]                                            #použij tyto hodnoty


#definice 2. funkce:
def pocet_dni_medzi(datum1, datum2):

    #promněné funkce:
    md1 = datum1[:datum1.find('.')]                                 #název měsíce datum1
    md2 = datum2[:datum2.find('.')]                                 #název měsíce datum2
    rd1 = int(datum1[datum1.find('.')+1:])                          #hodnota roku z datum1
    rd2 = int(datum2[datum2.find('.')+1:])                          #hodnota roku z datum2
    d1_pd = int(pocet_dni_v_mesici(md1, (rd1%4==0))[4:])            #počet dní v měsíci a od začátku roku pro datum1
    d2_pd = int(pocet_dni_v_mesici(md2, (rd2%4==0))[4:])            #počet dní v měsíci a od začátku roku pro datum2
    roky = 0

###následující dvě kontroly správného uvedení dat, jsou neaktivní, v této úloze nejsou potřeba, protože ke kontrole dochází v 4.funkci
##    #přehození datumů v případě, že první je rok je větší než druhý
##    if rd1 > rd2:                                                   #podmínka - pokud je první rok větší než druhý
##        md1, md2 = md2, md1                                         #prohoď měsíce
##        rd1, rd2 = rd2, rd1                                         #prohoď roky
##        d1_pd, d2_pd = d2_pd, d1_pd                                 #prohoď datumy
##
##    #přehození datumů v případě, kdy roky jsou stejné, ale první měsíc je větší než druhý
##    if rd1 == rd2 and d1_pd > d2_pd:                                #podmínka - pokud jsou roky stejné, ale první datum je větší než druhý
##        d1_pd, d2_pd = d2_pd, d1_pd                                 #prohoď datumy
    
    #spočítání dnů z roků
    for i in range (rd1, rd2):                                      #cyklus - pro každý rok
        if i % 4 == 0:                                              #podmínka - pokud je rok přestupný
            roky += 366                                             #připočti tuto hodnotu
        else:                                                       #jinak
            roky += 365                                             #připočítej tuto hodnotu

    #přípočet dní z měsíce
    if d1_pd > d2_pd:                                               #podmínka - pokud je 1. datum větší než 2.
        if rd1%4 == 0:                                              #pokud rok prvního datumu je přestupný
            return 366 - d1_pd + d2_pd + roky - 366                 #vrať tuto hodnotu (zbylé dny z 1. roku + dny posledního roku + roky - přestupný rok)
        else:                                                       #jinak
            return 365 - d1_pd + d2_pd + roky - 365                 #vrať tuto hodnotu (zbylé dny z 1. roku + dny posledního roku + roky - nepřestupný rok)
    else:                                                           #jinak
        return d2_pd - d1_pd + roky                                 #vrať tuto hodnotu (dny posledního roku - dny prvního roku + roky)


#definice 3. funkce:
def den_v_tyzdni(datum):
    
    #promněné funkce:
    den = int(datum[:datum.find('.')])                              #výpočet dne
    a = datum[datum.find('.')+1:]                                   #odebrání z datumu hodnoty pro den
    měsíc = a[:a.find('.')]                                         #výpočet měsíce
    rok = a[a.find('.')+1:]                                         #výpočet roku
    d1 = 'leden.1901'                                               #datum 1 - výchozí datum
    d2 = f'{měsíc}.{rok}'                                           #datum 2 - vypočítaný datum
    b = (pocet_dni_medzi(d1, d2) + den) % 7                         #promněná pro zbytek po dělení 7 z hodnoty funkce pocet_dni_medzi() a hodnoty dne

    #výpočet
    if b == 0:                                                      #pokud je promněná b rovna této hodnotě
        return 'pon'                                                #vrať tuto hodnotu
    if b == 1:
        return 'úte'
    if b == 2:
        return 'stř'
    if b == 3:
        return 'čtv'
    if b == 4:
        return 'pát'
    if b == 5:
        return 'sob'
    if b == 6:
        return 'ned'
    

#definice 4. funkce:
def kalendar(datum):

    #promněné funkce:
    m = datum[:datum.find('.')]                                     #promněná pro měsíc
    r = int(datum[datum.find('.')+1:])                              #promněná pro rok
    k = ''                                                          #proměná výsledného řetězce
    nr = "\n"                                                       #promněná pro nový řádek

    #kontrola správně zadaných údajů:
    if m not in ('leden', 'únor', 'březen', 'duben', 'květen', 'červen', 'červenec', 'srpen', 'září',  'říjen', 'listopat', 'prosinec'):
        print('Zadal jsi špatně měsíc - zadej celý název malími písmeny s diakritikou!')
        input('Program zobrazí neplatné výsledky! Je třeba program ukončit a spusit znovu!')
        print()
    if r not in range(1901, 2901):
        print('Zadal jsi špatně rok - rok musí být zadán 4 číslicemi v rozmezí let 1901 - 2901!')
        input('Program zobrazí neplatné výsledky! Je třeba program ukončit a spusit znovu!')
        print()
        
    #výpis kalendáře:
    print()
    print('pon', 'úte', 'stř', 'čtv', 'pát', 'sob', 'ned')          #vypsání prvního řádku
    for d in range(int(pocet_dni_v_mesici(m, (r%4==0))[:3])):       #cyklus - dle dní v měsíci
        if den_v_tyzdni(f'{d+1}.{m}.{r}') == 'pon':                 #podmínka - když funkce den_v_tyzdni() vrací tuto hodnotu
            k += f'{d+1:3} '                                        #přičti do výsledku tyto hodnoty
        elif den_v_tyzdni(f'{d+1}.{m}.{r}') == 'úte':
            if d == 0:
                k += f'{" "*4}{d+1:3} '
            else:
                k += f'{d+1:3} '
        elif den_v_tyzdni(f'{d+1}.{m}.{r}') == 'stř':
            if d == 0:
                k += f'{" "*8}{d+1:3} '
            else:
                k += f'{d+1:3} '
        elif den_v_tyzdni(f'{d+1}.{m}.{r}') == 'čtv':
            if d == 0:
                k += f'{" "*12}{d+1:3} '
            else:
                k += f'{d+1:3} '
        elif den_v_tyzdni(f'{d+1}.{m}.{r}') == 'pát':
            if d == 0:
                k += f'{" "*16}{d+1:3} '
            else:
                k += f'{d+1:3} '
        elif den_v_tyzdni(f'{d+1}.{m}.{r}') == 'sob':
            if d == 0:
                k += f'{" "*20}{d+1:3} '
            else:
                k += f'{d+1:3} '
        elif den_v_tyzdni(f'{d+1}.{m}.{r}') == 'ned':
            if d == 0:
                k += f'{" "*24}{d+1:3} '
            else:
                k += f'{d+1:3}{nr}'
    print(k)


#vstup:
datum = input('''Napiš jméno měsíce a roku ve formátu: květen.1945
(vše malýma písmenama s diakritikou, rok 4 číslicemi
a mezi měsícem a rokem je pouze tečka)

>>> ''')
kalendar(datum)


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
