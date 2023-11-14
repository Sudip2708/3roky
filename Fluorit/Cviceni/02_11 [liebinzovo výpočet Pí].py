##  Výpočet pi podľa Liebnizovho vzorca je takýto súčet radu:
##
##    4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + 4/13 ...
##
##  Napíš program, ktorý vypočíta súčet tohto radu pre prvých n členov.
##
##  Po spustení môžeš dostať:
##
##    zadaj počet: 10
##    pi = 3.0418396189294032
##
##    zadaj počet: 100000
##    pi = 3.1415826535897198


#úvodní a prázdný řádek:
print('LIEBINZOVO VÝPOČET PI')
print()


#vstupní data:
a = int(input('Zadej POČET CYKLŮ a po té zmáční [Enter]: '))    #počet opakování
b = 1                                                           #proměná za lomítko
c = 0                                                           #součet
d = 2                                                           #počítadlo lichá / sudá


#prázdný řádek
print()


#výpočet:
for i in range(a):
    if d % 2 == 0:                                              #když "d" je sudá
        c += 4 / b                                              #připočti tento zlomek
    else:
        c -= 4 / b                                              #jinak odečti tento zlomek
    b += 2                                                      #zvýšení dělitele v zlomku o 2
    d += 1                                                      #zvíšení počítadla lichá / sudá o 1
print(f'Při {a} cyklů má Pí hodnotu: {c}')                     #výsledek
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
