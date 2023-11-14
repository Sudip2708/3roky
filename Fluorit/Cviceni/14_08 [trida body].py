##Zadefinuj triedu Body, ktorá si bude uchovávať momentálny stav bodov
##(napríklad získané body v nejakej hre).
##Trieda bude mať tieto metódy:
##metóda pridaj() k momentálnemu stavu pridá 1 bod
##metóda uber() od momentálneho stavu odoberie 1 bod;
##metóda kolko() vráti celé číslo - momentálny bodový stav
##Napríklad:
##>>> b = Body()
##>>> for i in range(10):
##        b.pridaj()
##>>> b.uber()
##>>> b.uber()
##>>> print('body =', b.kolko())
##    body = 8


#úvodní a prázdný řádek:                                                  
print('TŘÍDA - BODY')                              
print('''
Třída Body obsahuje následující funkce:

1) inicializační funkce, která neočekává žádnou hodnotu,
a založí atribut 'body', s hodnotou 0

2) metoda pridaj(), která přidá 1 bod

3) metoda uber(), která ubere 1 bod

4) metoda kolko(), která vrátí aktuální hodnotu bodů''')

class Body:
    def __init__(self, body=0):
        self.body = 0
        print(f'>> bylo založeno počítadlo bodů s hodnotou 0')

    def pridaj(self):
        self.body += 1
        print(f'>> byl přidán 1 bod')
        
    def uber(self):
        self.body -= 1
        print(f'>> byl ubrán 1 bod')

    def kolko(self):
        return self.body

print()
input("""zmáčkni [enter] pro zadání příkazu: b = Body()
(která založí instanci třídy 'b' s atributem 0 bodů)""")
b = Body()

print()
input("""zmáčkni [enter] pro přidání 10 bodů: 10x b.pridaj() """)
for i in range(10):
    b.pridaj()

print()
input("""zmáčkni [enter] pro ubrání 2 bodů: 2x b.uber()""")
b.uber()
b.uber()

print()
input("""zmáčkni [enter] pro zadání příkazu: print('body =', b.kolko())
(která vypíše aktuální počet bodů)""")
print('>> body =', b.kolko())

print()
input("""zmáčkni [enter] pro zavření programu""")

