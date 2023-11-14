##  V jednom starodávnom príbehu sa na políčka šachovnice kládli zrniečka ryže:
##  na 1. políčko 1 zrnko ryže, na ďalšie 2,
##  na každom ďalšom je dvojnásobok predchádzajúceho.
##  Napíš program, ktorý vypíše, koľko zrniek bude na n-tom políčku.
##
##  Po spustení môžeš dostať:
##
##    zadaj n: 5
##    na 5. políčku bude 16 zrniek ryže
##
##  Všimni si, že za poradovým číslom vo výpise je bodka (5.)
##  a je to zapísané bez medzery.
##
##  Zisti počet zrniek ryže na 64. políčku šachovnice.
##  Odhadni koľko je to ton ryže, keď 50 zrniek váži asi 1 gram.


#úvod
print('VÝPOČET ZRNEK RÝŽÍ NA ŠACHOVNICI')
print()


#vstupní data:
a = int(input('Zadej ČÍSLO POLE ŠACHOVNICE a zmáčkni [Enter]: '))


#výpočet:
b = 2 ** (a - 1)        #výpočet kolik je zrnek rýže na daném políčku
c = b // 50             #výpočet hmotnosti (gramy)
d = c / 1000000         #výpočet hmotnosti (tuny)


#prázdný řádek
print()


#výpis:
print(f'Na {a}. políčku bude {b} zrnek rýže')
print(f'To je přibližně {c} gramů')
print(f'To je přibližně {d} tun')


#prázdný řádek a příkaz k potvrzení zobrazení tabulky:
print()
input('Zmáčkni [Enter] pro vypsání tabulky pro celou šachovnici: ')


#prázdný řádek
print()


#bonus - tabulka celé šachovnice
for i in range(65):
    x1 = 2 ** (i - 1)
    x2 = x1 // 50
    x3 = x2 / 1000000
    if i == 0:
        print()
    else:
        print(f'{i:2}.pole {x1:19}-zrnek {x2:18}-gramů {x3:15.2f}-tun')
    

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
