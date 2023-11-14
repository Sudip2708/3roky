##9. Týždenný projekt
##L.I.S.T.
##• riešenie odovzdaj na úlohový server https://list.fmph.uniba.sk/
##• príklad zo skúšky z roku 2018/2019
##
##Robot Karel
##
##Robot Karel sa pohybuje po štvorcovej sieti,
##v ktorej sa na niektorých políčkach nachádzajú kartičky s nejakými symbolmi.
##Robot prechádza ponad tieto políčka,
##pričom na niektorých môže kartičku pod sebou zdvihnúť
##(vloží si ju do svojho batoha), resp. karičku z batoha vybrať
##a položiť na políčko pod seba.
##
##Robot reaguje na povely 'vlavo', 'vpravo', 'krok', 'zdvihni', 'poloz':
##    • robot je natočený v jednom zo štyroch smerov, označovať ich budeme takto:
##        0 na východ, 1 na juh, 2 na západ, 3 na sever
##    • príkazy 'vlavo', resp. 'vpravo' otočia robota v danom smere
##    • príkazom 'krok' robot prejde v momentálnom smere na susedné políčko,
##        ak je už na okraji siete, z plochy nevypadne, ale v danom smere nevykoná nič
##    • príkazom 'zdvihni' zoberie kartičku z políčka pod sebou a vloží ju do batoha;
##        ak na danom políčku nebola žiadna kartička, príkaz nevykoná nič;
##        ak na danom políčku bolo na sebe viac kartičiek, robot zdvihne najvrchnejšiu z nich;
##        kartičky vkladá do batoha na seba v poradí ako ich zdvíhal z plochy
##        (naspodku je prvá, na vrchu je naposledy zdvihnutá)
##    • príkazom 'poloz' vyberie najvrchnejšiu kartičku z batoha
##        a vloží ju na políčko pod seba; ak bol batoh prázdny, príkaz neurobí nič;
##        ak na políčku už boli nejaké kartičky pred tým,
##        novú kartičku položí na vrch týchto kartičiek.
##
##Zadanie štvorcovej siete s počiatočným rozložením kartičiek je v textovom súbore.
##V prvom riadku je dvojica celých čísel, ktorá popisuje veľkosť štvorcovej siete:
##    počet riadkov a počet stĺpcov. Za tým nasleduje informácia o kartičkách v ploche
##    - v každom riadku je symbol na kartičke a dvojica celých čísel,
##    ktoré označujú riadok a stĺpec pozície kartičky (číslujeme od 0).
##    Na jednom políčku sa môže nachádzať aj viac kartičiek.
##
##Naprogramuj triedu RobotKarel:
##class RobotKarel:
##    def __init__(self, meno_suboru):
##        ...
##
##    def __str__(self):
##        return ''
##
##    def robot(self, riadok, stlpec, smer):
##        ...
##
##    def rob(self, prikaz):
##        return 0
##
##    def batoh(self):
##        return []
##kde:
##    • init prečíta súbor - robot tam zatiaľ nie je
##    • __str__ vráti znakovú reprezentáciu plochy:
##        pozíciu robota zapíš (podľa momentálneho natočenia)
##        jedným zo znakov '>', 'v', '<', '^',
##        ak je na políčku viac kartičiek, zobrazí sa iba najvrchnejšia z nich,
##        prázdne políčko zobraz znakom '.';
##        ak je robot na políčku s kartičkami, zobrazí sa iba robot
##    • robot položí robota na zadaný riadok a stĺpec s daným otočením
##        (číslo od 0 do 3)
##    • rob dostáva jeden povel, alebo postupnosť za sebou nasledujúcich povelov,
##        pričom povel je jeden z reťazcov
##        'vlavo', 'vpravo', 'krok', 'zdvihni', 'poloz',
##        ktorý môže mať na začiatku aj celé číslo, vtedy to označuje počet opakovaní;
##        napríklad '3 krok' označuje tri kroky za sebou;
##        robot sa postupne pohybuje v danom smere, pričom zbiera, resp. kladie kartičky;
##        povely, ktoré sa nedajú vykonať, ignoruje;
##        funkcia vráti počet tu vykonaných ale neignorovaných povelov
##    • metóda batoh vráti momentálny zoznam kartičiek so symbolmi v batohu
##        (prvým prvkom je najspodnejšia kartička, posledným je najvrchnejšia)
##    • odporúčame štvorcovú sieť reprezentovať ako dvojrozmernú tabuľku (zoznam zoznamov),
##        v ktorej každý prvok je buď reťazec (postupnosť znakov) alebo zoznam znakov,
##        políčka bez kartičiek reprezentuj prázdnym reťazcom, resp. zoznamom
##
##Napríklad, pre súbor 'subor1.txt':
##3 4
##N 1 3
##O 1 2
##H 1 1
##P 0 1
##Y 0 2
##T 0 3
##
##a testovanie môžeš využiť tento kód
##(umiestni ho za definíciu triedy, môže ostať v module,
## aj keď ho budeš odovzdávať na testovanie):
##if __name__ == '__main__':
##    k = RobotKarel('subor1.txt')
##    k.robot(0, 0, 0)
##    print(k)
##    print(k.rob('krok'))
##    print(k.rob('2 zdvihni'))
##    k.rob('krok')
##    k.rob('vpravo')
##    k.rob('krok')
##    k.rob('2 zdvihni')
##    k.rob('2 krok')
##    print(k)
##    print('batoh =', k.batoh())
##    k.rob('poloz vlavo')
##    k.rob('krok 6 vlavo')
##    print(k)
##    print('batoh =', k.batoh())
##
##vypíše:
##>PYT
##.HON
##....
##1
##1
##..YT
##.H.N
##..v.
##batoh = ['P', 'O']
##..YT
##.H.N
##..O<
##batoh = ['P']
##
##Z úlohového servera L.I.S.T. si stiahni kostru programu riesenie.py.
##Pozri si testovacie dáta v súboroch 'subor1.txt', 'subor2.txt', 'subor3.txt', …, ktoré bude používať testovač.
##Tvoj odovzdaný program s menom riesenie.py musí začínať tromi riadkami komentárov:
### 9. zadanie: karel
### autor: Janko Hraško
### datum: 10.12.2021
##Projekt riesenie.py odovzdaj (bez dátových súborov) na úlohový server L.I.S.T. najneskôr do 10. decembra.
##Môžeš zaň získať 5 bodov.
                                                                            #
#8. zadanie: stvorce
#autor: Dalibor Sova
#datum: 13.4.2023


#úvodní a prázdný řádek:                                                  
print('TÝDENÍ PROJEKT 16 LEKCE')                              
print('''
Program obsahuje třídu RobotKarel,
která z textového souboru načte instrukce k vytvoření hrací plochy,
kde v čtvercové síti jsou rozmístěny určité kartičky  a robotr Karel,
a naším úkolem je navigovat robota, aby kartičky posbíral.

Třída RobotKartel obsahuje následující metody:

1) inicializační funkce __init__(textový soubor)
    povinný parametr - textový soubor s instrukcema
    inicializační funkce přečte soubour
    a dle instrukcí vytvoří hrací plochu.
    Také obsahuje funkci pro kontrolu chyb textového souboru

2) metoda __str__
    bez parametrů
    metoda vrátí řetězec pro výpis aktuální tabulky

3) metoda robot(řádek, sloupec, směr),
    povinný parametr - řádek a sloupec umístění robota
    a směr natočení
    metoda dle parametrů umístí do plochy robota

4) metoda rob(textový řetězec s příkazi), 
    povinný parametr - textový řetězec s příkazi
    rozlišule celkem 5 textových příkazů:
        1) vlevo - otočí robota vlevo
        2) vpravo - otočí robota vpravo
        3) krok - posune robota směrem otočení
        4) zdvihni - zvedne kartičku a vloží ji do batohu
        5) poloz - vezme kartičku z batohu a položí na plochu
    textových příkazů je možné zadávat v jednom řetězci víc,
    musí být ale odděleny prázdnou mezerou.
    Pokud chceme některý příkaz opakovat vícekrát,
    je možné před příkaz zapsat hodnotu opakování číslicí
    a od příkazu ji oddělit prázdnou mezerou.

5) metoda batoh()
    bez parametrů
    metoda vrátí řetězec pro výpis aktuálního obsahu batohu
''')

1234567890123456789012345678901234567890123456789012345678901234567890123456789


                
class RobotKarel:                                                               #definice třídy RobertKarel
    def __init__(self, jmeno_souboru):                                              #definice metody __init__
        self.jmeno_souboru = jmeno_souboru                                              #přiřazení atributu pro jméno snačteného souboru

        def kontrola_radku(radek, cislo_radku):                                         #definice vnitřní funkce pro kontrolu chyb načteného textového souboru
            text0 = '>> CHYBA! <<\n'                                                        #text cybové odpovědi
            text1 = f'>> {cislo_radku}. řádek souboru {self.jmeno_souboru} <<\n'            #text cybové odpovědi
            text2 = '>> má obsahouvat 2 parametry: <<\n'                                    #text cybové odpovědi
            text3 = '>> 1) počet řádků <<\n>> 2) počet sloupců <<\n'                        #text cybové odpovědi
            text4 = '>> má obsahouvat 3 parametry: <<\n'                                    #text cybové odpovědi
            text5 = '>> 1) hodnotu karničky <<\n>> 2) číslo řádku <<\n>> 3) číslo sloupce <<\n'     #text cybové odpovědi
            text6 = f'>> obsah řádku: {radek} <<\n'                                         #text cybové odpovědi
            text7 = '>> má obsahovat dva číselné údaje <<\n'                                #text cybové odpovědi
            text8 = '>> má na 2. a 3. pozici obsahovat dva číselné údaje <<\n'              #text cybové odpovědi
            
            if cislo_radku == 1:                                                            #podmínka - když se jedná o první řádek
                if len(radek) != 2:                                                             #podmínka - když na prvním řádku nejsou jen 2 parametry 
                    print(text0, text1, text2, text3, text6)                                        #výstup - vypiš pro tuto chybu, tyto texty
                if not radek[0].isnumeric() or not radek[1].isnumeric():                        #podmínka - když hodnoty nejsou čísla
                    print(text0, text1, text7, text6)                                               #výstup - vypiš pro tuto chybu, tyto texty
            else:                                                                           #podmínka - když se nejedná o první řádek
                if len(radek) != 3:                                                             #podmínka - když na řádku nejsou pouze 3 parametry 
                    print(text0, text1, text4, text5, text6)                                        #výstup - vypiš pro tuto chybu, tyto texty
                if not radek[1].isnumeric() or not radek[2].isnumeric():                        #podmínka - když druhá a třetí hodnota nejsou čísla
                    print(text0, text1, text8, text6)                                               #výstup - vypiš pro tuto chybu, tyto texty
                
        soubor = open(self.jmeno_souboru, 'r')                                          #otevření souboru
        print(f'>> soubor {self.jmeno_souboru} byl načten <<')                          #oznam o provedené akci

        prvni_radek = soubor.readline().split()                                         #načtení prvního řádku do lokální proměnné
        cislo_radku = 1                                                                 #přiřazení hodnoty do proměnné pro číslo řádku
        kontrola_radku(prvni_radek, cislo_radku)                                        #volání vnitřní funkce pro kontrolu řádku

        self.pocet_radku = int(prvni_radek[0])                                          #přiřazení hodnot do atributu pro počet řádků tabulky
        self.pocet_sloupcu = int(prvni_radek[1])                                        #přiřazení hodnot do atributu pro počet sloupců tabulky
        self.herni_plocha = []                                                          #přiřazení prázdného seznamu do atributu pro tabulku

        for radek in range(self.pocet_radku):                                           #cyklus dle počtu řádků
            self.herni_plocha.append([])                                                    #přidej do seznamu pro tabulku prázdný seznam
            for sloupec in range(self.pocet_sloupcu):                                       #cyklus dle počtu sloupců
                self.herni_plocha[-1].append([])                                                #přidej do posledního přidaného seznamu pro řádek prázdný seznam
        print('>> byla vytvořena tabulka herní plochy <<')                              #oznam o provedené akci
        print(f'>> počet řádků: {self.pocet_radku}, počet sloupců: {self.pocet_sloupcu} <<')    #oznam o provedené akci

        dalsi_radek = soubor.readline().split()                                         #načtení dalšího řádku do lokální proměnné
        cislo_radku = 2                                                                 #přiřazení hodnoty do proměnné pro číslo řádku
 
        while len(dalsi_radek) > 0:                                                     #cyklus, dokud není proměnná pro další řádek prázdná
            kontrola_radku(dalsi_radek, cislo_radku)                                        #volání vnitřní funkce pro kontrolu řádku
            symbol = dalsi_radek[0]                                                         #přiřazení hodnot do lokální proměnné pro symbol (kartu)
            radek, sloupec = int(dalsi_radek[1]), int(dalsi_radek[2])                       #přiřazení hodnot do lokální proměnné pro řádek a sloupec
            self.herni_plocha[radek][sloupec].append(symbol)                                #změna v tabulce pro hrací plochu - přiřazení kartičky na dané umístění
            dalsi_radek = soubor.readline().split()                                         #načtení dalšího řádku do lokální proměnné      
            cislo_radku += 1                                                                #přiřazení hodnoty do proměnné pro číslo řádku
        print(f'>> do herní plochy bylo umístěno {cislo_radku-1} kartiček <<')          #oznam o provedené akci

        soubor.close()                                                                  #zavření souboru
        print(f'>> soubor {self.jmeno_souboru} byl uzavřen <<')                         #oznam o provedené akci


    def __str__(self):                                                              #definice metody __str__
        vystup = ''                                                                     #vytvoření lokální proměnné pro výstupný textový soubor
        for radek in self.herni_plocha:                                                 #cyklus dle řádků v herní ploše
            for sloupec in radek:                                                           #cyklus dle sloupců v herní ploše 
                if len(sloupec) == 0:                                                           #podmínka, když je pozice prázdná
                    vystup += '.'                                                                   #přidej do lokální proměnné pro výstupný textový soubor tečku
                else:                                                                           #podmínka, když pozice není prázdná
                    if sloupec[-1] in (0, 1, 2, 3):                                                 #podmínka, když na pozici je 0, 1, 2, 3
                        znak = ['>', 'v', '<', '^']                                                     #dočasná proměnná pro tabulku zástupných hodnot
                        vystup += znak[sloupec[-1]]                                                     #přidej do lokální proměnné pro výstupný textový soubor příslušný znak z tabulky zástupných hodnot
                    else:                                                                           #podmínka, když na pozici je jiný znak než 0, 1, 2, 3
                        vystup += sloupec[-1]                                                           #přidej do lokální proměnné pro výstupný textový soubor příslušný znak 
            vystup += '\n'                                                                  #po vyplnění sloupců uvnitř řádku, přidej na konec řádku znak pro nový řádek
        return vystup.rstrip()                                                          #návratová hodnota - vrať obsah lokální proměnné pro výstupný textový soubor bez posledního znaku (odskok na nový řádek)
        

    def robot(self, radek, sloupec, smer):                                          #definice metody robot
        self.batuzek = []                                                               #vytvoření prázdného seznamu a atributu baťůžek
        self.robot_radek = radek                                                        #přiřazení hodnoty a vytvoření atributu pro řádek umístění robota 
        self.robot_sloupec = sloupec                                                    #přiřazení hodnoty a vytvoření atributu pro sloupec umístění robota 
        self.robot_smer = smer                                                          #přiřazení hodnoty a vytvoření atributu pro směr umístění robota 
        self.herni_plocha[radek][sloupec].append(smer)                                  #umístění robota do seznamu pro hrací plochu
        print('>> do herní plochy byl umístěn robot Karel <<')                          #oznam o provedené akci
        print(f'>> na umístění {radek}.řádek a {sloupec}.sloupec <<')                   #oznam o provedené akci
        print(f'>> směrem na {["východ", "jih", "západ", "sever"][smer]} <<')           #oznam o provedené akci


    def rob(self, prikaz):                                                          #definice metody rob
        seznam_prikazu = prikaz,                                                        #přiřazení hodnot do lokální proměnné pro seznam příkazů
        if ' ' in prikaz:                                                               #podmínky, když je příkaz složen z více příkazů
            seznam_prikazu = prikaz.split()                                                 #rozřaď tyto příkazy do lokální proměnné pro seznam příkazů

        ppp = pocet_provedenych_prikazu = 1                                             #vytvoření lokální proměnný a zástupné zkratky pro počet provedených příkazů
        po = pocet_opakovani = 1                                                        #vytvoření lokální proměnný a zástupné zkratky  pro počet opakování
        for prikaz in seznam_prikazu:                                                   #cyklus pro každý příkaz ze seznamu příkazů
            if prikaz.isnumeric():                                                          #podmínka, pokud příkaz je číslo
                pocet_opakovani = int(prikaz)                                                   #vlož tuto hodnotu do lokální proměnné pro počet opakování

            else:                                                                           #podmínka, pokud příkaz není číslo
                if prikaz == 'vlevo':                                                           #podmínka, když je příkazem slovo vlevo
                    self.robot_smer -= pocet_opakovani%4                                            #odečti od atributu pro směr robota zbytek po dělení 4 z lokální proměnné pro pocet opakování
                    if self.robot_smer < 0:                                                         #podmínka, když atribut pro směr robota má menší hodnotu naž 0
                        self.robot_smer = [0, -3, -2, -1].index(self.robot_smer)                        #změň tuto hodnotu na její kladný ekvivalent
                    self.herni_plocha[self.robot_radek][self.robot_sloupec].pop()                   #odstraň z atributu hrací plochy robota
                    self.herni_plocha[self.robot_radek][self.robot_sloupec].append(self.robot_smer) #vrať do atributu hrací plochy robota s novým nastavením směru
                    pocet_provedenych_prikazu = pocet_opakovani%4                                   #aktualizuj hodnotu lokální proměnné pro počet opakování
                    print(f'>> byl {pocet_provedenych_prikazu}x proveden příkaz otočení vlevo <<')  #oznam o provedené akci

                elif prikaz == 'vpravo':                                                        #podmínka, když je příkazem slovo vpravo
                    self.robot_smer = (self.robot_smer + pocet_opakovani)%4                         #přičti k atrubutu pro směr robota hodnotu lokální proměnné pro počet opakování a použij zbytek po dělení 4
                    self.herni_plocha[self.robot_radek][self.robot_sloupec].pop()                   #odstraň z atributu hrací plochy robota
                    self.herni_plocha[self.robot_radek][self.robot_sloupec].append(self.robot_smer) #vrať do atributu hrací plochy robota s novým nastavením směru
                    pocet_provedenych_prikazu = pocet_opakovani%4                                   #aktualizuj hodnotu lokální proměnné pro počet opakování
                    print(f'>> byl {pocet_provedenych_prikazu}x proveden příkaz otočení vpravo <<') #oznam o provedené akci

                elif prikaz == 'krok':                                                          #podmínka, když je příkazem slovo krok
                    self.herni_plocha[self.robot_radek][self.robot_sloupec].pop()                   #odstraň z atributu hrací plochy robota
                    if self.robot_smer == 1:                                                        #podmínka, když je směr robota 1 (na jih)
                        self.robot_radek += pocet_opakovani                                             #přičti k hodnotě atributu pro řádek robota hodnotu proměnné pro počet opakování
                        if self.robot_radek > self.pocet_radku-1:                                       #podmínka, když hodnota atributu pro řádek robota je větší než hodnota atributu pro počet řádků
                            ppp = self.pocet_radku-1 - (self.robot_radek - po)                              #aktualizuj hodnotu lokální proměnné pro počet opakování
                            self.robot_radek = self.pocet_radku-1                                           #změň hodnotu atributu pro řádek robota

                    if self.robot_smer == 3:                                                    #podmínka, když je směr robota 3 (na sever)
                        self.robot_radek -= pocet_opakovani                                         #odečti k hodnotě atributu pro řádek robota hodnotu proměnné pro počet opakování
                        if self.robot_radek < 0:                                                    #podmínka, když hodnota atributu pro řádek robota je menší než nula
                            ppp = self.robot_radek + po                                                 #aktualizuj hodnotu lokální proměnné pro počet opakování
                            self.robot_radek = 0                                                        #změň hodnotu atributu pro řádek robota

                    if self.robot_smer == 0:                                                    #podmínka, když je směr robota 0 (na východ)
                        self.robot_sloupec += pocet_opakovani                                       #přičti k hodnotě atributu pro sloupec robota hodnotu proměnné pro počet opakování
                        if self.robot_sloupec > self.pocet_sloupcu-1:                               #podmínka, když hodnota atributu pro sloupec robota je větší než hodnota atributu pro počet sloupců
                            ppp = self.pocet_sloupcu-1 - (self.robot_sloupec - po)                      #aktualizuj hodnotu lokální proměnné pro počet opakování
                            self.robot_sloupec = self.pocet_sloupcu-1                                   #změň hodnotu atributu pro sloupec robota

                    if self.robot_smer == 2:                                                    #podmínka, když je směr robota 2 (na západ)
                        self.robot_sloupec -= pocet_opakovani                                       #odečti k hodnotě atributu pro sloupec robota hodnotu proměnné pro počet opakování
                        if self.robot_sloupec < 0:                                                  #podmínka, když hodnota atributu pro sloupec robota je menší než nula
                            ppp = self.robot_sloupec + po                                               #aktualizuj hodnotu lokální proměnné pro počet opakování
                            self.robot_sloupec = 0                                                      #změň hodnotu atributu pro sloupec robota

                    self.herni_plocha[self.robot_radek][self.robot_sloupec].append(self.robot_smer)     #vrať do atributu hrací plochy robota na novou pozici
                    print(f'>> byl {pocet_provedenych_prikazu}x proveden příkaz pohybu směrem na {["východ", "jih", "západ", "sever"][self.robot_smer]} <<')  #oznam o provedené akci

                elif prikaz == 'zdvihni':                                                       #podmínka, když je příkazem slovo zdvihni
                    if len(self.herni_plocha[self.robot_radek][self.robot_sloupec]) > 1:            #podmínka, když na daném umístění je alespoň jedna karta
                        pocet_provedenych_prikazu = 1                                                   #nastav hodnotu lokální proměnné pro počet příkazů na 1
                        self.herni_plocha[self.robot_radek][self.robot_sloupec].pop()                   #odstraň z atributu hrací plochy robota
                        karta = self.herni_plocha[self.robot_radek][self.robot_sloupec].pop()           #odeber kartu z atributu hrací plochy a vlož ji do baťůžku
                        self.batuzek.append(karta)                                                      #vlož do baťůžku kartu z lokální proměnné
                        self.herni_plocha[self.robot_radek][self.robot_sloupec].append(self.robot_smer) #vrať do atributu hrací plochy robota 
                        print(f'>> z polohy {self.robot_radek}.řádek a {self.robot_sloupec}.sloupec byla zvednuta a do batohu přidána karta "{karta}" <<')  #oznam o provedené akci
                    else:                                                                           #podmínka, když na daném místě není žádná karta
                        pocet_provedenych_prikazu = 0                                                   #nastav hodnotu lokální proměnné pro počet příkazů na 0
                        print(f'>> na uvedené poloze není žádná kata <<')                               #vypiš oznam

                elif prikaz == 'poloz':                                                         #podmínka, když je příkazem slovo polož
                    if len(self.batuzek) > 0:                                                       #podmínka, když v baťohu je alespoň jedna karta
                        pocet_provedenych_prikazu = 1                                                   #nastav hodnotu lokální proměnné pro počet příkazů na 1
                        karta = self.batuzek.pop()                                                      #vyndej kartu z baťůžku a vlož ji do lokální proměnné
                        self.herni_plocha[self.robot_radek][self.robot_sloupec].pop()                   #odstraň z atributu hrací plochy robota
                        self.herni_plocha[self.robot_radek][self.robot_sloupec].append(karta)           #vlož kartičku na dané umístění do atributu pro hrací plochu
                        self.herni_plocha[self.robot_radek][self.robot_sloupec].append(self.robot_smer) #vrať do atributu hrací plochy robota 
                        print(f'>> na {self.robot_radek}.řádek a {self.robot_sloupec}.sloupec byla umístěna karta "{karta}" <<')  #oznam o provedené akci
                    else:                                                                           #podmínka, když v baťůžku není žádná karta
                        pocet_provedenych_prikazu = 0                                                   #nastav hodnotu lokální proměnné pro počet příkazů na 0
                        print(f'>> váš batoh neobsahuje žádnou kartu <<')                               #vypiš oznam

                else:                                                                           #podmínka, když se nejedná o žádný z výše uvedených příkazů
                    print(f'!!! neznámý, či chybně zapsaný, příkaz: {prikaz} !!!')                  #vypiš oznam
                pocet_opakovani = 1                                                             #nastav hodnotu lokální proměnné pro počet příkazů na 1

        return pocet_provedenych_prikazu                                                #návratová hodnota - vrať obsah lokální proměnné pro počet provedených příkazů

    def batoh(self):                                                                #definice metody baťoh
        return self.batuzek                                                             #návratová hodnota - vrať obsah atributu baťůžek


print('''
---------------------------------------------------------------------
Ukázka správné funkčnosti programu pro vytvoření
hrací tabulky (plochy) z textového souboru 16_13_soubor.txt,
který obsahuje následující instrukce:
3 4
O 2 2
P 0 1
Y 2 0
T 0 3
H 1 1
N 2 2''')
input('''
---------------------------------------------------------------------
Zmáčkni [enter] pro vytvoření instance "k",
načtení textového souboru a umístění robota na první políčko
hrací plochy, aktivací příkazů:

>>> k = RobotKarel('16_13_soubor.txt')
>>> k.robot(0, 0, 0)

a následném zobrazení vytvořené hrací plocha
a obsahu baťůžku příkazy print(k) a print(k.batuzek)
''')
k = RobotKarel('16_13_soubor.txt')
k.robot(0, 0, 0)
print()
print('Hrací plocha: ')
print(k)
print()
print('Obsah baťůžku: ', k.batuzek)

input('''
---------------------------------------------------------------------
Zmáčkni [enter] pro následující sadu příkazů
pro sebrání 1. kartičky:

>>> k.rob('krok zdvihni')

a následném zobrazení vytvořené hrací plocha
a obsahu baťůžku příkazy print(k) a print(k.batuzek)
''')
k.rob('krok zdvihni')
print()
print('Hrací plocha: ')
print(k)
print()
print('Obsah baťůžku: ', k.batuzek)

input('''
---------------------------------------------------------------------
Zmáčkni [enter] pro následující sadu příkazů
pro sebrání 2. kartičky:

>>> k.rob('vpravo 3 krok vpravo krok zdvihni')

a následném zobrazení vytvořené hrací plocha
a obsahu baťůžku příkazy print(k) a print(k.batuzek)
''')
k.rob('vpravo 3 krok vpravo krok zdvihni')
print()
print('Hrací plocha: ')
print(k)
print()
print('Obsah baťůžku: ', k.batuzek)

input('''
---------------------------------------------------------------------
Zmáčkni [enter] pro následující sadu příkazů
pro sebrání 3. kartičky:

>>> k.rob('6 vpravo 3 krok vlevo 5 krok zdvihni')

a následném zobrazení vytvořené hrací plocha
a obsahu baťůžku příkazy print(k) a print(k.batuzek)
''')
k.rob('6 vpravo 3 krok vlevo 5 krok zdvihni')
print()
print('Hrací plocha: ')
print(k)
print()
print('Obsah baťůžku: ', k.batuzek)

input('''
---------------------------------------------------------------------
Zmáčkni [enter] pro následující sadu příkazů
pro sebrání 4. kartičky:

>>> k.rob('vlevo 2 krok vlevo krok zdvihni')

a následném zobrazení vytvořené hrací plocha
a obsahu baťůžku příkazy print(k) a print(k.batuzek)
''')
k.rob('vlevo 2 krok vlevo krok zdvihni')
print()
print('Hrací plocha: ')
print(k)
print()
print('Obsah baťůžku: ', k.batuzek)

input('''
---------------------------------------------------------------------
Zmáčkni [enter] pro následující sadu příkazů
pro sebrání 6. kartičky (5. kartička je pod ní):

>>> k.rob('5 krok vlevo krok zdvihni')

a následném zobrazení vytvořené hrací plocha
a obsahu baťůžku příkazy print(k) a print(k.batuzek)
''')
k.rob('5 krok vlevo krok zdvihni')
print()
print('Hrací plocha: ')
print(k)
print()
print('Obsah baťůžku: ', k.batuzek)

input('''
---------------------------------------------------------------------
Zmáčkni [enter] pro následující sadu příkazů
pro položení bokem 6. kartičky:

>>> k.rob('krok poloz')

a následném zobrazení vytvořené hrací plocha
a obsahu baťůžku příkazy print(k) a print(k.batuzek)
''')
k.rob('krok poloz')
print()
print('Hrací plocha: ')
print(k)
print()
print('Obsah baťůžku: ', k.batuzek)

input('''
---------------------------------------------------------------------
Zmáčkni [enter] pro následující sadu příkazů
pro sebrání 1. kartičky:

>>> k.rob('2 vpravo krok zdvihni')

a následném zobrazení vytvořené hrací plocha
a obsahu baťůžku příkazy print(k) a print(k.batuzek)
''')
k.rob('2 vpravo krok zdvihni')
print()
print('Hrací plocha: ')
print(k)
print()
print('Obsah baťůžku: ', k.batuzek)

input('''
---------------------------------------------------------------------
Zmáčkni [enter] pro následující sadu příkazů
pro sebrání 1. kartičky:

>>> k.rob('2 vpravo krok zdvihni')

a následném zobrazení vytvořené hrací plocha
a obsahu baťůžku příkazy print(k) a print(k.batuzek)
''')
k.rob('2 vpravo krok zdvihni')
print()
print('Hrací plocha: ')
print(k)
print()
print('Obsah baťůžku: ', k.batuzek)

input('''
---------------------------------------------------------------------
Zmáčkni [enter] pro ukončení programu''')

