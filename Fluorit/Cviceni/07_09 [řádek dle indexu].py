##  Napíš funkciu ity(meno_suboru, index),
##  ktorá z daného súboru vráti (return) riadok s daným poradovým číslom (index).
##  Riadky číslujeme od 0.
##
##  Napríklad:
##    >>> ity('text1.txt', 2)
##    '- ze ho pouzivame.'
##    >>> ity('text2.txt', 0)
##    'Tri zakladne zakony robotiky.'
##    >>> ity('text3.txt', 3)
##    'Stojí stojí mohyla'


#úvodní a prázdný řádek:
print('TEXTOVÉ SOUBORY - ŘÁDEK DLE INDEXU')
print('funkce vrátí z uvedeného textu, odpovídající řádek')
print()
print('jméno souboru pro otestování: 07_09.txt')
print('možnost volby řádku: 1 - 13, s tím, že 3. řádek je prázdný')
print()


#definování funkce:
def ity(meno_suboru, index):
    soubor = open(meno_suboru)          #proměnná pro otevření souboru
    for i, text in enumerate(soubor):   #cyklus - pro řádek v textu + index řádku
        if i == index:                  #podmínka - pokud index řádkku odpovídá indexu ze zadání
            return text                 #vrať daný řádek
    soubor.close()                      #zavření souboru


#vstup:
meno_suboru = input('Zadej název souboru: ')
index = int(input('Zadej číslo hledaného řádku: '))-1


#výstup:
print()    
print(f'Na řádku č. {index+1} je uveden tento text:')
print(ity(meno_suboru, index))
     

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
