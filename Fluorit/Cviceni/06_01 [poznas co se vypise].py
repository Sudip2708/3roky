##  Ručne bez počítača zisti, čo sa vypíše:
##    >>>x, y ='Bratislava', 'Košice'
##    >>>y[1] + x[4] + y[3] + x[-4] + y[-5]
##        ...
##    >>>x[5:8] +3* x[3] + y[2:]
##        ...
##    >>>y[:2] + x[-2:]
##        ...
##    >>>x[1::2] + y[2::2] + x[2::3]
##        ...
##    >>>x.replace('a', 'e') + y.replace('ic', 'm')
##        ...
##    >>>(y + x).replace('i', '').replace('a', 'xa')
##        ...
##
##  Potom to skontroluj pomocou Pythonu.


#úvodní a prázdný řádek:
print('POZNÁŠ CO SE VYPÍŠE?')
print('zkus nejprve z hlavy vypočíst, co se vypíše a pak si to nech zkontrolovat')
print()


#definování funkce:
def uloha(n, utext, uvysledek):
    print()
    input(f'Zmáčkni [Enter] pro zobrazení {n}. úlohy:')
    print(utext)
    print()
    ttip = input("Tvůj tip: ")
    print()
    if ttip == uvysledek:
        print("Tvůj tip je správně! Blahopřeji!")
        z += 1
    print("Tvůj tip není zcela správně.")
    print(f'Správný výsledek je: {uvysledek}')
    print('------------------------------------------')


#vstupní data:
x = 'Bratislava'
y = 'Košice'
z = 0


#zadání:
print("""
vstupní slova:

x = 'Bratislava'
y = 'Košice'""")
print('------------------------------------------')
uloha(1, "y[1] + x[4] + y[3] + x[-4] + y[-5]", y[1] + x[4] + y[3] + x[-4] + y[-5])
uloha(2, "x[5:8] +3* x[3] + y[2:]", x[5:8] +3* x[3] + y[2:])
uloha(3, "y[:2] + x[-2:]", y[:2] + x[-2:])
uloha(4, "x[1::2] + y[2::2] + x[2::3]", x[1::2] + y[2::2] + x[2::3])
uloha(5, "x.replace('a', 'e') + y.replace('ic', 'm')", x.replace('a', 'e') + y.replace('ic', 'm'))
uloha(6, "(y + x).replace('i', '').replace('a', 'xa')", (y + x).replace('i', '').replace('a', 'xa'))
print()
print(f'Z 6. úloh jsi měl {z} správně :-)')


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
