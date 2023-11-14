##  Napíš funkciu rozsekaj(text, sirka),
##  ktorá vypíše zadaný text do viacerých riadkov,
##  pričom každý (možno okrem posledného) má presne sirka znakov.
##
##  Napríklad:
##    >>>ret = rozsekaj('Anicka dusicka, kde si bola', 10)
##    >>>ret
##        'Anicka dus\nicka, kde \nsi bola'
##    >>>print(ret)
##        Anicka dus
##        icka, kde
##        si bola


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - ROZŘÁTKOVÁNÍ')
print('funkce dle zadané délky řádku rozřádkuje zadaný text')
print()


#definování funkce:
def rozsekaj(text, sirka):
    '''Funkce vypíše zadaný text do řádků dle požadovaného počtu znaků.'''
    vysledek = ''                   #proměnná pro výsledný text
    while len(text) != 0:           #cyklus - dokud není původní text prázdný
        vysledek += text[:sirka]    #přidej k výslednému textu z textu daný počet znaků
        vysledek += '\n'            #zapiš za ně znak pro odskočení na nový řádek
        text = text[sirka:]         #odeber již zpracovaný text z původního textu
    return vysledek                 #vrať výsledek


#vstup:
text = input('Zadej text, který chceš rozřádkovat: ')
sirka = int(input('Zadej šířku řádku: '))


#výstup:
print(rozsekaj(text, sirka))
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
