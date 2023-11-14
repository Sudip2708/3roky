##6. Týždenný projekt
##L.I.S.T.
##•	riešenie odovzdaj na úlohový server https://list.fmph.uniba.sk/
##
##Programovací jazyk Logo, podobne ako my v Pythone, riadi korytnačku v grafickej ploche.
##Syntax jazyka sa ale trochu líši od Pythonu. Nás z Loga bude zaujímať len týchto 10 príkazov:
##•	fd 100 - zodpovedá pythonovskému t.fd(100), parametrom je výraz s hodnotou celého alebo desatinného čísla
##•	rt 45 - zodpovedá pythonovskému t.rt(45), parametrom je výraz s hodnotou celého alebo desatinného čísla
##•	lt 60 - zodpovedá pythonovskému t.lt(60), parametrom je výraz s hodnotou celého alebo desatinného čísla
##•	pu - zodpovedá pythonovskému t.pu(), príkaz je bez parametrov
##•	pd - zodpovedá pythonovskému t.pd(), príkaz je bez parametrov
##•	setpc 'red' - zodpovedá pythonovskému t.pencolor('red'),
##parametrom je znakový reťazec farby (pozor, môže obsahovať aj medzeru, napríklad 'light blue')
##•	setpw 5 - zodpovedá pythonovskému t.pensize(5), parametrom je výraz s hodnotou celého čísla
##•	repeat 4 [fd 50 rt 90] - označuje cyklus (s premennou cyklu repc) s daným počtom opakovaní
##(celé číslo, pritom premenná cyklu má začínať 1), telom cyklu môže byť ľubovoľný logovský program (aj prázdny),
##napríklad tento konkrétny repeat-cyklus sa môže preložiť takto:
##•	for repc in range(1, 5):
##•	    t.fd(50)
##•	    t.rt(90)
##•	to schod [fd 50 rt 90 fd 20 lt 90] - definuje funkciu schod bez parametrov,
##pričom telom môže byť ľubovoľný logovský program (aj prázdny),
##napríklad táto konkrétna definícia sa môže preložiť takto:
##•	def schod():
##•	    t.fd(50)
##•	    t.rt(90)
##•	    t.fd(20)
##•	    t.lt(90)
##•	každý iný identifikátor bude označovať volanie funkcie bez parametrov;,
##napríklad schod zodpovedá pythonovskému schod()
##Program v Logu môže byť naformátovaný úplne voľne, t.j. medzi príkazmi sú buď medzery alebo nové riadky
##a tak isto aj parametre sú od príkazov oddelené aspoň jednou medzerou alebo prázdnym riadkom,
##prípadne znakmi hranatých zátvoriek. Výrazy, ktoré sú parametrami príkazov, neobsahujú medzery,
##teda môžu mať tvar napríklad fd 10+repc. Môžeš predpokladať, že zadaný logovský program je korektný.
##Tvojou úlohou bude napísať pythonovský skript s funkciou logo2python(),
##ktorá dostane logovský program (textový súbor s príponou '.txt')
##a vyrobí z neho pythonovský skript (textový súbor s rovnakým menom, ale s príponou '.py'),
##ktorým by sa nakreslil identický obrázok s logovským programom.
##Napríklad, pre takýto vstupný súbor 'subor1.txt':
##pu lt 30 fd 100 lt 60 setpc
##'red' pd
##fd 100 rt 120 fd
##100    rt 120
##     fd 100 rt
##   60 setpc 'blue' fd 100 rt 120
##fd 100
##Tvoj program vygeneruje takýto pythonovský skript 'subor1.py':
##import turtle
##t = turtle.Turtle()
##t.pu()
##t.lt(30)
##t.fd(100)
##t.lt(60)
##t.pencolor('red')
##t.pd()
##t.fd(100)
##t.rt(120)
##t.fd(100)
##t.rt(120)
##t.fd(100)
##t.rt(60)
##t.pencolor('blue')
##t.fd(100)
##t.rt(120)
##t.fd(100)
##turtle.done()
##Alebo pre nejaký iný vstupný súbor:
##lt 90 pu fd 100 rt 30 pd
##to krok
##[fd 30 rt 120]
##
##repeat 4 [
##  fd 50
##  lt 10+20
##  repeat 3[krok]lt 60
##] rt 30 fd 70
##repeat 10[]
##dostaneme:
##import turtle
##t = turtle.Turtle()
##t.lt(90)
##t.pu()
##t.fd(100)
##t.rt(30)
##t.pd()
##def krok():
##    t.fd(30)
##    t.rt(120)
##for repc in range(1, 5):
##    t.fd(50)
##    t.lt(10+20)
##    for repc in range(1, 4):
##        krok()
##    t.lt(60)
##t.rt(30)
##t.fd(70)
##for repc in range(1, 11):
##    pass
##turtle.done()
##Tvoj odovzdaný program s menom riesenie.py musí začínať tromi riadkami komentárov:
### 6. zadanie: logo
### autor: Janko Hraško
### datum: 1.11.2021
##Modul musí obsahovať definíciu funkcie:
##def logo2python(meno_suboru, tab=4):
##    ...
##Túto funkciu bude volať testovač s rôznymi logovskými súbormi.
##Druhý parameter tab určuje o koľko medzier bude odsunutý každý vnorený blok príkazov vo for-cykle.
##Prázdne riadky vo výstupnom súbore sa budú ignorovať.
##Vo svojom module môžeš použiť aj ďalšie pomocné funkcie, nepoužívaj global.
##Projekt riesenie.py odovzdaj (bez ďalších dátových súborov) na úlohový server https://list.fmph.uniba.sk/ najneskôr do 23:00 12. novembra.
##Testovač bude spúšťať tvoju funkciu s rôznymi textovými súbormi, ktoré si môžeš stiahnuť z L.I.S.T.u. Za tento projekt môžeš získať 5 bodov.

# 6. zadanie: logo
# autor: Dalibor Sova
# datum: 22.2.2023
############################################################################


#úvodní text:
print('TÝDENÍ PROJEKT 12 LEKCE')
print(f'''Program slouží k převodu "želvých" instrukcí
napsaných v jazyce LOGO a uložených ve formátu .txt
do zápisu v jazyce python a následně je i uloží
pod stejným jménem ve formátu .py,
který v této ukázce i zpustí.

Program postupně načte, zpracuje, uloží
a následně i zpustí data z těchto dvou souborů:
12_16_s_1.txt
12_16_s_2.txt''')
print()
input('[zmáčkni [Enter] pro výpočet a překlad prvního souboru]')
print()


#rekurzivní funkce:
def logo2python(soubor):                                                #definice funkce pro převod turtlr programu napsaném v LEGO do jazyka Python
    prikazy = []                                                            #vyčištění seznamu pro jednotlivé příkazy
    t = open(soubor, 'r')                                                   #otevření textového souboru s turtle programem napsaným v LEGU
    nazev = str(soubor)                                                     #proměná pro název souboru - pro pozdější uložení programu v Pythonu
    text = t.read() + ' '                                                   #vložení textu do proměné s prázdným znakem na konci pro načtenbí posledního slova
    t.close()                                                               #zavření textového souboru 
    text = text.replace('\n', ' ')                                          #nahrazení v načteném textu všech znaků pro nový řádek za znak mezery
    text = text.replace('\t', ' ')                                          #nahrazení v načteném textu všech znaků pro tabulátor za znak mezery

    slovo = ''                                                              #proměná pro načítání znaků a následné předání jednotlivých slov (oddělených mezerou)
    for i in text:                                                          #cyklus - dle počtu znaků v zpracovávaném textu
        if i == ' ':                                                            #podmínka - pokud je zpracovávaným znakem mezera
            if slovo != '':                                                         #podmínka - pokud proměná 'slovo' není prázdná
                prikazy.append(slovo)                                               #předej obsah proměnné 'slovo' jako položku na konec seznamu 'prikazy'
                slovo = ''                                                          #vyprázdni obsah proměnné 'slovo'
        else:                                                                   #podmínka - pokud zpracovávaným znakem není mezera
            if i == '[' or i == ']':                                                #podmínka - pokud zpracovávaným znakem jsou lomené závorky
                if slovo != '':                                                         #podmínka - pokud proměná 'slovo' není prázdná             
                    prikazy.append(slovo)                                                   #předej obsah proměnné 'slovo' jako položku na konec seznamu 'prikazy'          
                    slovo = ''                                                              #vyprázdni obsah proměnné 'slovo'
                prikazy.append(i)                                                       #předej lomenou závorku jako položku na konec seznamu 'prikazy'  
            else:                                                                   #podmínka - pokud zpracovávaným znakem nejsou lomené závorky
                slovo += i                                                              #přidej znak do proměnné 'slovo'
        
    odsazeni = 0                                                            #proměnná pro počet odsazení v přepisu programu v Pythonu
    tabulátor = '    '                                                      #proměnná pro hodnotu odsazení - tabulátor = 4 mezery
    novy = ''                                                               #proměnná pro nový text přepisu programu do Pythonu

    novy += 'import turtle\n'                                               #přidej do proměnné 'nový' následující text
    novy += 't = turtle.Turtle()\n'                                         #přidej do proměnné 'nový' následující text
    for ix, i in enumerate(prikazy):                                        #cyklus s počítáním indexu - pro každou položku ze seznamu 'prikazy'
        if i == 'pu':                                                           #podmínka - pokud položka je rovna tomuto textu
            novy += f'{odsazeni*tabulátor}t.pu()\n'                                 #přidej do proměnné 'nový' následující text
        elif i == 'pd':                                                         #podmínka - pokud položka je rovna tomuto textu
            novy += f'{odsazeni*tabulátor}t.pd()\n'                                 #přidej do proměnné 'nový' následující text
        elif i == 'fd':                                                         #podmínka - pokud položka je rovna tomuto textu
            novy += f'{odsazeni*tabulátor}t.fd({prikazy[ix+1]})\n'                  #přidej do proměnné 'nový' následující text
        elif i == 'lt':                                                         #podmínka - pokud položka je rovna tomuto textu
            novy += f'{odsazeni*tabulátor}t.lt({prikazy[ix+1]})\n'                  #přidej do proměnné 'nový' následující text
        elif i == 'rt':                                                         #podmínka - pokud položka je rovna tomuto textu
            novy += f'{odsazeni*tabulátor}t.rt({prikazy[ix+1]})\n'                  #přidej do proměnné 'nový' následující text
        elif i == 'setpc':                                                      #podmínka - pokud položka je rovna tomuto textu
            novy += f'{odsazeni*tabulátor}t.pencolor({prikazy[ix+1]})\n'            #přidej do proměnné 'nový' následující text
        elif i == 'to':                                                         #podmínka - pokud položka je rovna tomuto textu
            novy += f'def {prikazy[ix+1]}():\n'                                     #přidej do proměnné 'nový' následující text
        elif i == 'repeat':                                                     #podmínka - pokud položka je rovna tomuto textu
            novy += f'{odsazeni*tabulátor}for i in range({prikazy[ix+1]}):\n'       #přidej do proměnné 'nový' následující text
        elif i == '[':                                                          #podmínka - pokud položka je rovna tomuto textu
            odsazeni += 1                                                           #změň hodnotu odsazení o +1
        elif i == ']':                                                          #podmínka - pokud položka je rovna tomuto textu
            if prikazy[ix-1] == '[':                                                #podmínka - pokud předchozí znak je otevřená lomená závorka
                novy += f'{odsazeni*tabulátor}pass\n'                                   #přidej do proměnné 'nový' následující text
            odsazeni -= 1                                                           #změň hodnotu odsazení o -1
        else:                                                                   #podmínka - ve všech ostatních případech
            if prikazy[ix-1] == '[' and prikazy[ix+1] == ']':                       #podmínka - pokud před znakem a za znakem jsou lomené závorky
                novy += f'{odsazeni*tabulátor}{i}()\n'                                  #přidej do proměnné 'nový' následující text
    novy += 'turtle.done()'                                                 #přidej do proměnné 'nový' následující text

    t = open(f'{nazev[:-4]}.py', 'w')                                       #otevření nového souboru s totožným názvem jako u čteného souboru pro zápis
    t.write(novy)                                                           #zápis do nového souboru
    t.close()                                                               #uzavření nového souboru

    print('Hotovo!')                                                        #oznam o splnění úkonu

prikazy = []                                                            #seznam pro jednotlivé příkazy

nazev_souboru = '12_16_s_1.txt'                                         #proměná pro název (případně i cestu) souboru s programem v LEGO
logo2python(nazev_souboru)                                              #volání funkce pro převod turtlr programu napsaném v LEGO do jazyka Python

print()
input('[zmáčkni [Enter] pro výpočet a překlad druhého souboru]')
print()

nazev_souboru = '12_16_s_2.txt'                                         #proměná pro název (případně i cestu) souboru s programem v LEGO
logo2python(nazev_souboru)                                              #volání funkce pro převod turtlr programu napsaném v LEGO do jazyka Python

print()
input('[zmáčkni [Enter] pro zpuštění prvního souboru]')
print()

import os                                                               #import modulu os
os.system('12_16_s_1.py')                                               #zpuštění programu

print()
input('[zmáčkni [Enter] pro zpuštění druhého souboru]')
print()

os.system('12_16_s_2.py')                                               #zpuštění programu
