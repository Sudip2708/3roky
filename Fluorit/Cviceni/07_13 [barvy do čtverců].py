##  Textový súbor obsahuje v každom riadku jedno meno farby.
##  Napíš funkciu do_riadkov(meno_suboru, sirka), ktorá vypíše rad štvorčekov (veľkosti 30x30).
##  Každý z týchto štvorčekov zafarbí príslušnou farbou zo súboru.
##  Po vykreslení sirka štvorčekov, pokračuje pod týmito v ďalšom rade štvorčekov s ďalšími farbami zo súboru.
##  Takto pokračuje, kým sa neminú všetky farby zo súboru.
##
##  Napríklad, pre súbor 'farby.txt':
##    red
##    blue
##    red
##    blue
##    yellow
##    red
##    yellow
##    red
##    green
##    yellow
##    yellow
##    green
##  volanie:
##    import tkinter
##    canvas = ...
##    do_riadkov('farby.txt', 4)
##  nakreslí:
##
##  Ak by sme tento súbor vypisovali do 5 stĺpcov, dostali by sme:


#úvodní a prázdný řádek:
print('BARVY Z TEXTU DO ČTVERCŮ V GRAFICKÉ PLOŠE')
print('''program obsahuje funkci na přečtení textového souboru obsahující 
jména barev a jejich následné vykreslení do grafické plochy''')
print()
print('soubor pro otestování: 07_13.txt')
print('počet barev na řádek v rozmezí: 2 - 10')
print()


#vstup:
meno_suboru = input('Zadej název souboru: ')
sirka = int(input('Zadej počet barev na řádek: '))


#definice funkce:
def do_riadkov(meno_suboru, sirka):
    soubor = open(meno_suboru)                                              #otevření souboru
    strana = 30                                                             #velikost strany čtverce
    x, y = 30, 30                                                           #přiřazení prvního bodu x, y
    mezera = 2                                                              #velikost mezery mezi čtverci
    pocitadlo = 0                                                           #počítadlo průběhů
    for radek in soubor:                                                    #cyklus - pro každý řádek ze souboru
        canvas.create_rectangle(x, y, x+strana, y+strana, fill=radek[:-1])  #vytvoř čtverec a vyplň barvou
        x = x+strana+mezera                                                 #posuň osu x
        pocitadlo += 1                                                      #připočti 1 do počítadla
        if pocitadlo%sirka == 0:                                            #podmínka - pokud počet v počítadle je dělitelný 4
            x = 30                                                          #změň x na počáteční hodnotu
            y =y+strana+mezera                                              #posuň osu y stranu čtverce a mezeru níž
    soubor.close()                                                          #zavření souboru


#import modulů:
import tkinter


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#výstup:
do_riadkov(meno_suboru, sirka)


#aktivace grafické aplikace:
tkinter.mainloop() 
    
