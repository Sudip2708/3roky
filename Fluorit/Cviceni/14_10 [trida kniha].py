##Zadefinuj triedu Kniha, ktorá bude udržiavať informácie o jednej knihe.
##Trieda bude mať tieto metódy:
##inicializácia __init__(autor, titul)
##metóda nastav_vydavatela(vydavatel) pridá informáciu o vydavateľovi
##metóda nnastav_rok(rok) pridá informáciu o roku vydania
##metóda vypis() vypíše informácie o knihe
##Napríklad:
##k1 = Kniha('Dobsinsky', 'Rozpravky')
##k1.nastav_vydavatela('Mlade Leta')
##k2 = Kniha('Lasica', 'Bodka')
##k2.nastav_rok(2007)
##k1.vypis()
##k2.vypis()
##vypíše:
##Kniha: Dobsinsky: Rozpravky,  Mlade Leta
##Kniha: Lasica: Bodka, 2007


#úvodní a prázdný řádek:                                                  
print('TŘÍDA - KNIHA')                              
print('''
Třída Kniha obsahuje následující funkce:

1) inicializační funkce, která založí atributy pro autora, název knihy, vydavatele
a roku vydání. Poviné atributy jsou autor a název knihy.

2) metoda nastav_vydavatela(vydavatel), která přepíše hodnotu vydavatele

3) nastav_rok(rok), která přepíše hodnotu roku vydání

4) metoda vypis(), která vypíše atributy knihy''')


class Kniha:
    def __init__(self, autor, titul):
        self.autor = autor
        self.titul = titul
        self.vydavatel = ''
        self.rok = ''
        print(f'>> Byla vytvořen záznam o knihze: {self.autor}: {self.titul}, {self.rok} {self.vydavatel}')

    def nastav_vydavatela(self, vydavatel):
        self.vydavatel = vydavatel
        print(f'>> U knihy {self.autor}: {self.titul}, byl přidán vydavatel: {self.vydavatel}')

    def nastav_rok(self, rok):
        self.rok = rok
        print(f'>> U knihy {self.autor}: {self.titul}, byl přidán rok vydání: {self.rok}')

    def vypis(self):
        print(f'>> Kniha: {self.autor}: {self.titul}, {self.rok} {self.vydavatel}')


print()
input("""zmáčkni [enter] pro zadání příkazu: k1 = Kniha('Dobsinsky', 'Rozpravky')
(která vytvoří novou instanci třídy Kniha - nový záznam o knize (k1))""")
k1 = Kniha('Dobsinsky', 'Rozpravky')

print()
input("""zmáčkni [enter] pro zadání příkazu: k1.nastav_vydavatela('Mlade Leta')
(která přidá ke knize k1 vydavatele)""")
k1.nastav_vydavatela('Mlade Leta')

print()
input("""zmáčkni [enter] pro zadání příkazu: k2 = Kniha('Lasica', 'Bodka')
(která vytvoří novou instanci třídy Kniha - nový záznam o knize (k2))""")
k2 = Kniha('Lasica', 'Bodka')

print()
input("""zmáčkni [enter] pro zadání příkazu: k2.nastav_rok(2007)
(která přidá ke knize k2 rok)""")
k2.nastav_rok(2007)

print()
input("""zmáčkni [enter] pro zadání příkazu: k1.vypis()
(která vypíše atributy knihy k1)""")
k1.vypis()

print()
input("""zmáčkni [enter] pro zadání příkazu: k1.vypis()
(která vypíše atributy knihy k2)""")
k2.vypis()

print()
input("""zmáčkni [enter] pro zavření programu""")

