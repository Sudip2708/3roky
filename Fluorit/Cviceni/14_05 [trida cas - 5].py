##Vytvor pätnásť-prvkový zoznam inštancií triedy Cas,
##v ktorom prvý prvok reprezentuje 8:10 a každý ďalší je posunutý o 50 minút.
##Ďalšie časy v zozname vytváraj v cykle, využi funkciu neskor().
##Napríklad:
##zoznam = [Cas(8, 10)]
##for i in range(14):       # vyrobí 15-prvkový zoznam časov
##    zoznam ...
##for c in zoznam:
##    print(c.str(), end=' ')
##vypíše:
##8:10 9:00 9:50 ... 19:50


#úvodní a prázdný řádek:                                                  
print('TŘÍDA - ČAS - 05')                              
print('''
Třída Cas obsahuje následující funkce:

1) inicializační funkce, která očekává hodnotu pro hodiny a minuty
a založení objektu instance třídy

2) metoda vypis(), která vypíše text s časem

3) metoda str(), která vrátí hodnotu času jako textový soubor

4) metoda pridaj(hodiny, minuty), která změní původní hodnotu času,
přičtením hodnot hodin a minut

Dále program obsahuje:

1) jednu vnbější funkci: neskor(cas, hodiny, minuty),
která vytvoří novou instanci třídy Čas,
kde čas posune o zadaný počet hodin a minut.

2) seznam na vytvořené instance

3) cyklus na vytvoření 14-ti instancí

4) cyklus na vypsání hodnot času všech vytvořených
nstancí zapsaný v jednom řádku''')




class Cas:
    def __init__(self, hodiny, minuty):
        self.hodiny = hodiny
        self.minuty = minuty

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

def neskor(cas, hodiny, minuty):
    novy = Cas(cas.hodiny, cas.minuty)
    novy.pridaj(hodiny, minuty)
    return novy

zoznam = [Cas(8, 10)]
for i in range(14):
    posun = (i+1) * 50
    posun_h = posun//60
    posun_m = posun%60
    cas = zoznam[0]
    zoznam.append(neskor(cas, posun_h, posun_m))

print()
input("""zmáčkni [enter] pro vypsání 14-ti časů
s počátečním časem 8:10
a postupným přírůstkem vždy o 50 minut""")
print()

for c in zoznam:
    print(c.str(), end=' ')

print()
print()
input("""zmáčkni [enter] pro zavření programu""")

