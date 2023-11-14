##Zadefinuj triedu Cas,
##ktorá bude mať dva celočíselné atribúty hodiny a minuty.
##Aj inicializácia (metóda __init__()) bude mať dva parametre hodiny a minuty.
##Metóda vypis() vypíše nastavený čas v tvare čas je 9:17.
##Trieda Cas:
##class Cas:
##    ...
##Otestuj, napríklad:
##>>> c = Cas(9, 17)
##>>> c.vypis()
##    čas je 9:17
##>>> d = Cas(10, 5)
##>>> d.vypis()
##    čas je 10:05
##Zamysli sa, čo sa stane pre volanie Cas.vypis(c), čím sa to líši od c.vypis()?


#úvodní a prázdný řádek:                                                  
print('TŘÍDA - ČAS - 01')                              
print('''
Třída Cas obsahuje následující funkce:

1) inicializační funkce, která očekává hodnotu pro hodiny a minuty
a založení objektu instance třídy

2) metoda vypis(), která vypíše text s časem''')


class Cas:
    def __init__(self, hodiny, minuty):
        self.hodiny = hodiny
        self.minuty = minuty
        print(f'''>> Vytvořena instance třídy čas s hodnotami:
              hodiny - {self.hodiny}
              minuty - {self. minuty}''')

    def vypis(self):
        print(f'>> čas je {self.hodiny}:{self. minuty:02}')
    

print()
input("""zmáčkni [enter] pro zadání příkazu: c = Cas(9, 17)
(která založí instanci třídy 'c' s danými parametry času)""")
c = Cas(9, 17)


print()
input("""zmáčkni [enter] pro zadání příkazu: c.vypis()
(která vypíše text s časem)""")
c.vypis()


print()
input("""zmáčkni [enter] pro zadání příkazu: Cas.vypis(c)
(která vypíše text s časem - delší zápis)""")
Cas.vypis(c)


print()
input("""zmáčkni [enter] pro zadání příkazu: d = Cas(10, 5)
(která založí instanci třídy 'c' s danými parametry času)""")
d = Cas(10, 5)


print()
input("""zmáčkni [enter] pro zadání příkazu: d.vypis()
(která vypíše text s časem)""")
d.vypis()

print()
input("""zmáčkni [enter] pro zavření programu""")
