##  Napíš funkciu nahodne_cisla(meno_suboru, pocet).
##  Funkcia vytvorí textový súbor s trojcifernými náhodnými číslami (zrejme z intervalu <100, 999>).
##  V každom riadku bude jedno číslo, riadkov bude zadaný počet.
##
##  Napríklad volanie:
##    >>> nahodne_cisla('cisla1.txt', 5)
##  Vytvorí päťriadkový súbor 'cisla1.txt', ktorý môže obsahovať:
##    272
##    598
##    822
##    927
##    233
##  Otestuj takto vytvorený súbor s tvojou funkciu, ktorá počíta priemer, napríklad:
##    >>> nahodne_cisla('cisla2.txt', 100)
##    >>> print('priemer =', priemer('cisla2.txt'))
##    priemer = 540.58


#úvodní a prázdný řádek:
print('TEXTOVÉ SOUBORY - NÁHODNÁ ČÍSLA ULOŽENA DO SOUBORU')
print('''funkce dle námi zadaného jména vytvoří soubor a zapíše do něj
náhodně vygenerované trojmísná čísla, v námi zadaném počtu,
druhá funkce pak vrátí jejich průměr''')
print()
print('jméno souboru pro otestování: 07_14.txt')
print('počet čísel je zcela na nás :)')
print()


#definování funkce:
def nahodne_cisla(meno_suboru, pocet):
    import random
    soubor = open(meno_suboru, 'w')                     #vytvoření souboru
    for i in range(pocet):                              #cyklus - dlepočtu
        print(random.randint(100, 999), file=soubor)    #zapiš náhodné číslo
    soubor.close()                                      #uzavři soubor


#definování funkce:        
def priemer(meno_suboru): 
    soubor = open(meno_suboru)                          #načtení souboru
    součet = 0                                          #proměnná pro součet všech čísel
    řádků = 0                                           #proměnná pro počet řádků
    for řádek in soubor:                                #cyklus - pro řádek v souboru
        součet += int(řádek)                            #přičti hodnotu v řádku do součtu
        řádků += 1                                      #připočítej 1 do počtu řádků
    return součet / řádků                               #vrať průměr
    soubor.close()                                      #zavření souboru


#vstup:
meno_suboru = input('Zadej název souboru: ')
pocet = int(input('Zadej počet čísel: '))
nahodne_cisla(meno_suboru, pocet)


#výstup:
print()    
print(f'Do souboru {meno_suboru} bylo vygenerováno {pocet} náhodných trojmístných čísel.')
print('Jejich průměr je: ', priemer(meno_suboru))
     

#prázdný řádek a příkaz pro neuzavření okna
print()
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
