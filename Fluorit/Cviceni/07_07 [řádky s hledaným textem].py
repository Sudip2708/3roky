##  Napíš funkciu riadky_s_textom(meno_suboru, text),
##  ktorá otvorí zadaný súbor (môže byť aj súbor s pythonovským programom)
##  a vypíše z neho len tie riadky, ktoré obsahujú zadaný text.
##
##  Napríklad:
##    >>> riadky_s_textom('riesenie.py', 'if ')
##    if a != b:
##        serif = 1517
##    elif b < 7:
##        if x:
##    >>> riadky_s_textom('text3.txt', 'ali')
##    Žltá ľalija
##    jedna žltá ľalija
##    Tá ľalija smutno vzdychá
##    pomôžte mi v mojom žiali


#úvodní a prázdný řádek:
print('TEXTOVÉ SOUBORY - VÝPIS ŘÁDKŮ S HLEDANÝM TEXTEM')
print('funkce načte námi uvedený soubor a vypíše z něj ty řádky, které obsahují námi uvedené znaky')
print()
print('jméno souboru pro otestování: 07_07.txt')
print('hledaný text pro otestování: ali')
print()


#definování funkce:
def riadky_s_textom(meno_suboru, text):
    soubor = open(meno_suboru)          #proměnná pro otevření souboru
    výsledek = ''                       #proměnná pro výsledek
    for řádek in soubor:                #cyklus - pro řádek v souboru
        if řádek.find(text) != -1:      #podmínka - když řádek obsahuje text
            výsledek += řádek           #přičtii řádek do výsledku
    return výsledek                     #vrať výsledek


#vstup:
meno_suboru = input('Zadej název souboru: ')
text = input('Zadej nhledaný výraz: ')


#výstup:
print()
print('Hledaný text obsahují tyto řádky:')
print()
print(riadky_s_textom(meno_suboru, text))
     

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')              
