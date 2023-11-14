##  Napíš pythonovský skript, ktorý bude definovať túto funkciu:
##    vypis(meno_suboru, sirka, zarovnat=True, slovo='')
##
##  Funkcia vypis() dostáva ako prvý parameter meno textového súboru
##  a druhým parametrom je celé číslo, ktoré udáva šírku výpisu.
##  Funkcia tento súbor prečíta a celý ho vypíše do textovej plochy
##  (do konzoly) tak, že bude zarovnaný na danú šírku.
##
##  Textový súbor sa skladá z odsekov, ktoré sa skladajú zo slov.
##  Odseky sú navzájom oddelené aspoň jedným prázdnym riadkom.
##  Slová v odseku sú navzájom oddelené aspoň jednou medzerou alebo koncom riadka.
##
##  Napríklad, "subor1.txt" sa skladá z týchto riadkov:
##    Ján Botto:
##      Žltá ľalija
##
##
##    Stojí, stojí mohyla.
##
##    Na mohyle   zlá    chvíľa,
##    na mohyle tŕnie,   chrastie
##     a v tom tŕní, chrastí rastie,
##      rastie, kvety rozvíja
##    jedna   žltá   ľalija.
##
##
##      Tá ľalija smutno vzdychá:
##
##      Hlávku moju tŕnie pichá
##     a  nožičky  oheň  páli —
##    pomôžte mi v mojom žiali!
##
##  Tento súbor obsahuje 5 „odsekov“, pričom najkratší je druhý a má 3 „slová“.
##  Najdlhší je tretí odsek má 20 slov.
##
##  Volanie vypis('subor1.txt', 20) vypíše:
##    Ján    Botto:   Žltá
##    ľalija
##
##    Stojí, stojí mohyla.
##
##    Na     mohyle    zlá
##    chvíľa,   na  mohyle
##    tŕnie,  chrastie a v
##    tom   tŕní,  chrastí
##    rastie,      rastie,
##    kvety  rozvíja jedna
##    žltá ľalija.
##
##    Tá   ľalija   smutno
##    vzdychá:
##
##    Hlávku   moju  tŕnie
##    pichá a nožičky oheň
##    páli  — pomôžte mi v
##    mojom žiali!
##
##  Pričom vypis('subor1.txt', 60) vypíše:
##    Ján Botto: Žltá ľalija
##
##    Stojí, stojí mohyla.
##
##    Na  mohyle  zlá  chvíľa,  na  mohyle tŕnie, chrastie a v tom
##    tŕní,  chrastí  rastie,  rastie,  kvety  rozvíja  jedna žltá
##    ľalija.
##
##    Tá ľalija smutno vzdychá:
##
##    Hlávku  moju  tŕnie pichá a nožičky oheň páli — pomôžte mi v
##    mojom žiali!
##
##  Všimni si, že všetky riadky v odseku okrem posledného sú zarovnané vpravo
##  na zadanú šírku, pričom, ak by bola dĺžka takéhoto riadka kratšia
##  ako zadaná šírka, medzi slová sú rovnomerne vložené medzery.
##  Ak nejaký riadok obsahuje len jedno slovo,
##  tak ani tento sa nezarovnáva na pravý okraj.
##  Ak je nejaké slovo dlhšie ako zadaná šírka,
##  tak toto slovo sa nerozdeľuje do viacerých riadkov,
##  ale bude v riadku výpisu jediné.
##
##  Funkcia vypis() má ešte ďalšie dva parametre,
##  ktoré majú určené aj náhradné hodnoty:
##
##  parameter zarovnat s hodnotou True pracuje tak, ako bolo popísané vyššie,
##  teda všetky riadky všetkých odsekov (okrem posledných a jednoslovných)
##  zarovnáva na pravý okraj.
##  Hodnota False označuje, že odseky sa na pravý okraj nezarovnávajú,
##  ale text ostáva „zubatý“.
##  Napríklad, volanie vypis('subor1.txt', 45, False) vypíše:
##    Ján Botto: Žltá ľalija
##
##    Stojí, stojí mohyla.
##
##    Na mohyle zlá chvíľa, na mohyle tŕnie,
##    chrastie a v tom tŕní, chrastí rastie,
##    rastie, kvety rozvíja jedna žltá ľalija.
##
##    Tá ľalija smutno vzdychá:
##
##    Hlávku moju tŕnie pichá a nožičky oheň páli —
##    pomôžte mi v mojom žiali!
##
##  ďalší parameter slovo s hodnotou '' označuje, že treba spracovať
##  (zarovnať, alebo nezarovnať) všetky odseky v súbore.
##  Iná hodnota označuje, že chceme spracovávať len tie odseky,
##  ktoré obsahujú toto konkrétne slovo.
##  Napríklad, volanie vypis('subor1.txt', 45, True, 'kvety')
##  vypíše len tento jeden odsek:
##    Na   mohyle  zlá  chvíľa,  na  mohyle  tŕnie,
##    chrastie   a  v  tom  tŕní,  chrastí  rastie,
##    rastie, kvety rozvíja jedna žltá ľalija.
##
##  Tvoj odovzdaný program s menom riesenie.py musí začínať
##  tromi riadkami komentárov (s tvojim menom a dátumom):
##    # 4. zadanie: zarovnaj
##    # autor: Janko Hraško
##    # datum: 29.10.2021
#################################################################################


# 4. zadanie: zarovnaj
# autor: Dalibor Sudip Sova
# datum: 15.9.2022


#úvodní a prázdný řádek:
print('TÝDENNÍ PROJEKT PRO 8. LEKCI')
print('''
Zadání programu bylo vytvořit funkci, která načte text ze souboru,
očistí ho o zdvojené mezery a naformátuje dle zadání.

V zadání funkce můžeme uvést následující hodnoty:
    soubor   = název souboru s textem
    sirka    = šířka řádku (počet znaků pro jeden řádek)
    zarovnat = zda má být text zarovnán od kraje do kraje
               True = bude zarovnáno (přednastavená volba)
               False = nebude zarovnáno
    slovo    = zde může být uvedeno slovo, které pokud se vyskytuje
               v textu, pak budou zpracovány jen ty odstavce, které
               toto slovo obsahují.

Pro vyzkoušení programu je zde připraven text "08_25.txt", který má
následující vstupní podobu:''')

print()
input('>>> zmáčkni [Enter] pro zobrazení textu <<<')
print('''
>>> Ján Botto:
      Žltá ľalija


    Stojí, stojí mohyla.

    Na mohyle   zlá    chvíľa,
    na mohyle tŕnie,   chrastie
     a v tom tŕní, chrastí rastie,
      rastie, kvety rozvíja
    jedna   žltá   ľalija.


      Tá ľalija smutno vzdychá:

      Hlávku moju tŕnie pichá
     a  nožičky  oheň  páli —
    pomôžte mi v mojom žiali! <<<
''')

print()
input('>>> zmáčkni [Enter] pro přístup k zadání parametrů <<<')
print()
print('-'*80)
print('''V následujících 4 krocích můžeš nastavit všechny parametry, a to i včetně
vlastního textu, který je ale třeba uvést i s celou přístupovou cestou.

[Pokud neuvedete žádný z parametrů, program vypíše přednastavené výpisy.] ''')
print()


#vstup dat:
print('''
1) Zadání názvu souboru.
Soubor, který je společně v adresáři s programem, takže stačí jen zadat
jeho název "08_25.txt", u všech ostatních souborů je potřeba uvést
i celou cestou.

(Parametr není třeba vyplňovat, stačí jen zmáčknout [Enter])''')
print()
a = input('Zadej název souboru: ')
print()
print('''
2) Zadání šířky řádku.
Zde je možné nastavit, kolik znaků má řádek.
Nejmenší možná šířka řádku pro soubor "08_25.txt" je 15 znaků.
(Nejdelší sousloví dvou slov a jedné mezery)
Při zadání nižší hodnoty, program se uzavře.

(Parametr není třeba vyplňovat, stačí jen zmáčknout [Enter])''')
print()
b = input('Zadej šířku řádku: ')
print()
print('''
3) Zadání zarovnání řádku.
Defaultně je nastavena hodnota "True", což znamená, že řádky budou roztařeny
od kraje do kraje. Pro zrušení tohoto nastavení zapiš "False"

(Parametr není třeba vyplňovat, stačí jen zmáčknout [Enter])''')
print()
c = input('Zadej zda zarovnat: ')
print()
print('''
4) Zadání hledaného slova.
Zde je možné zadat slovo, či část slova. Program potom vypíše jen ty odstavce,
které ho obsahují. V případě, že slovo nebude nalezeno, bude vypsán pouze oznam
o nenalezení slova.

(Parametr není třeba vyplňovat, stačí jen zmáčknout [Enter])''')
print()
d = input('Zadej hledané slovo: ')
print()
print()


#definice funkce vypis:
def vypis(meno_suboru, sirka, zarovnat=True, slovo=''):
    '''Funkce vypíše "text" načtený ze souboru v udané délce "sirka" řádku.
    Parametr "zarovnat" určuje, zda má být text zarovnán od kraje do kraje.
    Defaulně je nastaven na zarovnávání, pro zrušení je potřeba uvést hodnotu "False".
    Parametr "slovo" je-li vyplněn, vypíše pouze ty odstavce, které slovo obsahují.'''


    #definice podfunkce rozradkovat:
    def rozradkovat(text, sirka, zarovnat):
        '''Funkce rozřádkuje zadaný "text", dle hodnoty "sirka" a zarovná od kraje ke kraji.
        Zarovnání je možno zrušit uvedením hodnoty"False".'''

    #proměnné podfunkce rozradkovat:      
        t2 = text                                                               #kontejner pro text na rozřádkování
        si = sirka                                                              #šířka(počet znaků) jednoho řádku
        zr = zarovnat                                                           #zarovnat, či nezarovnat
        ns = novy_soubor = ''                                                   #kontejner pro nově upravený text
        rd = radek = ''                                                         #kontejner pro nově tvořený řádek
        dr = delka_radku = 0                                                    #počítadlo délky nově tvořeného řádku
        ds = delka_cteneho_slova = 0                                            #počítadlo délky čteného slova
        pz = predposledni_znak = ''                                             #kontejner pro přdchozí čtený znak
        cs = ctene_slovo = ''                                                   #kontejner pro dočasné umístění znaků posledního čteného slova (přesáhne-li řádek šířku)
        cd = 0                                                                  #kontejner pro hodnotu celočíselného dělení (při tvorbě zarovnaného řádku)
        zd = 0                                                                  #kontejner pro hodnotu zbytku po celočíselném dělení (při tvorbě zarovnaného řádku)
        dt = ''                                                                 #kontejner pro dočasný text (při tvorbě zarovnaného řádku) + (při výběru části pro zpracování)
        pm = 0                                                                  #přípočet mezery (1/0) dle zbytku po dělení (při tvorbě zarovnaného řádku)

    #výpočet podfunkce rozradkovat:
        for i in t2:                                                            #cyklus - pro každý znak z textu
            if i == ' ':                                                        #podmínka - když čtený znak je mezera
                if pz == ' ' or pz == '\n' or pz == 'n_n':                      #pod-podmínka - když v kontejneru pro předchozí čtený znak, je znak pro mezeru, nebo nový řádek, nebo je zde oznam ('n_n') o novém odstavci
                    pass                                                        #čtený znak vynech (zahoď)
                else:                                                           #pod-podmínka - když předchozí čtený znak, byl znak textu
                    rd, dr, ds, pz = rd+' ', dr+1, 0, i                         #přičti znak do řádku; přičti 1 do délky řádku; vynuluj hodnotu délky čteného slova; nastav mezeru jako předchozí čtený znak 
            elif i == '\n':                                                     #podmínka - když v kontejneru pro čtený znak je znak pro nový řádek
                if pz == '\n':                                                  #pod-podmínka - pokud předchozí čtený znak byl také znak pro nový řádek
                    ns += rd + '\n\n'                                           #přidej do nového textu obsah řádku a znak pro odstavec
                    rd, dr, ds, pz = '', 0, 0, 'n_n'                            #vyprázdni kontejner pro řádek; vynuluj počítadlo délky řádku; vynuluj počítadlo délky čteného slova; do kontejneru pro předchozí znak vlož oznam ('n_n') o novém odstavci
                elif pz == 'n_n':                                               #pod-podmínka - pokud v kontejneru pro předchozí znak je oznam o novém odstavci
                    pass                                                        #čtený znak vynech (zahoď)
                else:                                                           #pod-podmínka - když předchozí čtený znak, byl znak textu
                    rd, dr, ds, pz = rd+' ', dr+1, 0, '\n'                      #přičti mezeru do řádku; přičti 1 do délky řádku; vynuluj hodnotu délky čteného slova; nastav znak pro nový řádek, jako předchozí čtený znak 
            else:                                                               #podmínka - když v kontejneru pro předchozí čtený znak, není znak pro mezeru, nebo nový řádek, nebo oznam ('n_n') o novém odstavci
                rd, dr, ds, pz = rd+i, dr+1, ds+1, i                            #přičti znak do řádku; přičti 1 do délky řádku; přičti 1 do délky čteného slova; vlož (a nahrať) znak do kontejneru pro předchozí čtený znak
                if dr > si:                                                     #pod-podmínka - pokud délka (počet znaků)řádku je větší než uvedená šířka
                    cs, rd = rd[-ds:], rd[:-ds]                                 #vlož znaky posledního čteného slova do kontejneru pro poslední čtené slovo; a z kontejneru pro řádek, tyto znaky odeber
                    if zr == True:                                              #pod-pod-podmínka - pokud je možnost "zarovnat" v pozici "True"
                        rd = rd[:-1]                                            #odeber z řádku poslední znak (mezera)
                        cd = a =((si - len(rd)) // rd.count(' '))               #odečti z šířky délu řádku a celočíselně vyděl počtem mezer - výsledek vlož do kontejneru pro celočíselné dělení 
                        zd = b =((si - len(rd))  % rd.count(' '))               #zjisti zbytek po dělení a výsledek vlož do kontejneru pro zbytek po celočíselném dělení 
                        dt = ''                                                 #vyprázdnění kontejneru pro dočasný text
                        for i in range(rd.count(' ')):                          #cyklus - dle počtu mezer mezy slovy
                            if zd > 0:                                          #pokud zbytek po dělení je větší než 0
                                pm = 1                                          #do proměné pro přípočet mezery zapiš 1
                            dt += rd[:rd.find(' ')+1] + (' '*cd) + (' '*pm)     #výřez slova a přípočet mezer
                            rd = rd[rd.find(' ')+1:]                            #přiřazení slova s mezery do dočasného textu
                            zd, pm = zd-1, 0                                    #ze zbytku po dělení odešti 1; přípočet mezery změň na 0
                        ns += (dt + rd[rd.find(' ')+1:]  + '\n')                #přiřaď řádek a znaku pro nový řádek do nového souboru
                    else:                                                       #podmínka - pokud je možnost "zarovnat" v pozici "False"
                        ns += rd + '\n'                                         #přiřaď řádek a znaku pro nový řádek do nového souboru
                    rd, dr, cs = cs, len(cs), ''                                #přiřaď do vyprázdněného kontejneru pro řádek znaky posledního čteného slova; počet znaků přiřaď do délky řádku; vyprázdní kontejner pro čtené slovo
        return (ns + rd)                                                        #přiřaď do nového souboru poslední řádek a vrať "nový soubor" jako výsledek


    #definice podfunkce vyber_cast:
    def vyber_cast(text, slovo):
        'Funkce vybere a vrátí odstavec s prvním výskytem hledaného slova'

    #proměnné podfunkce vyber_cast: 
        t1 = text                                                               #kontejner pro text
        sl = slovo                                                              #kontejner pro hledané slovo
        us = t1.find(sl)                                                        #kontejner prohodnotu (index) umístění slova (prvního znaku)
        dt = ''                                                                 #vyprázdnění kontejneru pro dočasný text
        vt = ''                                                                 #kontejner pro výsledný text

    #výpočet podfunkce vyber_cast:
        if t1[us:].find('\n\n') != -1:                                          #podmínka - pokud se za pozicí umístění slova vyskytuje znak pro nový odstavec
            dt = t1[us:].find('\n\n')                                           #do kontejneru pro dočasný text vlož text od pozice prvního znaku hledaného slova až po znak pro nový odstavec
        else:                                                                   #podmínka - pokud se za pozicí umístění slova nevyskytuje znak pro nový odstavec (posední odstavec)
            dt = len(t1[us:])                                                   #do kontejneru pro dočasný text vlož text od pozice prvního znaku hledaného slova až po konec
        vt = t1[:us + dt]                                                       #do výsledného textu přiřaď část před pozicí umístění slova a přidej část z kontejneru pro dočasný text
        if vt.count('\n\n') > 0:                                                #podmínka - pokud výsledný text obsahuje alespoň 1 znak pro nový odstavec
            vt = vt[::-1]                                                       #převrať text (od zadu do předu)
            vt = vt[:vt.find('\n\n')]                                           #najdi první výskyt znaku pro nový řádek a použij jen text před ním
            vt = vt[::-1]                                                       #převrať text do správného pořadí (od předu do zadu)
        return vt.strip()                                                       #vrať výsledný text očištěný o mezery před a za


#proměnné funkce vypis:
    soubor = open(meno_suboru, 'r')                                             #načtení souboru
    t0 = soubor.read()                                                          #kontejner pro celý soubor
    soubor.close()                                                              #zavření souboru
    sl = slovo                                                                  #zástupce (zkratka) pro "slovo"
    si = sirka                                                                  #zástupce (zkratka) pro "sirka"
    zr = zarovnat                                                               #zástupce (zkratka) pro "zarovnat"

#výpočet funkce vypis:    
    if sl != '':                                                                #podmínka - pokud je hodnota "slovo" zadaná
        if t0.count(sl) == 0:                                                   #pod-podmínka - pokud slovo v textu nebylo nalezeno
            print('Slovo, které jste zadali, nebylo v textu nenalezeno.')       #vypiš tento text
        elif t0.count(sl) == 1:                                                 #pod-podmínka - pokud slovo se vyskytuje v textu pouze 1x
            print(rozradkovat(vyber_cast(t0, sl), si, zr))                      #pošli text do funkce "vyber_cast" - vygeneruj odstavec v kterém je obsaženo hledané slovo, pošli ho na zpracování (funkce "rozradkovat"), a vypiš výsledek
        else:                                                                   #pod-podmínka - pokud se slovo v textu vyskytuje více než 1x
            while t0.find(sl) != -1:                                            #cyklus - dokud text obsahuje hledané slovo
                print(rozradkovat(vyber_cast(t0, sl), si, zr), '\n')            #pošli text do funkce "vyber_cast" - vygeneruj odstavec v kterém je obsaženo hledané slovo, pošli ho na zpracování (funkce "rozradkovat"), a vypiš výsledek
                t0 = t0[t0.find(sl):][t0[t0.find(sl):].find('\n\n'):]           #najdi v textu hledané slovo a od něj vyhledej první výskat znaku pro nový odstavec a část před ním a včetně jeho, odeber z textu
    else:                                                                       #podmínka - pokud je hodnota "slovo" zadaná
        print(rozradkovat(t0, si, zr))                                          #pošli text do funkce "rozradkovaní" na rozřádkování a vypiš výsledek

#zpracování dat ze vstupu:
if a == '' and b == '' and c == '' and d == '':
    print('-'*80)
    print('Nebyla zadána žádná hodnota, následuje 7 příkladů různých zadání:')
    print()
    print()
    print('Ukázka č. 1: šířka 20 znaků + zarovnání:')
    print()
    input('>>> zmáčkni [Enter] pro zobrazení výsledku <<<')
    print()
    print('-'*20)
    vypis('08_25.txt', 20)
    print('-'*20)
    print()
    print()
    print('Ukázka č. 2: šířka 20 znaků + bez zarovnání:')
    print()
    input('>>> zmáčkni [Enter] pro zobrazení výsledku <<<')
    print()
    print('-'*20)
    vypis('08_25.txt', 20, False)
    print('-'*20)
    print()
    print()
    print('Ukázka č. 3: šířka 40 znaků + zarovnání:')
    print()
    input('>>> zmáčkni [Enter] pro zobrazení výsledku <<<')
    print()
    print('-'*40)
    vypis('08_25.txt', 40)
    print('-'*40)
    print()
    print()
    print('Ukázka č. 4: šířka 40 znaků + bez zarovnání:')
    print()
    input('>>> zmáčkni [Enter] pro zobrazení výsledku <<<')
    print()
    print('-'*40)
    vypis('08_25.txt', 40, False)
    print('-'*40)
    print()
    print()
    print('''Ukázka č. 5: šířka 40 znaků + bez zarovnání
+ hledané slovo "Botto" (první odstavec):''')
    print()
    input('>>> zmáčkni [Enter] pro zobrazení výsledku <<<')
    print()
    print('-'*40)
    vypis('08_25.txt', 40, False, 'Botto')
    print('-'*40)
    print()
    print()
    print('''Ukázka č. 6: šířka 40 znaků + bez zarovnání
+ hledané slovo "mohyl" (druhý a třetí odstavec):''')
    print()
    input('>>> zmáčkni [Enter] pro zobrazení výsledku <<<')
    print()
    print('-'*40)
    vypis('08_25.txt', 40, False, 'mohyl')
    print('-'*40)
    print()
    print()
    print('''Ukázka č. 7: šířka 40 znaků + bez zarovnání
+ hledané slovo "žiali" (poslední odstavec):''')
    print()
    input('>>> zmáčkni [Enter] pro zobrazení výsledku <<<')
    print()
    print('-'*40)
    vypis('08_25.txt', 40, False, 'žiali')
    print('-'*40)
    print()  
else:
    if a != '':
        meno_suboru = a
    else:
        meno_suboru = '08_25.txt'
    if b != '':
        sirka = int(b)
    else:
        sirka = 40
    if c != '':
        zarovnat = c
    else:
        zarovnat = True
    if zarovnat == True:
        zzz = 'ano'
    else:
        zzz = 'ne'
    if d != '':
        slovo = d
    else:
        slovo = ''
    if slovo == '':
        sss = 'neuvedeno'
    else:
        sss = slovo
    print('-'*sirka)
    print('Vaše zadání je:')
    print(f'Jméno souboru: {meno_suboru}')
    print(f'Šířka řádku:   {sirka}')
    print(f'Zarovnání:     {zzz}')
    print(f'Slovo:         {sss}')
    print('-'*sirka)
    print()
    vypis(meno_suboru, sirka, zarovnat, slovo)
    print('-'*sirka)

    
#prázdný řádek a příkaz pro neuzavření okna
print()
print('''A to je vše.
Děkuji za vyzkoušení programu a přeji příjemný den :-)''')
print()
print()
input('>>> zmáčkni [Enter] pro zavření okna <<<') 
