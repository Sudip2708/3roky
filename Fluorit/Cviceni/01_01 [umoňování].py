##  Pomocou operácie ** vieme vypočítať mocniny čísel.
##  Ak je exponentom, napríklad zlomok 1/2, vypočítame tým druhú odmocninu čísla.
##  Zapíš v Pythone:
##
##    do premennej a1 priraď druhú odmocninu z 3
##    do premennej a2 priraď tretinu tretej odmocniny z 5
##    do premennej a3 priraď piatu mocninu piatej odmocniny z 1024
##    do premennej a4 priraď desiatu odmocninu z dvadsiatej mocniny 2
##
##  Hodnoty týchto štyroch premenných potom vypíš v tvare:
##
##  a1 = 1.7320508075688772

#úvod
print('ČTYŘI PŘÍKLADY')
print()
input('[zmáčkni [Enter] pro zobrazení příkladů]')
print()

#příklady
print('1) Druhá mocnina ze tří')
print('2) Třetina třetí odmocniny z pěti')
print('3) Pátá mocnina páté odmocniny z tisíc dvacet čtyři')
print('4) Desátá odmocnina z dvacáté mocniny dvou')

#prázdný řádek, příkaz pro zobrazení výsledků a prázdný řádek
print()
input('[zmáčkni [Enter] pro zobrazení výsledků]')
print()

#proměné
a1 = 3 ** (1/2)
a2 = (5 ** (1/3)) / 3
a3 = (1024 ** (1/5)) ** 5
a4 = (2 ** 20) **(1/10)

#výsledek
print('1) ', a1)
print('2) ', a2)
print('3) ', a3)
print('4) ', a4)

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
