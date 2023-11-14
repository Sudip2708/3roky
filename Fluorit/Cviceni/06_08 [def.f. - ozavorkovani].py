##  Napíš funkciu ozatvorkuj(retazec, podretazec),
##  ktorá v zadanom reťazci retazec všetky výskyty daného podreťazca ozátvorkuje.
##
##  Napríklad:
##  >>>b = ozatvorkuj('Bratislava', 'a')
##  >>>b
##    'Br(a)tisl(a)v(a)'
##  >>>ozatvorkuj('prospešné programovanie v prologu', 'pro')
##    '(pro)spešné (pro)gramovanie v (pro)logu'


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - OZÁVORKOVÁNÍ')
print('funkce ozávorkuje v zadaném textu námi hledané části')
print()


#definování funkce:
def ozatvorkuj(retazec, podretazec):
    return(retazec.replace(podretazec, f'({podretazec})'))  #nahrazení hledaného podřetězce, stejnou hodnotou v závorkách


#vstup:
retazec = input('Zadej text v kterém chceš hledat: ')
podretazec = input('Zadej text, který chceš ozávorkovat: ')
print()


#výstup:
print(f'Výsledný text: {ozatvorkuj(retazec, podretazec)}')
     

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
