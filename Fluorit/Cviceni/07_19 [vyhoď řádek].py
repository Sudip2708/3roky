##  Napíš funkciu vyhod_riadok(meno_suboru, index),
##  ktorá z textového súboru odstráni zadaný riadok (index je číslo riadka od 0).
##  Ak sa index rovná -1, funkcia vyhodí posledný riadok.
##  Ak riadok so zadaným indexom neexistuje, funkcia nerobí nič.
##
##  Napríklad, pre 4-riadkový 'subor.txt' z predchádzajúceho príkladu, volanie:
##    >>> vyhod_riadok('subor.txt', 1)
##  odstráni riadok s indexom 1, teda druhý v poradí:
##    prvý riadok
##    predposledný
##    posledný riadok


#úvodní a prázdný řádek:
print('TEXTOVÉ SOUBORY - VYHOĎ ŘÁDEK')
print('funkce vypíše námi vybraný text, bez udaného řádku')
print('pokud chceš odstranit poslední řádek, napiš "-1"')
print()
print('jméno souboru pro otestování: 07_19.txt')
print('text 07_19.txt obsahuje 13 řádků s tím, že třetí je prázdný')
print()


#definování funkce:
def vyhod_riadok(meno_suboru, index):
    soubor = open(meno_suboru, 'r')             #načtení souboru
    cely = soubor.read()                        #uložení souboru do proměnné
    soubor.close()                              #zavření souboru
    novy = ''                                   #proměnná pro nový text
    pocet_r = cely.count('\n')                  #počet řádků
    index = index                               #číslo řádku, který se má vyhodit
    if index == -1:                             #podmínka - když index je -1
        index = pocet_r                         #použij index posledního řádku
    for i in range(pocet_r):                    #caklus - dle počtu řádků
        if i != index -1:                       #podmínka - pokud index řádku není shodný s indexem řádku, který se má odstranit
            novy += cely[:cely.find('\n')+1]    #zapiš do proměnné text čteného řádku
            cely = cely[cely.find('\n')+1:]     #odstraň tento řádek z čteného textu
        else:                                   #jinak
            cely = cely[cely.find('\n')+1:]     #odstraň tento řádek z čteného textu
    return(novy)                                #vrať nový text
      
       
#vstup:
meno_suboru = input('Zadej název souboru: ')
index = int(input('Zadej číslo řádku, který cheš vynechat: '))
if index == -1:
    cislo_radku = 'posledního'
else:
    cislo_radku = index


#výstup:
print()    
print(f'Zde je text ze souboru {meno_suboru} bez {cislo_radku} řádku:')
print()  
print(vyhod_riadok(meno_suboru, index))
     

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
