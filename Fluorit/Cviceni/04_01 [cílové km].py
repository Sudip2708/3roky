##  Sportovec první den proběhl x kilometrů.
##  Každý další den proběhl o 10% více než v předchozí den.
##  Napiš program, který pro dané y zjistí,
##  v který den sportovec dohromady proběhne alespoň y kilometrů.
##
##  Například po spuštění můžeš dostat:
##    zadaj km pre prvý deň: 10
##    zadaj cieľové km: 20
##    na 9. deň prebehne 21.44 km


#úvodní a prázdný řádek:
print('UBĚHNUTÍ DANÉ VZDÁLENOSTI')
print('''program vypočítá den, dosáhnete cílové vzdálenosti, pokud každý den zaběhnete o 10% větší vzdálenost, než ten předchozí''')
print()


#vstupní data a proměné:
a = int(input('Zadej km pre první den: '))      #vstup km za první den
b = int(input('Zadej cílové km: '))             #vstup cílového počtu km na den
c = a                                           #přírusek každý den
d = 1                                           #počítadlo dní                       


#prázdný řádek
print()


#výpočet a výstup:
while c <= b:                                   #cyklus
    c *= 1.1                                    #denní přípočet km
    d += 1                                      #přípočet dnů

print(f'{d}. den zaběhne {c:.2f} km.')          #konečný výpis
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    
