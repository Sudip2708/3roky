##  Napíš funkciu rozdel(retazec),
##  ktorá daný reťazec rozdelí na podreťazce a tieto vráti ako zoznam reťazcov.
##  Podreťazce sú navzájom oddelené aspoň jednou medzerou alebo znakom '\n'.
##  Funkcia nič nevypisuje. Nepoužívaj split.
##  Napríklad:
##    >>>zoz = rozdel('  jeden   dva tri')
##    >>>zoz
##        ['jeden', 'dva', 'tri']
##    >>>rozdel(input('zadaj cisla:'))
##        zadaj cisla:11 234 5 5789
##        ['11', '234', '5', '5789']
##    >>>rozdel('ah\noj\n')
##        ['ah', 'oj']


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - ROZDĚL TEXT NA SEZNAM')
print('funkce rozdělí text oddělený mezerami na jednotlivé položky seznamu')
print()


#definování funkce:
def rozdel(retazec):
    'vrátí znaky a slova oddělené mezerou, nebo novým řádkem jako položky seznamu'
    mezera = False                                          #promněná pro ukazatel, zda je nárok na mezeru (nový řádek)
    n_retazec = ''                                          #proměnná pro nový řetězec
    seznam = []                                             #proměnná pro tvořený seznam
    for i in retazec:                                       #cyklus - pro každý znak řetězce
        if i == ' ' or i == '\n':                           #podmínka - když znak obsahuje mezeru, nebo nový řádek
            if mezera == True:                              #podmínka - když je nárok na mezeru
                n_retazec += '\n'                           #přidej do nového řetězce za slovo znak pro nový řádek
                mezera = False                              #zruš nárok na mezeru
        else:                                               #podmínka - když znak neobsahuje mezeru nebo nový řádek
            n_retazec += i                                  #přidej tento znak do nového řetězce
            mezera = True                                   #aktivuj nárok na mezeru
    if n_retazec[-1] != '\n':                               #podmínka - kdyžna konci výsledného řetězce není znak pro nový řádek
        n_retazec += '\n'                                   #přidej na konec znak pro nový řádek
    for i in range(n_retazec.count('\n')):                  #cyklus - dle počtu znaků pro nový řádek
        seznam.append(n_retazec[:n_retazec.find('\n')])     #přidej do seznamu položku složenou se znaků před znakem pro nový řádek
        n_retazec = n_retazec[n_retazec.find('\n')+1:]      #odeber z původního řetězce již zpracovanou čát
    return(seznam)                                          #vrať seznam


#vstup:
a = input('''Zapiš text, kde hodnoty jsou odděleny mezerami a zmáčkni [enter]:
''')
print()


#výstup:
print('Výsledný seznam:')
print(rozdel(a))
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
