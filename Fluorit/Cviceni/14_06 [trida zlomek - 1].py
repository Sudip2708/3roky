##Zapíš definíciu triedy Zlomok,
##ktorá v inicializácii vytvorí dva atribúty citatel a menovatel.
##Metóda vypis() vypíše pomocou print() tento zlomok v tvare zlomok je 3/8.
##Napríklad:
##>>> z1 = Zlomok(3, 8)
##>>> z2 = Zlomok(2, 4)
##>>> z1.vypis()
##    zlomok je 3/8
##>>> z2.vypis()
##    zlomok je 2/4


#úvodní a prázdný řádek:                                                  
print('TŘÍDA - ZLOMEK - 01')                              
print('''
Třída Zlomek obsahuje následující funkce:

1) inicializační funkce, očekávající hodnotu citatele a jmenovatele

2) metoda vypis(), která vypíše text s zlomkem''')


class Zlomok:
    def __init__(self, citatel, jmenovatel):
        self.citatel = citatel
        self.jmenovatel = jmenovatel
        print(f'''>> Vytvořena instance třídy Zlomek s hodnotami:
              citatel - {self.citatel}
              jmenovatel - {self. jmenovatel}''')

    def vypis(self):
        print(f'>> zlomek je {self.citatel }/{self.jmenovatel}')

print()
input("""zmáčkni [enter] pro zadání příkazu: z1 = Zlomok(3, 8)
(která založí instanci třídy 'z1' s danými hodnotami zlomku)""")
z1 = Zlomok(3, 8)

print()
input("""zmáčkni [enter] pro zadání příkazu: z2 = Zlomok(2, 4)
(která založí instanci třídy 'z2' s danými hodnotami zlomku)""")
z2 = Zlomok(2, 4)

print()
input("""zmáčkni [enter] pro zadání příkazu: z1.vypis()
(která vypíše text se zlomkem z instance 'z1')""")
z1.vypis()

print()
input("""zmáčkni [enter] pro zadání příkazu: c.vypis()
(která vypíše text se zlomkem z instance 'z2')""")
z2.vypis()

print()
input("""zmáčkni [enter] pro zavření programu""")

