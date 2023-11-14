##Napíš globálnu funkciu (nie metódu) neskor(cas, hodiny, minuty),
##ktorá vytvorí (return) novú inštanciu triedy Cas.
##Táto nová inštancia bude od zadaného času
##(parameter cas je tiež inštancia triedy Cas)
##posunutá o zadaný počet hodín a minút.
##Využi metódu pridaj().
##Napríklad:
##>>> c = Cas(17, 40)
##>>> d = neskor(c, 2, 55)
##>>> print(c.str())
##    17:40
##>>> print(d.str())
##    20:35


#úvodní a prázdný řádek:                                                  
print('TŘÍDA - ČAS - 04')                              
print('''
Třída Cas obsahuje následující funkce:

1) inicializační funkce, která očekává hodnotu pro hodiny a minuty
a založení objektu instance třídy

2) metoda vypis(), která vypíše text s časem

3) metoda str(), která vrátí hodnotu času jako textový soubor

4) metoda pridaj(hodiny, minuty), která změní původní hodnotu času,
přičtením hodnot hodin a minut

Dále program obsahuje i jednu vnbější funkci:
neskor(cas, hodiny, minuty),
která vytvoří novou instanci třídy Čas,
kde čas posune o zadaný počet hodin a minut.
''')




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

def neskor(cas, hodiny, minuty):
    novy = Cas(cas.hodiny, cas.minuty)
    novy.pridaj(hodiny, minuty)
    return novy


print()
input("""zmáčkni [enter] pro zadání příkazu: cas = Cas(17, 40)
(která založí instanci třídy 'c' s danými parametry času)""")
c = Cas(17, 40)

print()
input("""zmáčkni [enter] pro zadání příkazu: d = neskor(c, 2, 55)
(která založí novou instanci třídy dle instance 'c'
v čase posunutou o dané parametry času)""")
d = neskor(c, 2, 55)

print()
input("""zmáčkni [enter] pro zadání příkazu: print(c.str())
(která vypíše čas)""")
print(c.str())

print()
input("""zmáčkni [enter] pro zadání příkazu: print(d.str())
(která vypíše čas)""")
print(d.str())

print()
input("""zmáčkni [enter] pro zavření programu""")
