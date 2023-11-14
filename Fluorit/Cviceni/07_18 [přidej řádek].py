##  Napíš funkciu pridaj(meno_suboru, text),
##  ktorá do textového súboru pridá na koniec nový riadok so zadaným textom.
##
##  Napríklad, ak súbor obsahoval riadky:
##    prvý riadok
##    druhý riadok
##  potom volania:
##    >>> pridaj('subor.txt', 'predposledný')
##    >>> pridaj('subor.txt', 'posledný riadok')
##  zmenia tento súbor:
##    prvý riadok
##    druhý riadok
##    predposledný
##    posledný riadok


#úvodní a prázdný řádek:
print('TEXTOVÉ SOUBORY - PŘIDEJ ŘÁDEK')
print('funkce přidá do námi zadaného souboru řádek s námi zadaným textem')
print()
print('jméno souboru pro otestování: 07_18.txt')
print('text je zcela na nás :)')
print()


#definování funkce:
def pridaj(meno_suboru, text):
    soubor = open(meno_suboru, 'a')     #otevření souboru pro přípis
    soubor.write(text + '\n')           #přípis textu
    soubor.close()                      #zavření souboru


#vstup:
meno_suboru = input('Zadej název souboru: ')
text = input('Zadej text který chceš přidat: ')
pridaj(meno_suboru, text)


#výstup:
print()    
print(f'''Gratuluji, právě jsi přidal do textového souboru {meno_suboru}
tento řádek: {text}''')
print()
print('''Pokud jsi použil jméno souboru pro otestování, výsledný textový soubor
nalezneš ve stejné složce jako je tento program.''')
     

#prázdný řádek a příkaz pro neuzavření okna
print()
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
