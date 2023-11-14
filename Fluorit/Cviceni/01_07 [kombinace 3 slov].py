##  Napíš program, ktorý prečíta tri slová a vypíše všetkých6 rôznych permutácií.
##
##  Po spustení môžeš dostať:
##
##    zadaj 1. slovo: biela
##    zadaj 2. slovo: modrá
##    zadaj 3. slovo: červená
##    biela modrá červená
##    biela červená modrá
##    modrá biela červená
##    modrá červená biela
##    červená biela modrá
##    červená modrá biela


#úvod
print('KOMBINACE 3 SLOV')
print()


#získání slov:
a = input('Zadej 1. SLOVO a zmáčkni [Enter]: ')
b = input('Zadej 2. SLOVO a zmáčkni [Enter]: ')
c = input('Zadej 3. SLOVO a zmáčkni [Enter]: ')


#prázdný řádek
print()


#výpis konbinací slov:
print(f'''{a} {b} {c}
{a} {c} {b}
{b} {a} {c}
{b} {c} {a}
{c} {a} {b}
{c} {b} {a}''')


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
