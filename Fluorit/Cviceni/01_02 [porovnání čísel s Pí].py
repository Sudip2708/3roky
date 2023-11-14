##  Ludolfovo číslo pi rôzni matematici v histórii počítali podľa
##  zaujímavých magických vzorcov.
##
##    predpokladaj, že
##    pi = 3.141592653589793
##
##  zisti, ktorý so vzorcov sa k tomuto číslu pi priblížil najviac:
##
##    podiel 223 a 71
##    súčet zlomkov 22/17, 37/47 a 88/83
##    druhá mocnina 99 lomeno súčin 2206 krát druhá odmocnina z 2
##    druhá odmocnina z 5, k tomu plus 6, to celé druhá odmocnina, k tomu plus 7 a to celé opäť druhá odmocnina
##    10 na 100 lomeno 11222.11122 a to celé 193 odmocnina
##
##  Napríklad podiel 223 a 71 sa od pi líši o 0.0007475831672580924.

#úvod
print('ČKTERÉ ČÍSLO JE NEJBLÍŽE K PÍ?')
print()
input('[zmáčkni [Enter] pro zobrazení příkladů]')
print()

#příklady
print('1) Podíl 223 a 71')
print('2) Součet zlomků 22/17, 37/47 a 88/87')
print('3) Druhá mocnina 99 lomeno sůčin 2206 krát druhá odmocnina ze 2')
print('''4) Druhá odmocnina z 5, k tomu plus 6, to celé druhá mocnina, k tomu plus 7 a
   to celé opět druhá mocnina''')
print('5) 10 na 100 lomeno 11222.11122 a to celé 193 odmocnina')

print()
print('Předpokládej, že Pí je 3.141592653589793')
print()

print()
input('[zmáčkni [Enter] pro zobrazení výsledků]')
print()


#čílso Pi:
a = 3.141592653589793


#jednotlivé výpočty:
b = 223/71
c = 22/17 + 37/47 + 88/83
d = (99 ** 2) / (2206 * (2 ** (1/2)))
e = ((((5 ** (1/2)) + 6) ** (1/2)) + 7) ** (1/2)
f = ((10 ** 100) // 11222.11122) ** (1/193)


#absolutní hodnota rozdílů mezi Pi a jednotpivými výpočty:
b1 = abs(a - b)
c1 = abs(a - c)
d1 = abs(a - d)
e1 = abs(a - e)
f1 = abs(a - f)


#porovnání absolutních hodnot rozdílů (který je nejmenší):
if b1<c1 and b1<d1 and b1<e1 and b1<f1:
    print('Nejblíže z uvedeného seznamu k čísli Pi je:\npodiel 223 a 71')
elif c1<d1 and c1<e1 and c1<f1:
    print('Nejblíže z uvedeného seznamu k čísli Pi je:\nsúčet zlomkov 22/17, 37/47 a 88/83')
elif d1<e1 and d1<f1:
    print('Nejblíže z uvedeného seznamu k čísli Pi je:\ndruhá mocnina 99 lomeno súčin 2206 krát druhá odmocnina z 2')
elif c1<f1:
    print('Nejblíže z uvedeného seznamu k čísli Pi je:\ndruhá odmocnina z 5, k tomu plus 6, to celé druhá odmocnina, k tomu plus 7 a to celé opäť druhá odmocnina')
else:
    print('Nejblíže z uvedeného seznamu k čísli Pi je:\n10 na 100 lomeno 11222.11122 a to celé 193 odmocnina')


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
