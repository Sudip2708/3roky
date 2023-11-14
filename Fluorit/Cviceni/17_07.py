##Napíš funkciu daj_cislo(meno_suboru, index, vynimka=None),
##ktorá predpokladá, že daný súbor má v každom riadku po jednom celom čísle.
##Funkcia vráti číselnú hodnotu z tohto riadka a ak sa to nedá
##(napríklad súbor neexistuje, nemá dosť riadkov,
## nie je v tomto riadku iba jediná celočíselná hodnota),
##vyvolá príslušnú výnimku s upresňujúcim textom.
##Ak treti parameter chýba, v prípade chyby funkcia vráti None.
##Napríklad:
##>>> daj_cislo('cvicenie.py', 17, IndexError)
##    ...
##    IndexError: chybne zadany index
##>>> daj_cislo('cvicenie.txt', 17, IndexError)
##    ...
##    IndexError: neexistujuci subor
##>>> daj_cislo('data.txt', 3, IndexError)
##    ...
##    IndexError: chybne cislo v zadanom riadku
##>>> daj_cislo('data.txt', 1, IndexError)
##    2020
##>>> print(daj_cislo('data.txt', '1'))
##    None
##Nezabudni zatvoriť otvorený súbor.



def dej_cislo(jmeno_souboru, index, vyjimka=None):
    try:
        soubor = open(jmeno_souboru, 'r')
        cely_soubor = soubor.read().split('\n')
        soubor.close()
        return int(cely_soubor[index-1])
        
    except FileNotFoundError:
        if vyjimka == None:
            return None
        raise vyjimka('neexistující soubor')
    except IndexError:
        if vyjimka == None:
            return None
        raise vyjimka('chybně zadaný index')
    except ValueError:
        if vyjimka == None:
            return None
        raise vyjimka('chybné číslo v zadaném řádku')
    

print(dej_cislo('17_07_cisla.txt', 2, IndexError))






