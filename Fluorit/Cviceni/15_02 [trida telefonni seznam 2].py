##Zober riešenie (11) úlohy z predchádzajúceho cvičenia:
##triedu TelefonnyZoznam, ktorá udržiava informácie o telefónnych číslach
##(ako zoznam list dvojíc tuple).
##Trieda mala tieto metódy:
##o	metóda pridaj(meno, telefon) pridá do zoznamu dvojicu (meno, telefon)
##ak takéto meno v zozname už existovalo, nepridáva novú dvojicu, ale nahradí len telefónne číslo
##o	metóda vypis() vypíše celý telefónny zoznam.
##o	malo by fungovať:
##    tz = TelefonnyZoznam()
##    tz.pridaj('Jana', '0901020304')
##    tz.pridaj('Juro', '0911111111')
##    tz.pridaj('Jozo', '0212345678')
##    tz.pridaj('Jana', '0999020304')
##    tz.vypis()
##Doplň do tejto triedy nové metódy tak, aby fungovalo aj zapisovanie aj čítanie s textovým súborom:
##o	metóda __init__(meno_suboru) si zapamätá meno súboru (nič ešte nezapisuje ani nečíta)
##o	metóda zapis() momentálny obsah telefónneho zoznamu zapíše do súboru:
##        v každom riadku bude jedna dvojica hodnôt meno a číslo,
##        pričom budú navzájom oddelené znakom ';'
##        (v jednom riadku súboru môže byť, napríklad Jana;0999020304)
##o	metóda citaj() prečíta zadaný súbor a vyrobí z neho zoznam dvojíc
##        (list s prvkami tuple) - starý obsah zoznamu v pamäti sa zruší a nahradí novým
##o	malo by fungovať napríklad:
##    tz = TelefonnyZoznam('tel.txt')
##    tz.pridaj('Jana', '0901020304')
##    tz.pridaj(...
##    ...
##    tz.zapis()     # zapísal do súboru
##    t2 = TelefonnyZoznam('tel.txt')
##    t2.citaj()
##    t2.vypis()     # pôvodny obsah


#úvodní a prázdný řádek:                                                  
print('TŘÍDA - TELEFONÍ SEZNAM 2')                              
print('''
Třída TelefonnyZoznam obsahuje následující funkce:

1) inicializační funkce __init__()očekávající 1 parametr: "jmeno_souboru"
Vytvoří atribut "self.jmeno_souboru" a prázdný seznam "self.zoznam"

2) metoda pridaj(meno, telefon), pro přidání jména a telefonu
metoda je provázaná s metodou zkontroluj(meno)
pokud zjistí, že jméno v seznamu již existuje, přepíše jen telefon

3) metoda zkontroluj(meno), pro kontrolu,
zda náš seznam "self.zoznam" již obsahuje přidávané jméno

4) metoda zapis(), která vytvoří textový soubor,
který pojmenuje dle atributu "self.jmeno_souboru"
a zapíše do něj obsah seznamu "self.zoznam"

5) metoda citaj(), která vymaže obsah seznamu "self.zoznam"
a po té otevře textový soubor a do seznamu přepíše jeho obsah.

6) metoda vypis(), která vypíše obsah seznamu "self.zoznam"''')


class TelefonnyZoznam:
    def __init__(self, jmeno_souboru):
        self.jmeno_souboru = jmeno_souboru
        self.zoznam = []
        print(f'>> byl vytvořen atribut: jmeno_souboru = {jmeno_souboru}')
        print('>> byl vytvořen seznam')


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


    def zapis(self):
        subor = open(self.jmeno_souboru, 'w')
        for jmeno, telefon in self.zoznam:
            print(f'{jmeno}; {telefon}', file=subor)
        subor.close()
        print(f'>> obsah seznamu zapsán do souboru {self.jmeno_souboru}')

        
    def citaj(self):
        self.zoznam = []
        subor = open(self.jmeno_souboru, 'r')
        radek = subor.readline().strip()
        while radek:
            self.zoznam.append(tuple(radek.split("; ")))
            radek = subor.readline().strip()
        print(f'>> obsah soubro {self.jmeno_souboru} zapsán do seznamu')

        
    def vypis(self):
        if len(self.zoznam) > 0:
            for i in self.zoznam:
                meno = i[0]
                telefon = i[1]
                print('>>', meno, telefon)
        else:
            print('>> seznam je prázdný')

            
print()
input('''Zmáčkni [enter] pro vytvoření instance "t1" třídy "TelefonnyZoznam"
"t1 = TelefonnyZoznam("15_02_tel.txt")"''')
t1 = TelefonnyZoznam('15_02_tel.txt')

print()
input('''Zmáčkni [enter] pro zadání následujících tří položek seznamu:
"t1.pridaj("Jana", "0901020304")"
"t1.pridaj("Juro", "0911111111")"
"t1.pridaj("Jozo", "0212345678")"''')
t1.pridaj('Jana', '0901020304')
t1.pridaj('Juro', '0911111111')
t1.pridaj('Jozo', '0212345678')

print()
input('''Zmáčkni [enter] pro změnu telefonu u Jany:
"t1.pridaj("Jana", "0999020304")"''')
t1.pridaj('Jana', '0999020304')

print()
input('''Zmáčkni [enter] pro zápis seznamu do souboru:
"t1.zapis()"''')
t1.zapis()
      
print()
input('''Zmáčkni [enter] pro vytvoření instance "t2" třídy "TelefonnyZoznam"
"t2 = TelefonnyZoznam("15_02_tel.txt")"''')
t2 = TelefonnyZoznam('15_02_tel.txt')

print()
input('''Zmáčkni [enter] pro přepsání obsahu souboru "15_02_tel.txt" do seznamu:
"t2.citaj()"''')
t2.citaj()

print()
input('''Zmáčkni [enter] pro výpis instane "t2":
"t2.vypis()"''')
t2.vypis()

print()
input('Zmáčkní [enter] pro ukončení programu')
   
