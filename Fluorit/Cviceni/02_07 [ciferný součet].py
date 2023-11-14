##  Celé číslo môžeme rozobrať na jednotlivé cifry tak,
##  že ho najprv prevedieme na reťazec
##  a potom vo for-cykle každú cifru (ako znak) zvlášť prevedieme na číslo.
##  Napíš program, ktorý prečíta celé číslo,
##  rozoberie ho na cifry,
##  tieto vypíše aj s poradovým číslom a zistí ich súčet.
##  Takýto súčet voláme ciferný súčet.
##
##  Po spustení dostaneš, napríklad:
##
##    zadaj číslo: 784
##    1. cifra 7
##    2. cifra 8
##    3. cifra 4
##    ciferný súčet je 19


#úvodní a prázdný řádek:
print('POSTUPKA Z HVĚZDIČEK')
print()


#vstupní data:
a = str(input('Zadej ČÍSLO a po té zmáční [Enter]: '))  #vstupní číslo + převod na text
b = 1                                                   #počítadlo jednotlivých čísel
c = 0                                                   #ciferný součet


#prázdný řádek
print()


#výpočet:
for i in a:                         
    print(f'{b}. cifra {i}')                            #výpis jednotlivých čísel
    b += 1                                              #přípočet k počítadlu jednotlivých čísel
    c += int(i)                                         #převod na číslo a přípočet k cifernému součtu
print()
print('Ciferný součet je', c)                           #výpis ciferného součtu
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')   
