##Zadefinuj triedu Zoznam,
##pomocou ktorej si budeme vedieť udržiavať zoznam svojich záväzkov (sľubov, povinností, …).
##Tieto budeš uchovávať v atribúte zoznam typu list.
##Trieda obsahuje tieto metódy:
##metóda pridaj(prvok), ak sa tam takýto záväzok ešte nenachádza, pridá ho na koniec
##metóda vyhod(prvok), ak sa tam takýto záväzok nachádzal, vyhodí ho
##metóda je_v_zozname(prvok) vráti True alebo False podľa toho, či sa tam tento záväzok nachádza
##metóda vypis() vypíše všetky záväzky v tvare zoznam: záväzok, záväzok, záväzok
##Napríklad:
##moj = Zoznam()
##moj.pridaj('upratat')
##moj.pridaj('behat')
##moj.pridaj('ucit sa')
##if moj.je_v_zozname('behat'):
##    print('musis behat')
##else:
##    print('nebehaj')
##moj.pridaj('upratat')
##moj.vyhod('spievat')
##moj.vypis()
##vypíše:
##musis behat
##zoznam: upratat, behat, ucit sa


#úvodní a prázdný řádek:                                                  
print('TŘÍDA - SEZNAM NA HOBBY')                              
print('''
Třída Zoznam obsahuje následující funkce:

1) inicializační funkce, která vytvoří prázdný seznam

2) metoda pridaj(prvok), která přidá do seznamu prvek (obsahující text s hobby)

3) metoda vyhod(prvok), která odebere ze seznamu prvek (obsahující text s hobby)

4) metoda je_v_zozname(prvok), která zjistí, zda se prvek již v seznamu nachází

5) metoda vypis(), která vypíše položky seznamu''')


class Zoznam:
    def __init__(self):
        self.zoznam = []
        print('>> seznam pro hobby vytvořen')

    def pridaj(self, prvok):
        if not self.je_v_zozname(prvok):
            self.zoznam.append(prvok)
            print('>> do seznamu bylo přidané hobby:', prvok)

    def vyhod(self, prvok):
        if self.je_v_zozname(prvok):
            self.zoznam.pop(self.zoznam.index(prvok))
            print('>> ze seznamu bylo odebráno hobby:', prvok)
        else:
            print('>> seznam hobby:', prvok, 'neobsahuje')

    def je_v_zozname(self, prvok):
        for i in self.zoznam:
            if i == prvok:
                return True

    def vypis(self):
        print('>> zoznam: ', end='')
        for i in self.zoznam:
            if i == self.zoznam[-1]:
                print(i)
            else:
                print(i, end=', ')

print()
input("""zmáčkni [enter] pro zadání příkazu: moj = Zoznam()
(která vytvoří nový prázdný seznam)""")
moj = Zoznam()

print()
input("""zmáčkni [enter] pro zadání příkazu: moj.pridaj('upratat')
(pro přidání prvního záznamu)""")
moj.pridaj('upratat')

print()
input("""zmáčkni [enter] pro zadání příkazu: moj.pridaj('behat')
(pro přidání druhého záznamu)""")
moj.pridaj('behat')

print()
input("""zmáčkni [enter] pro zadání příkazu: moj.pridaj('ucit sa')
(pro přidání třetího záznamu)""")
moj.pridaj('ucit sa')

print()
input("""zmáčkni [enter] pro zadání příkazu:

if moj.je_v_zozname('behat'):
    print('musis behat')
else:
    print('nebehaj')
    """)
if moj.je_v_zozname('behat'):
    print('>> musis behat')
else:
    print('>> nebehaj')

print()
input("""zmáčkni [enter] pro zadání příkazu: moj.pridaj('upratat')
(pro přidání čtvrtého záznamu)""")
moj.pridaj('upratat')

print()
input("""zmáčkni [enter] pro zadání příkazu: moj.vyhod('spievat')
(pro odebrání záznamu, který seznam neobsahuje)""")
moj.vyhod('spievat')

print()
input("""zmáčkni [enter] pro zadání příkazu: tz.vypis()
(pro výpis telefonního seznamu)""")
moj.vypis()

print()
input("""zmáčkni [enter] pro zavření programu""")




