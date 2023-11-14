##  Napíš funkciu vyhod_medzery(text), ktorá zo zadaného textu vyhodí všetky medzery.
##  Nepoužívajte žiadne funkcie ani operácie s reťazcami, ktoré sme sa ešte neučili.
##  Funkcia nič nevypisuje, ale pomocou return vráti nový reťazec.
##  Otestuj ju s rôznymi hodnotami parametrov.
##
##  Napríklad:
##    >>> vyhod_medzery('  mám   rád Python ')
##    'mámrádPython'
##    >>> vyhod_medzery('      ')
##    ''


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - VYHOĎ MEZERY')
print('funkce vynechá všechny mezery ve větě')
print()


#definování funkce:
def vyhod_medzery(text):
    text2 = ''                                  #promněná výsledného textu
    for i in text:                              #cyklus pro každý znak v textu
        if i != ' ':                            #podmínka - když znak není mezera
            text2 += i                          #přepiš znak do promněné výsledného textu    
    return text2                                #po skončení vrať výsledný text
            

#vstup:
text = input('Zadej nějakou větu: ')


#výstup:
print(f'Věta bez mezer by vypadal takto: {vyhod_medzery(text)}')
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  


