##Zadefinuj triedu TelefonnyZoznam,
##ktorá bude udržiavať informácie o telefónnych číslach (ako zoznam list dvojíc tuple).
##Trieda bude mať tieto metódy:
##metóda pridaj(meno, telefon) pridá do zoznamu dvojicu (meno, telefon)
##ak takéto meno v zozname už existovalo, nepridáva novú dvojicu, ale nahradí len telefónne číslo
##metóda vypis() vypíše celý telefónny zoznam.
##Napríklad:
##tz = TelefonnyZoznam()
##tz.pridaj('Jana', '0901020304')
##tz.pridaj('Juro', '0911111111')
##tz.pridaj('Jozo', '0212345678')
##tz.pridaj('Jana', '0999020304')
##tz.vypis()
##vypíše:
##Jana 0999020304
##Juro 0911111111
##Jozo 0212345678


#úvodní a prázdný řádek:                                                  
print('TŘÍDA - TELEFONÍ SEZNAM')                              
print('''
Třída TelefonnyZoznam obsahuje následující funkce:

1) inicializační funkce, která vytvoří prázdný seznam

2) metoda pridaj(meno, telefon), pro přidání jména a telefonu
metoda je provázaná s metodou zkontroluj(meno)
pokud zjistí, že jméno v seznamu již existuje, přepíše jen telefon

3) metoda zkontroluj(meno), pro kontrolu,
zda náš seznam již obsahuje přidávané jméno

4) metoda vypis(), která vypíše položky seznamu''')


class TelefonnyZoznam:
    def __init__(self):
        self.zoznam = []
        print('>> telefonní seznam vytvořen')

    def pridaj(self, meno, telefon):
        idx = self.zkontroluj(meno)
        if idx != None:
            self.zoznam[idx][1] = telefon
            print('>> u jména ', meno, 'bylo aktualizované číslo: ', telefon)
        else:
            self.zoznam.append([meno, telefon])
            print('>> do seznamu bylo přidané jméno:', meno, 'a telefon: ', telefon)

    def zkontroluj(self, meno):
        if len(self.zoznam) > 0:
            for idx, dvojice in enumerate(self.zoznam):
                if dvojice[0] == meno:
                    return idx
                return None

    def vypis(self):
        if len(self.zoznam) > 0:
            for i in self.zoznam:
                meno = i[0]
                telefon = i[1]
                print('>>', meno, telefon)
        else:
            print('>> seznam je prázdný')
        
print()
input("""zmáčkni [enter] pro zadání příkazu:
tz = TelefonnyZoznam()
(které vytvoří nový telefonní seznam)""")
tz = TelefonnyZoznam()

print()
input("""zmáčkni [enter] pro zadání příkazu:
tz.pridaj('Jana', '0901020304')
(pro přidání prvního záznamu)""")
tz.pridaj('Jana', '0901020304')

print()
input("""zmáčkni [enter] pro zadání příkazu:
tz.pridaj('Juro', '0911111111')
(pro přidání druhého záznamu)""")
tz.pridaj('Juro', '0911111111')

print()
input("""zmáčkni [enter] pro zadání příkazu:
tz.pridaj('Jozo', '0212345678')
(pro přidání třetího záznamu)""")
tz.pridaj('Jozo', '0212345678')

print()
input("""zmáčkni [enter] pro zadání příkazu:
tz.pridaj('Jana', '0999020304')
(pro změnu telefonu u jany)""")
tz.pridaj('Jana', '0999020304')

print()
input("""zmáčkni [enter] pro zadání příkazu:
tz.vypis()
(pro výpis telefonního seznamu)""")
tz.vypis()

print()
input("""zmáčkni [enter] pro zavření programu""")
