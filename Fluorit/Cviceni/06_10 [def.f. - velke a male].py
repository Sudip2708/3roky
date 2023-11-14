##  Napíš funkcie male(retazec, i) a velke(retazec, i),
##  ktoré i-te písmeno v reťazci prerobia na malé (resp. veľké).
##
##  Napríklad:
##    >>>r = male('PYTHON', 3)
##    >>>r
##        'PYThON'
##    >>>r = velke('python', 5)
##    >>>r
##        'pythoN'


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - VELKÉ A MALÉ')
print('''funkce v námi zadaném textu, změní v udané pozici,
v prvním řádku na velké znaky a v druhém řádku na malé.''')
print()


#definování funkcí:
def male(retazec, i):
    return(retazec[:i] + retazec[i:i+1].lower() + retazec[i+1:])    #vrácení spojeného textu z, části před a za hledaným znakem a malého znaku

def velke(retazec, i):
    return(retazec[:i] + retazec[i:i+1].upper() + retazec[i+1:])    #vrácení spojeného textu z, části před a za hledaným znakem a velkého znaku


# vstup:
retazec = input('Zadej text: ')
i = int(input('Zadej pozici: ')) - 1
print()

#výstup:
print(f'Změna na velké: {velke(retazec, i)}')
print(f'Změna na malé: {male(retazec, i)}')
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
