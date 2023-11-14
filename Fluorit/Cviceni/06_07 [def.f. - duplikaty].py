##  Napíš funkciu vyhod_duplikaty(retazec),
##  ktorá z daného reťazca vyhodí všetky za sebou idúce opakujúce sa znaky
##  (nechá len jeden z nich).
##
##  Napríklad:
##    >>>x = vyhod_duplikaty('Braatisssllavaaaaa')
##    >>>x
##    'Bratislava'


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - DUPLIKÁTY')
print('funkce projde námi zadaný znak a odstraní všechny výskyty zdvojení znaků')
print()


#definování funkce:
def vyhod_duplikaty(retazec):  
    b = retazec[0]                          #promněná nového textu s již zadaným prvním znakem
    for i in range (len(retazec)-1):        #cyklus - dle počtu znaků (mínus ten první)
        if retazec[i+1] == retazec[i]:      #podmínka - když další znak je stejný jako ten před ním
            pass                            #nedělej nic
        else:                               #jinak
            b += retazec[i+1]               #přičti znak k výslednému řetězci
    return(b)                               #vrať výsledný řetězec
        

#vstup:
retazec = input('Zadej text ze kterého chceš odstranit zdvojené znaky: ')
print()

#výstup:
print(f'Výsledný text: {vyhod_duplikaty(retazec)}')


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
