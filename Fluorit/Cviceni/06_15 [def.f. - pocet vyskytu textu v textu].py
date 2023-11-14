##  Metóda 'reťazec'.count(podreťazec) zisťuje počet výskytov podreťazca v reťazci.
##  Napíš funkciu pocet(retazec, podretazec),
##  ktorá robí to isté, ale bez použitia tejto metódy.
##
##  Napríklad:
##    >>>pocet('mama ma emu a ema ma mamu', 'ma ')
##        4
##    >>>pocet('mama ma emu a ema ma mamu', 'am')
##        2


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - POČET VÝSKYTŮ')
print('funkce dohledá a zobrazí, kolikrát se v zadaném řetězci objevuje hledaný podřetězec')
print()


#definování funkce:
def pocet(retazec, podretazec):
    count = 0                                                           #promněná pro počítadlo výskytů
    while retazec.find(podretazec) != -1:                               #cyklus - dokud text obsahuje hledaný podřetězec
        count += 1                                                      #připočti 1 do počítadla výskytů
        retazec =  retazec[retazec.find(podretazec)+len(podretazec):]   #řetězec skrať o část před podřetězcem a podřetězec
    return(count)                                                       #vrať výsledek počítadla výskytů


#vstup:
retazec = input('Zadej hlavní text: ')
podretazec = input('Zadej hledaný text: ') 


#výstup:
print(f'Ve vámi zadaném textu se hledaný text objevuje {pocet(retazec, podretazec)}x.')
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
