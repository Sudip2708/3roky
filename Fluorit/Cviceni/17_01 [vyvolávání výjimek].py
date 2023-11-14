##Do premennej a sme priradili reťazec '7 3'.
##Potom sme v príkazom riadku zapisovali pythonovské výrazy,
##ktoré obsahovali túto premennú a,
##okrem nej možno nejaké identifikátory, operátory,
##jednoznakové reťazce a z čísel len 0.
##Zakaždým sme dostali nejakú chybovú správu.
##Pre každú túto chybovú správu nájdi pythonovský výraz, ktorý ju vyvolal.
##Nepoužívaj príkaz raise:
##>>> a = '7 3'
##>>> ...
##    ValueError: ...
##>>> ...
##    TypeError: ...
##>>> ...
##    FileNotFoundError: ...
##>>> ...
##    ZeroDivisionError: ...
##>>> ...
##    AttributeError: ...
##>>> ...
##    NameError: ...
##>>> ...
##    AssertionError: ...
##>>> ...
##    OverflowError: ...


print('''VYVOLÁVÁNÍ VÝJIMEK

Zadáním bylo vyvolat následujících 8 výjimek za použití
proměnné "a" v které je uložen řetězec '7 3'
''')

print('''
1. výjimka, kterou máme za úkol vyvolat, je:

ValueError - výjimka, která nastane,
pokud funkce dostane parametr správného typu,
ale nekompatibilní hodnoty.
''')
input('zmáčkni [enter] pro zobrazení možného řešení')
print('''
a = '7 1'
int(a)

metoda int() celé číslo uložené jako textový řetězec.
V našem případě proměnná "a" obsahuje dvě čísla oddělená mezerou,
takže nemohla být metoda provedena a byl vyvolán ValueError
--------------------------------------------------------------------''')

print('''
2. výjimka, kterou máme za úkol vyvolat, je:

TypeError - výjimka, která nastane,
když je operace nebo funkce aplikovaná na nesprávný
datový typ.
''')
input('zmáčkni [enter] pro zobrazení možného řešení')
print('''
a = '7 1'
a + 1

znamínkem plus můžeme sčítat čísla, nebo slučovat textové řetězce,
nicméně vždy musí být hodnoty stejného typu.
V tomto případě se snažíme sloučit, či sečíst typ str a typ int,
takže k úkonu nemohlo dojít a byl vyvolán TypeError''')
print('--------------------------------------------------------------------')

print('''
3. výjimka, kterou máme za úkol vyvolat, je:

FileNotFoundError - výjimka, která nastane,
pokud není nalezen soubor, který se snažíme otevřít.
''')
input('zmáčkni [enter] pro zobrazení možného řešení')
print('''
a = '7 1'
open(a)

Proměnná "a" není soubor a tak když se ji pokusíme otevřít,
dojde k vyvolání FileNotFoundError''')
print('--------------------------------------------------------------------')

print('''
4. výjimka, kterou máme za úkol vyvolat, je:

ZeroDivisionError - výjimka, která nastane,
pokud druhým dělitelem je nula.
''')
input('zmáčkni [enter] pro zobrazení možného řešení')
print('''
a = '7 1'
len(a) / 0

pokud někdy nastane situace, že se dojde někde v programu k dělení nulou,
dojde k vyvolání výjimky ZeroDivisionError''')
print('--------------------------------------------------------------------')

print('''
5. výjimka, kterou máme za úkol vyvolat, je:

AttributeError - výjimka, která nastane,
pokud se odkazujeme na určitý atribut,
který v dané třídě, nebo modulu neexistuje.
''')
input('zmáčkni [enter] pro zobrazení možného řešení')
print('''
a = '7 1'
a.b()

proměnná "a" odkazuje na hodnotu typu str,
a tato třída nemá žádný atribut s názvem "b",
dojde tedy k vyvolání výjimky AttributeError''')
print('--------------------------------------------------------------------')

print('''
6. výjimka, kterou máme za úkol vyvolat, je:

NameError - výjimka, která nastane,
pokud není nalezena proměnná.
''')
input('zmáčkni [enter] pro zobrazení možného řešení')
print('''
a = '7 1'
a + b

proměnná "b" neexistuje a tak vyvolá výjimku NameError''')
print('--------------------------------------------------------------------')

print('''
7. výjimka, kterou máme za úkol vyvolat, je:

AssertionError - výjimka, která nastane,
když podmínka příkazu assert není splněna.
''')
input('zmáčkni [enter] pro zobrazení možného řešení')
print('''
a = '7 1'
assert isinstance(a, int), 'parametr není celé číslo'

příkazem assert testujeme určitou podmínku,
v této situaci, zda je proměnná "a" typu "int".
Assert umožňuje i kromě podmínky, kterou ověřuje,
přidat i popis chyby, který se objeví ve výpisu výjimky.
Není-li popis uveden, zobrazí se pouze AssertionError.''')
print('--------------------------------------------------------------------')

print('''
8. výjimka, kterou máme za úkol vyvolat, je:

OverflowError - výjimka, která nastane,
když výsledek aritmetické operace je příliš velký.
''')
input('zmáčkni [enter] pro zobrazení možného řešení')
print('''
a = '7 1'
len(a) ** 1000 / 1

příkaz len(a) ** 10000 (3 na tdesttisícou), Python ještě zvládne,
nicméně dělení takto velkého čísla už způsobí výjimku OverflowError''')
print('--------------------------------------------------------------------')

print('''
A to je vše :-)''')
input('zmáčkni [enter] pro ukončení programu')
