##Do triedy Cas z (2) úlohy dopíš metódu pridaj(),
##ktorá bude mať 2 parametre hodiny a minuty.
##Metóda pridá k uloženému času zadané hodiny a minúty.
##Napríklad:
##>>> cas = Cas(17, 40)
##>>> print('teraz je', cas.str())
##    teraz je 17:40
##>>> cas.pridaj(1, 35)
##>>> print('neskôr', cas.str())
##    neskôr 19:15


#úvodní a prázdný řádek:                                                  
print('TŘÍDA - ČAS - 03')                              
print('''
Třída Cas obsahuje následující funkce:

1) inicializační funkce, která očekává hodnotu pro hodiny a minuty
a založení objektu instance třídy

2) metoda vypis(), která vypíše text s časem

3) metoda str(), která vrátí hodnotu času jako textový soubor

4) metoda pridaj(hodiny, minuty), která změní původní hodnotu času,
přičtením hodnot hodin a minut''')




class Cas:
    def __init__(self, hodiny, minuty):
        self.hodiny = hodiny
        self.minuty = minuty
        print(f'''>> Vytvořena instance třídy čas s hodnotami:
              hodiny - {self.hodiny}
              minuty - {self. minuty}''')

    def vypis(self):
        print(f'>> čas je {self.hodiny}:{self. minuty}')

    def str(self):
        return f'{self.hodiny}:{self. minuty:02}'

    def pridaj(self, hodiny, minuty):
        m = (self.minuty + minuty + 60)%60
        m_h = (self.minuty + minuty)//60
        h = (self.hodiny + hodiny + m_h + 24)%24
        self.hodiny = h
        self.minuty = m
        print(f'>> čas byl posunut o {hodiny} hodin a {minuty} minut')

print()
input("""zmáčkni [enter] pro zadání příkazu: cas = Cas(17, 40)
(která založí instanci třídy 'c' s danými parametry času)""")
cas = Cas(17, 40)

print()
input("""zmáčkni [enter] pro zadání příkazu: print('teraz je', cas.str())
(která vypíše text s časem, nyní je však čas jen hodnotou
ve funkci print())""")
print('teraz je', cas.str())

print()
input("""zmáčkni [enter] pro zadání příkazu: cas.pridaj(1, 35)
(která posune čas o zadané hodnoty)""")
cas.pridaj(1, 35)

print()
input("""zmáčkni [enter] pro zadání příkazu: print('neskôr', cas.str())
(která vypíše text s časem, nyní je však čas jen hodnotou
ve funkci print())""")
print('neskôr', cas.str())

print()
input("""zmáčkni [enter] pro zavření programu""")
