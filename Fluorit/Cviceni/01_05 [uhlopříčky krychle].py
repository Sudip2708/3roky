##  Napíš program, ktorý prečíta veľkosť strany kocky
##  a vypíše dĺžku stenovej a telesovej uhlopriečky - obe tieto dĺžky
##  zaokrúhli na 2 desatinné miesta (využiješ funkciu round).
##
##  Po spustení môžeš dostať:
##
##    zadaj veľkosť strany kocky: 18
##    stenová uhlopriečka je 25.46
##    telesová uhlopriečka je 31.18


#úvod
print('VÝPOČET STĚNOVÉ A TĚLESOVÉ UHLOPŘÍČKY KRYCHLE')
print()


#získání strany kostky:
a = float(input('Zadej VELIKOST STRANY KRYCHLE a zmáčkni [Enter]: '))


#prázdný řádek
print()


#zaokrouhlený výpočet stěnové uhlopříčky (a√2):
print(f'STĚNOVÁ UHLOPŘÍČKA je {round(a * (2**(1/2)),2)}')


#zaokrouhlený výpočet tělesové uhlopříčky (a√3):
print(f'TĚLESOVÁ UHLOPŘÍČKA je {round(a * (3**(1/2)),2)}')


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')

