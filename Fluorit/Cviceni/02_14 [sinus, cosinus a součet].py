##  Napíš program, ktorý vytvorí takúto tabuľku:
##  pre všetky uhly (v stupňoch) z nejakého daného intervalu
##  a kroku vypíše druhé mocniny príslušných sínusov a kosínusov a aj ich súčet.
##  Druhé mocniny vypíše na šírku 6 a 4 desatinné miesta,
##  súčet bez udania šírky a počtu desatinných miest.
##
##  Môžeš dostať takýto výstup:
##
##    zadaj od: 0
##    zadaj do: 90
##    zadaj krok: 10
##      0 sin**2=0.0000 cos**2=1.0000 súčet=1.0
##     10 sin**2=0.0302 cos**2=0.9698 súčet=0.9999999999999999
##     20 sin**2=0.1170 cos**2=0.8830 súčet=1.0
##     30 sin**2=0.2500 cos**2=0.7500 súčet=1.0
##     40 sin**2=0.4132 cos**2=0.5868 súčet=0.9999999999999999
##     50 sin**2=0.5868 cos**2=0.4132 súčet=1.0
##     60 sin**2=0.7500 cos**2=0.2500 súčet=1.0
##     70 sin**2=0.8830 cos**2=0.1170 súčet=0.9999999999999999
##     80 sin**2=0.9698 cos**2=0.0302 súčet=0.9999999999999999
##     90 sin**2=1.0000 cos**2=0.0000 súčet=1.0


#úvodní a prázdný řádek:
print('SINUS, COSINUS A SOUČET')
print()


#vstupní data:
import math                                                             #importování modulu math
a = int(input('Zadej POČÁTEČNÍ ČÍSLO ÚHLU a po té zmáční [Enter]: '))   #vstup počáteční hodnoty
b = int(input('Zadej KONCOVÉ ČÍSLO ÚHLU a po té zmáční [Enter]: '))     #vstup koncové hodnoty
c = int(input('Zadej KROK a po té zmáční [Enter]: '))                   #vstup hodnoty kroku


#prázdný řádek
print()


#výpočet:
for i in range(a, b+1, c):
    d = math.radians(i)                                                 #uhol_v_radianoch
    e = math.sin(d) ** 2                                                #sin_uhla 
    f = math.cos(d) ** 2                                                #cos_uhla 
    print(f'{i:3} sin**2={e:6.4f} cos**2={f:6.4f} součet={e+f}')        #výpis řádků
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
