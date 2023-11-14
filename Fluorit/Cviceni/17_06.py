##V textovom súbore sa nachádza nejaký text,
##pričom slová sú oddelené medzerami.
##Tento súbor môže obsahovať aj čísla.
##Napíš funkciu iba_cisla(meno_suboru),
##ktorá vráti zoznam celých čísel z tohto súboru.
##Ak sa súbor nedá otvoriť, funkcia vráti prádny zoznam.
##Napríklad, ak súbor obsahuje:
##farmar ma 15 ovci a 127 sliepok
##pricom 18. februara bolo od -15 do +2 stupnov
##volanie funkcie vráti:
##>>> print(iba_cisla('subor.txt'))
##    [15, 127, -15, 2]


def iba_cisla(jmeno_souboru):
    cisla = []
    try:
        soubor = open(jmeno_souboru, 'r')
        radek = soubor.readline().split()
        while radek != []:
            for prvek in radek:
                try:
                    cisla.append(int(prvek))
                except (ValueError):
                    pass
            radek = soubor.readline().split()
        soubor.close()

    except (FileNotFoundError):
        pass
    return cisla


print(iba_cisla('17_06_cisla.txt'))
