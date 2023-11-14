##  V premennej recept je zoznam, ktorého dĺžka je násobkom 3.
##  Napríklad:
##    recept = ['cukor', 100, 'g', 'vajíčka', 5, 'ks', 'mlieko', 2, 'dcl']
##  Napíš funkciu vypis_recept(zoznam),
##  ktorá takýto zoznam vypíše (pomocou print) do viacerých riadkov po troch,
##  napríklad:
##    vypis_recept(recept)
##    cukor 100 g
##    vajíčka 5 ks
##    mlieko 2 dcl
##  Funkcia nemodifikuje vstupný zoznam.
##  Svoje riešenie zapíš do troch riadkov:
##    def vypis_recept(zoznam):
##        for...
##          print(...


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - VÝPIS PO TŘECH')
print('funkce vypisuje položky ze seznamu po třech')
print()


#intro:
print('''předpřipravený seznam:
['cukor', 100, 'g', 'vajíčka', 5, 'ks', 'mlieko', 2, 'dcl']''')
print()
input('zmáčkni [enter] pro zobrazení seznamu po třech položkách')
print()


#definování funkce:
def vypis_recept(recept):
    'funkce vypíše 3 položkový seznam do jednotlivých řádků'
    for i in range(0, len(recept), 3):
        print(recept[i], recept[i+1], recept[i+2])


#seznam:
recept = ['cukor', 100, 'g', 'vajíčka', 5, 'ks', 'mlieko', 2, 'dcl']


#výstup:
vypis_recept(recept)
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')         
