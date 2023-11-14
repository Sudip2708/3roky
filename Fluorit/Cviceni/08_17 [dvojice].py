##  Napíš funkciu dvojice(zoznam),
##  ktorá v danom zozname spočíta (alebo zreťazí) dvojice prvkov.
##  Teda spočíta/zreťazí (operácia +) prvý a druhý prvok
##  a oba nahradí týmto súčtom, potom to isté s tretím a štvrtým,
##  potom piatym a šiestym, atď.
##  Funkcia nič nevracia ani nevypisuje, len modifikuje obsah zoznamu.
##  Napríklad:
##    >>>z =list('programovanie')
##    >>>dvojice(z)
##    >>>z
##        ['pr', 'og', 'ra', 'mo', 'va', 'ni', 'e']
##    >>>z =list(range(1, 11))
##    >>>z
##        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##    >>>dvojice(z)
##    >>>z
##        [3, 7, 11, 15, 19]
##    >>>dvojice(z)
##    >>>z
##        [10, 26, 19]


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - DVOJICE')
print('funkce spočítá, nebo zřetězí, každé dva sousedící prvky seznamu')
print()


#definování funkce:
def dvojice(seznam):
    for i in range(len(seznam)//2):
        seznam[i:i+2] = [seznam[i] + seznam[i+1]]


#seznamy:
a = list('programovanie')
b = list(range(1, 11))


#intro:
print('-'*41)
print('První seznam, pro ukázku funkce:')
print(a)
print('-'*41)
print('Druhý seznam, pro ukázku funkce:')
print(b)
print('-'*41)
print()
input('zmáčkni [enter], pro ukázku funkce')
print()


#výstup:
print('-'*41)
print('Vzhled prvního seznamu, po použití funkce:')
dvojice(a)
print(a)
print()
print('Vzled po opakovaném použití funkce:')
dvojice(a)
print(a)
print('-'*41)
print('Vzhled druhého seznamu, po použití funkce:')
dvojice(b)
print(b)
print()
print('Vzled po opakovaném použití funkce:')
dvojice(b)
print(b)
print('-'*41)


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')     
