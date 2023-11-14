##Do triedy Cas z úlohy (1) pridaj metódu str(),
##ktorá nič nevypisuje,
##ale namiesto toho vráti (return) znakový reťazec
##s hodinami a minútami v tvare '9:17'.
##Napríklad:
##>>> c = Cas(9, 1)
##>>> print('teraz je', c.str())
##    teraz je 9:01


#úvodní a prázdný řádek:                                                  
print('TŘÍDA - ČAS - 02')                              
print('''
Třída Cas obsahuje následující funkce:

1) inicializační funkce, která očekává hodnotu pro hodiny a minuty
a založení objektu instance třídy

2) metoda vypis(), která vypíše text s časem

3) metoda str(), která vrátí hodnotu času jako textový soubor''')




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
    
print()
input("""zmáčkni [enter] pro zadání příkazu: c = Cas(9, 1)
(která založí instanci třídy 'c' s danými parametry času)""")
c = Cas(9, 1)

print()
input("""zmáčkni [enter] pro zadání příkazu: print('teraz je', c.str())
(která vypíše text s časem, nyní je však čas jen hodnotou
ve funkci print())""")
print('teraz je', c.str())

print()
input("""zmáčkni [enter] pro zavření programu""")
