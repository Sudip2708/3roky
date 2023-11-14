##  Napíš a otestuj tieto funkcie.
##  Ich parametrom je meno nejakého textového súboru
##  a všetky vrátia (return) nejaký jeden riadok súboru:
##  funkcia posledny_riadok(meno_suboru)
##  funkcia predposledny_riadok(meno_suboru)
##  funkcia najdlhsi_riadok(meno_suboru)
##
##  Napríklad:
##    >>> posledny_riadok('text3.txt')
##    'pomôžte mi v mojom žiali'
##    >>> predposledny_riadok('text3.txt')
##    'a nožičky oheň páli'
##    >>> najdlhsi_riadok('text3.txt')
##    'a v tom tŕní chrastí rastie'


#úvodní a prázdný řádek:
print('TEXTOVÉ SOUBORY - POSLEDNÍ, PŘEDPOSLEDNÍ A NEJDELŠÍ ŘÁDEK')
print('''program obsahuje 3 funkce, které z načteného textu vrátí
poslední, předposlední a nejdelší řádek''')
print()
print('jméno souboru pro otestování: 07_08.txt')
print()


#definování funkce:
def posledny_riadok(meno_suboru):
    soubor = open(meno_suboru)                                  #proměnná pro otevření souboru
    vysledek = ''                                               #proměnná pro výsledek
    radek = soubor.readline()                                   #proměnná pro čtení řádku
    while radek:                                                #cyklus - dokud není konec textu
        vysledek = radek                                        #přiřaď řádek do výsledku
        radek = soubor.readline()                               #načti další řádek
    return vysledek[:-1]                                        #vrať výsledek bez znaku pro nový řádek
    soubor.close()                                              #zavření souboru


def predposledny_riadok(meno_suboru):
    soubor = open(meno_suboru)                                  #proměnná pro otevření souboru
    cely_soubor = soubor.read()                                 #proměnná pro celý text
    soubor.close()                                              #zavření souboru
    pocet_radku = cely_soubor.count('\n')                       #spočítání počtu řádků
    for i in range(pocet_radku - 2):                            #cyklus - dle počtu řádků mínus 2
        cely_soubor = cely_soubor[cely_soubor.find('\n')+1:]    #odseknutí již přečtené části
    return cely_soubor[:cely_soubor.find('\n')]                 #vrácení předposledního řádku
        

def najdlhsi_riadok(meno_suboru):
    soubor = open(meno_suboru)                                  #proměnná pro otevření souboru
    nejvetsi_pocet = 0                                          #proměnná největší počet znaků v řádku
    nejdelsi_radek = ''                                         #proměnná pro výpis nejdelšího řádku
    for i in soubor:                                            #cyklus - pro řádek v souboru
        if len(i) > nejvetsi_pocet:                             #podmínka - pokud je čtený řádek větší než hodnota v proměnné nejdelšího řádku
            nejvetsi_pocet = len(i)                             #zapiš tuto hodnotu do největší počet
            nejdelsi_radek = i                                  #zapiš tento řádek do nejdelšího řádku
    return nejdelsi_radek                                       #vrať nejdelší řádek
    soubor.close()                                              #zavření souboru


#vstup:
meno_suboru = input('Zadej název souboru: ')


#výstup:
print()
print('Poslední řádek je: ', posledny_riadok('07_text3.txt'))
print('Předposlední řádek je: ', predposledny_riadok('07_text3.txt'))
print('Nejdelší řádek je: ', najdlhsi_riadok('07_text3.txt'))
     

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')     
