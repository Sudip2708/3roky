##Zadefinuj triedu Ucet s týmito metódami:
##    o __init__(meno, suma) - meno účtu a počiatočná suma,
##    napríklad Ucet('mbank', 100) alebo Ucet('jbanka')
##    o __str__() - reťazec v tvare 'ucet mbank -> 100 euro'
##    alebo ucet jbanka -> 0 euro
##    o stav() - vráti momentálny stav účtu (vráti sumu na účte)
##    o vklad(suma) - danú sumu pripočíta k účtu
##    o vyber(suma) - vyberie sumu z účtu (len ak je to kladné číslo),
##    ak je na účte menej ako požadovaná suma,
##    vyberie len toľko koľko sa dá, metóda vráti (return) vybranú sumu
##
##Otestuj, napríklad takto:
##mbank = Ucet('mbank')
##csob = Ucet('csob', 100)
##tatra = Ucet('tatra', 17)
##sporo = Ucet('sporo', 50)
##mbank.vklad(sporo.vyber(30) + tatra.vyber(30))
##csob.vyber(-5)
##spolu = 0
##for ucet in mbank, csob, tatra, sporo:
##    print(ucet)
##    spolu += ucet.stav()
##print('spolu = ', spolu)
##
##vypíše:
##ucet mbank -> 47 euro
##ucet csob -> 100 euro
##ucet tatra -> 0 euro
##ucet sporo -> 20 euro
##spolu =  167


#úvodní a prázdný řádek:                                                  
print('TŘÍDA ÚČET - BANKY 01')                              
print('''
Třída Ucet obsahuje následující metody:

1) inicializační metoda __init__(jméno, suma)
    povynný parametr: jméno banky
    nepovynný parametr: suma (přednastavena na hodnotu 0)

2) metoda __str__()
    vrací řetězec s názvem banky a sumou

3) metoda stav()
    vrací hodnotu sumy

4) metoda vklad(suma)
    povynný parametr: suma
    pokud je hodnota kladná, připočítá sumu

5) metoda vyber(suma)
    povynný parametr: suma
    pokud je hodnota kladná, odečte sumu
''')


#definice třídy:
class Ucet:
    def __init__(self, jmeno, suma=0):
        self.jmeno = jmeno
        self.suma = suma
        print(f'>> Byl založen účet {self.jmeno} s počáteční sumou {self.suma} euro <<')

    def __str__(self):
        return f'Účet {self.jmeno} -> {self.suma} euro'

    def stav(self):
        return self.suma

    def vklad(self, suma):
        if suma > 0:
            self.suma += suma
            print(f'>> Na účet {self.jmeno} byla vložena částka {suma} euro <<')
            print(f'>> Momentální zůstatek je {self.suma} euro <<')
        else:
            print(f'>> Na účet {self.jmeno} nebyla vložena částka {suma} euro <<')
            print('>> Suma nemá kladnou hodnbotu <<')
            print('>> Trancakce neprovedena <<')
        
    def vyber(self, suma):
        if suma > 0:
            if self.suma > suma:
                self.suma -= suma
                print(f'>> Z účtu {self.jmeno} byla vybrána částka {suma} euro <<')
                print(f'>> Momentální zůstatek je {self.suma} euro <<')
                return suma
            else:
                zaplaceno = self.suma
                nezaplaceno = suma - self.suma
                self.suma = 0
                print(f'>> Z účtu {self.jmeno} byla vybrána částka {zaplaceno} euro <<')
                print(f'>> Momentální zůstatek je 0 euro <<')
                print(f'>> Cybí doplatit {nezaplaceno} euro <<')
                return zaplaceno
        else:
            print(f'>> Z úču {self.jmeno} nebyla vybrána částka {suma} euro <<')
            print('>> Suma nemá kladnou hodnbotu <<')
            print('>> Trancakce neprovedena <<')
            

print('''
Ukázka funkce třídy Ucet:

1) Vytvoříme 4 instance bank:
    mbank = Ucet('mbank')
    csob = Ucet('csob', 100)
    tatra = Ucet('tatra', 17)
    sporo = Ucet('sporo', 50)
''')
input('zmáčkni [enter] pro provedení příkazů')

mbank = Ucet('mbank')
csob = Ucet('csob', 100)
tatra = Ucet('tatra', 17)
sporo = Ucet('sporo', 50)


print('''
2) Nyní se pokusíme provést 4 transakce:
    a = sporo.vyber(30)
    b = tatra.vyber(30)
    mbank.vklad(a + b)
    csob.vyber(-5)
''')
input('zmáčkni [enter] pro provedení příkazů')

mbank.vklad(sporo.vyber(30) + tatra.vyber(30))
csob.vyber(-5)


print('''
Jak vydno, první výběr prošel, druhý nepročel celý,
protože na účtu nebylo dostatek peněz, vklad vyšel
a tření výběr nevyšel z důvody záporné částky.

3) Nyní vytvoříme dočasnou proměnou spolu
a for cyklem svypíšeme účet a zůstatek každé banky,
a do proměnné spolu zapíšeme celkovou sumu
a také ji vytisknem:

spolu = 0
for ucet in mbank, csob, tatra, sporo:
    print(ucet)
    spolu += ucet.stav()
print('spolu = ', spolu)
''')
input('zmáčkni [enter] pro provedení příkazů')

spolu = 0
for ucet in mbank, csob, tatra, sporo:
    print(ucet)
    spolu += ucet.stav()
print('spolu = ', spolu)
        

print('''
A to je vše :-)
''')
input('zmáčkni [enter] pro ukončení programu')
