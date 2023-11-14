##Zadefinuj triedu UcetHeslo, ktorá je odvodená z triedy Ucet
##a má takto zmenené správanie:
##    o __init__(meno, heslo, suma) - k účtu si zapamätá aj heslo
##    o vklad(suma) - si najprv vypýta heslo a až keď je správne,
##    zrealizuje vklad
##    o vyber(suma) - si najprv vypýta heslo a až keď je správne,
##    zrealizuje výber, inak vráti None
##    o pri definovaní týchto metód využite volania ich pôvodných
##    verzií z triedy Ucet
##
##Otestujte napríklad:
##mbank = UcetHeslo('mbank', 'gigi')
##csob = Ucet('csob', 100)
##tatra = UcetHeslo('tatra', 'gogo', 17)
##sporo = Ucet('sporo', 50)
##mbank.vklad(sporo.vyber(30) + tatra.vyber(30))
##csob.vyber(-5)
##spolu = 0
##for ucet in mbank, csob, tatra, sporo:
##    print(ucet)
##    spolu += ucet.stav()
##print('spolu = ', spolu)
##
##Tento program si najprv dvakrát vypýta heslo:
##zadaj heslo uctu tatra: gogo
##zadaj heslo uctu mbank: gigi
##    o a až potom (po správnom zadaní hesiel) vypíše to isté, ako predtým
##    o zisti, čo sa stane s účtami, keď pre 'mbank' určíme chybné heslo


#úvodní a prázdný řádek:                                                  
print('TŘÍDA ÚČET & HESLO - BANKY 02')                              
print('''
Následující program obsahuje 2 třídy:
Základní třídu Ucet obsahující následující metody:

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

A odvozenou třídu UcetHeslo, doplňující základní třídu
o tyto metody:

1) inicializační metoda __init__(jméno, heslo, suma)
    povynný parametr: jméno banky, heslo
    nepovynný parametr: suma (přednastavena na hodnotu 0)
    funkce navíc vytvoří atribut pocet_pokusu pro zaznamenání
    počtu chybných pokusů při zadávání hesla

2) metoda vklad(suma)
    povynný parametr: suma
    pokud je hodnota kladná, připočítá sumu
    zde je tato metoda rozšířena o kontrolu hesla
    maximální počet pokusů - 3x

3) metoda vyber(suma)
    povynný parametr: suma
    pokud je hodnota kladná, odečte sumu
    zde je tato metoda rozšířena o kontrolu hesla
    maximální počet pokusů - 3x
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


class UcetHeslo(Ucet):
    def __init__(self, jmeno, heslo, suma=0):
        Ucet.__init__(self, jmeno, suma)
        self.heslo = heslo
        self.pocet_pokusu = 0

    def vklad(self, suma):
        if self.pocet_pokusu < 3:
            heslo = input(f'>> Zadej heslo pro účet {self.jmeno}: ')
            if heslo == self.heslo:
                print('>> Heslo je správné <<')
                return Ucet.vklad(self, suma)
            else:
                print('>> Heslo není správné <<')
                self.pocet_pokusu += 1
                self.vklad(suma)
        else:
            print('>> 3 x jste zadali nesprávně heslo <<')
            print('>> Transakce nebyla provedena <<')
            self.pocet_pokusu = 0
            
        
    def vyber(self, suma):
        if self.pocet_pokusu < 3:
            heslo = input(f'>> Zadej heslo pro účet {self.jmeno}: ')
            if heslo == self.heslo:
                print('>> Heslo je správné <<')
                return Ucet.vyber(self, suma)
            else:
                print('>> Heslo není správné <<')
                self.pocet_pokusu += 1
                self.vklad(suma)
        else:
            print('>> 3 x jste zadali nesprávně heslo <<')
            print('>> Transakce nebyla provedena <<')
            self.pocet_pokusu = 0
            

print('''
Ukázka funkce třídy Ucet:

1) Vytvoříme 4 instance bank:
    mbank = Ucet('mbank')
    csob = Ucet('csob', 100)
    tatra = Ucet('tatra', 17)
    sporo = Ucet('sporo', 50)
''')
input('zmáčkni [enter] pro provedení příkazů')

mbank = UcetHeslo('mbank', 'gigi')
csob = Ucet('csob', 100)
tatra = UcetHeslo('tatra', 'gogo', 17)
sporo = Ucet('sporo', 50)


print('''
2) Nyní se pokusíme provést 4 transakce:
    a = sporo.vyber(30)
    b = tatra.vyber(30)
    mbank.vklad(a + b)
    csob.vyber(-5)

    (s tím že u účtu tatra a mbank budeme požádáni
    o přístupové heslo:
    tatra - gogo
    mbank - gigi
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



















        
