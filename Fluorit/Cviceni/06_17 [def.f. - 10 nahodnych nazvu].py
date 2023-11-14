##  Napíš funkciu nazov(n),
##  pomocou ktorej sa bude dať vygenerovať názov hudobnej skupiny.
##  Chceme, aby toto meno začínalo a končilo rovnakou samohláskou
##  a medzi týmito samohláskami by sa malá n krát objaviť nejaká spoluhláska.
##  Prvé písmeno mena by malo byť veľké ostatné malé.
##  Zrejme využiješ ideu z 2. prednášky,
##  pomocou ktorej sa náhodne generovali písmená.
##
##  Môžeš dostať napríklad:
##    for i in range(5):
##      print(nazov(2))
##      print(nazov(3))
##    Uxxu
##    Uxxxu
##    Ippi
##    Idddi
##    Atta
##    Ottto
##    Yggy
##    Odddo
##    Aqqa
##    Ibbbi


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - NÁZEV SKUPINY')
print('funkce vygeneruje 10 náhodných názvů skupin z dvou písmen')
print('(pouze k zobrazení)')
print()


#import modulu:
import random


#definování funkce:
def nazov(n):
    a = random.choice('aeiouy')                     #náhodný výběr ze samohlásek
    d = random.choice('bcdefghjklmnpqrstvwxyz')     #náhodný výběr ze souhlásek
    return(a.upper()+ d*n + a)                      #vrať výsledený text


#výstup:
for i in range(5):
    print(nazov(2))
    print(nazov(3))
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
