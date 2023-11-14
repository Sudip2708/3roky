##Zadefinuj metódy triedy TelefonnyZoznam podobnej z 15. cvičenia:
##class TelefonnyZoznam:
##    def __init__(self, meno_suboru=None):
##        ...
##
##    def pridaj(self, meno, telefon):
##        ...
##
##    def zisti(self, meno):
##        ...
##
##    def citaj(self, meno_suboru):
##        ...
##
##    def zapis(self, meno_suboru):
##        ...
##
##    def vypis(self):
##        ...
##Metódy:
##• __init__(meno_suboru=None)
##    inicializuje self.zoznam a zavolá self.citaj(meno_suboru),
##    prípadnú výnimku bude teraz ignorovať
##• pridaj(meno, telefon)
##    pridá dvojicu (tuple) do zoznamu alebo nahradí,
##    ak už také meno bolo v zozname
##    ak meno alebo telefon nie je reťazec, vyvolá výnimku TypeError
##• zisti(meno)
##    vráti príslušné telefónne číslo alebo vyvolá výnimku KeyError
##• citaj(meno_suboru)
##    prečíta obsah súboru (v každom riadku dva reťazce oddelené medzerou),
##    pri chybe vyvolá ValueError
##• zapis(meno_suboru)
##    do každého riadka zapíše meno a telefón, oddelí medzerou
##• vypis() vypíše do textovej plochy



class TelefonnyZoznam:
    def __init__(self, jmeno_souboru=None):
        self.seznam = []
        self.cti(jmeno_souboru)

    def cti(self, jmeno_souboru):
        cislo_radku = 0
        try:
            soubor = open(jmeno_souboru, 'r')
            radek = soubor.readline().strip()
            cislo_radku += 1
            while radek:
                radek = radek.split(' ')
                if len(radek) != 2:
                    raise ValueError
                self.seznam.append(tuple(radek))
                radek = soubor.readline().strip()
                cislo_radku += 1
            soubor.close()
            print(f'>> textový soubor {jmeno_souboru} byly načten <<')
        except FileNotFoundError:
            print('>> chyba: vámi uvedený soubor nebyl nalezen <<')
        except ValueError:
            print('>> chyba: soubor neobsahuje očekávané údaje:')
            print('    (očekávané údaje: jméno a telefon)')
            print(f'    {cislo_radku}. radek obsahuje: {radek} <<')
            

    def pridej(self, jmeno, telefon):
        nalezeno = False
        try:
            chyba1, chyba2 = None, None
            if not isinstance(jmeno, str):
                chyba1, chyba2 = 'jmeno', jmeno
                raise TypeError
            if not isinstance(telefon, str):
                chyba1, chyba2  = 'telefon', telefon
                raise TypeError
        except TypeError:
            print('>> chyba: metoda pridej očekává dvě hodnoty ve formě textového řetězce:')
            print(f'    {chyba1} není zadán jako řetězec: {chyba2} <<')
            
        if chyba1 == None and chyba2 == None:        
            for radek in self.seznam:
                if radek[0] == jmeno:
                    stare_cislo = radek[1]
                    radek[1] = telefon
                    nalezeno = True
                    print(f'>> u jména {jmeno}, byl změněn telefon:')
                    print(f'    původní číslo: {stare_cislo}, nové číslo: {telefon} <<')
            if nalezeno == False:
                self.seznam.append((jmeno, telefon))
                print('>> byl přidán nová záznam:')
                print(f'    jmeno: {jmeno}')
                print(f'    telefon: {telefon} <<')

    def zjisti(self, jmeno):
        nalezeno = False
        for radek in self.seznam:
            if radek[0] == jmeno:
                nalezeno = True
                print(f'>> {jmeno} má telefon: {radek[1]} <<')
        try:
            if nalezeno == False:
                raise KeyError
        except KeyError:
            print(f'>> chyba: jméno {jmeno} nebylo nalezeno <<')

    def zapis(self, jmeno_souboru):
        soubor = open(jmeno_souboru, 'w')
        for radek in self.seznam:
            print(f'{radek[0]} {radek[1]}', file=soubor)
        soubor.close()
        print(f'>> byl vytvořen textový soubor {jmeno_souboru}')
        print('    obsahující seznam všech jmen a telefonních čísel <<')
        
    def vypis(self):
        print('>> výpis telefonního seznamu:')
        for radek in self.seznam:
            print(f'{radek[0]} {radek[1]}')
        print('konec výpisu <<')

        
t1 = TelefonnyZoznam('17_10_tel.txt')
t1.pridej('kamil', '603563365')
t1.zjisti('kamil')
t1.zapis('17_11_tel.txt')
t1.vypis()
