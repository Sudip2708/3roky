##Zadefinuj triedu, pomocou ktorej budeš vedieť reprezentovať obdĺžniky.
##Pri obdĺžnikoch nás budú zaujímať len veľkosti strán
##a na základe toho sa bude dať vypočítať ich obsah aj obvod.
##Dopíš všetky metódy:
##class Obdlznik:
##    
##        def __init__(self, a, b):
##            # inicializuje
##            ...
##    
##        def __str__(self):
##            # vráti reťazec v tvare 'Obdlznik(100, 70)'
##            ...
##    
##        def obsah(self):
##            # vráti obsah
##            ...
##    
##        def obvod(self):
##            # vráti obvod
##            ...
##    
##        def zmen_velkost(self, pomer):
##            # vynásobí obe veľkosti strán zadaným pomerom
##            ...
##    
##        def kopia(self):
##            # vyrobí kópiu samého seba
##            ...
##Otestuj, napríklad:
##    >>> obd1 = Obdlznik(20, 7)
##    >>> print('obvod =', obd1.obvod())
##        obvod = 54
##    >>> print(obd1)
##        Obdlznik(20, 7)
##    >>> obd2 = obd1.kopia()
##    >>> obd2.zmen_velkost(2)
##    >>> print(obd2)
##        Obdlznik(40, 14)


#úvodní a prázdný řádek:                                                  
print('TŘÍDA OBDELNÍK')                              
print('''
Třída Obdelnik obsahuje následující funkce:

1) inicializační funkce __init__()očekávající 2 parametry:
    a = strana A obdelníku 
    b = strana B obdelníku

2) metoda __str__(), vrací řetězec s názvem třídy a vstupními parametry

3) metoda obsah(), vrací hodnotu obsahu

4) metoda obvod(), vrací hodnotu obvodu

5) metoda kopia(), vytvoří z hodnot instance novou instanci

6) metoda zmen_velikost(poměr), změní atributy 'a' a 'b' ''')


#definice třídy:
class Obdelnik:

    def __init__(self, a, b):
        '''inicializační metoda očekávající 2 parametry: strana A a B'''
        self.a = a
        self.b = b

    def __str__(self):
        '''metoda __str__ vrací řetězec s názvem třídy a vstupními parametry'''
        return f'Obdelnik({self.a}, {self.b})'

    def obsah(self):
        '''metoda obsah() vrací hodnotu obsahu'''
        return self.a * self.b

    def obvod(self):
        '''metoda obvod() vrací hodnotu obvodu'''
        return (self.a + self.b) * 2

    def zmen_velkost(self, pomer):
        '''metoda zmen_velkost(pomer) změní atributy délky stran A a B dle zadaného poměru'''
        self.a = self.a * pomer
        self.b = self.b * pomer
        print('>Byla změněna velikost<')

    def kopia(self):
        '''metoda kopia(), vytvoří z hodnot instance novou instanci'''
        novy = Obdelnik(self.a, self.b)
        print ('>Byla vytvořena kopie<')
        return novy


print()
print('Zadání vstupních údajů:')
a = float(input("Zadej délku strany 'a': "))
b = float(input("Zadej délku strany 'b': "))
obd_1 = Obdelnik(a, b)
print('--------------------')
print('Zadal jsi: ', obd_1)
print('--------------------')
print('obvod obdelníku je ', obd_1.obvod())
print('obsah obdelníku je ', obd_1.obsah())
print('--------------------')
print()
print('Vytvoření dalšího obdelníku dle poměru:')
pomer = float(input('Zadej hodnotu zvětšená (>1) nebo zmenšení (<1 a >0): '))
print('--------------------')
obd_2 = obd_1.kopia()
obd_2.zmen_velkost(pomer)
print('--------------------')
print('Nové zadání: ', obd_2)
print('--------------------')
print('obvod obdelníku je ', obd_2.obvod())
print('obsah obdelníku je ', obd_2.obsah())
print('--------------------')
print()
input('>> Zmáčkní [enter] pro ukončení programu <<')


