##  Napíš program, ktorý najprv prečíta do premennej txt nejaký text
##  a potom ho pomocou jediného print vypíše do 10 riadkov pod seba.
##  Premennú txt v príkaze print použi len raz.
##  Zrejme využiješ operáciu viacnásobného zreťazenia (*)
##  a tiež zreťazenia so špeciálnym znakom '\n'.
##
##  Po spustení môžeš dostať:
##
##    zadaj text: programujem v Pythone
##    programujem v Pythone
##    programujem v Pythone
##    programujem v Pythone
##    programujem v Pythone
##    programujem v Pythone
##    programujem v Pythone
##    programujem v Pythone
##    programujem v Pythone
##    programujem v Pythone
##    programujem v Pythone


#úvod
print('TEXT 10x POD SEBOU')
print()


#získání textu:
a = input('Zadej TEXT a zmáčkni [Enter]: ')


#prázdný řádek
print()


#výpis:
print((a + '\n') * 10)


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
