##7. Týždenný projekt	
##L.I.S.T.	
##•	riešenie odovzdaj na úlohový server https://list.fmph.uniba.sk/
##	
##Napíš pythonovský skript, v ktorom zadefinuješ päť funkcií na prácu so zoznamami:	
##•	number_of_lists(zoznam) … vráti int
##•	get_elements(zoznam) … vráti tuple
##•	flat_list(zoznam) … mení zoznam, teda vráti None
##•	nested_replace(zoznam, hodnota1, hodnota2) … vráti list
##•	change_values(zoznam, hodnota1, hodnota2) … mení zoznam, teda vráti None
##
##Vstupom pre tieto funkcie môže byť zoznam, ktorý môže obsahovať nielen čísla a reťazce, ale aj ďalšie podzoznamy.
##Tieto podzoznamy môžu opäť obsahovať ďalšie podzoznamy, atď.
##Napríklad aj takýto zoznam ['a', ['dom', [2], 3], [], [[[2]]], 'b'] môže byť vstupom do tvojich funkcií.	
##
##number_of_lists()	
##Funkcia number_of_lists(zoznam) vráti počet zoznamov, ktoré sa nachádzajú v danom vstupnom parametri.
##Napríklad:	
##>>> number_of_lists([1, 'a', 2])	
##1	
##>>> number_of_lists([[], 1, 'a', [3], 2])	
##3	
##>>> number_of_lists(['a', ['dom', [2], 3], [], [[[2]]], 'b'])	
##7	
##>>> number_of_lists([1, '[]', 2])	
##1	
##>>> number_of_lists((1, 2))	
##0	
##
##get_elements()	
##Funkcia get_elements(zoznam) vráti sploštený zoznam prvkov daného zoznamu (v tvare n-tice),
##teda taký, ktorý už neobsahuje žiadne podzoznamy. Funkcia vráti hodnotu v tvare tuple.
##Napríklad:	
##>>> print(get_elements([1, 2, 3, [4, 5], 6, [[[7]]], [], 8]))	
##    (1, 2, 3, 4, 5, 6, 7, 8)	
##>>> print(get_elements(['a', ['dom', [2], 3], [], [[[2]]], 'b']))	
##    ('a', 'dom', 2, 3, 2, 'b')	
##>>> print(get_elements([[], [[[]]], []]))	
##    ()	
##>>> zoz = [[[7]], 8]	
##>>> print(get_elements(zoz))	
##    (7, 8)	
##>>> zoz	
##    [[[7]], 8]	
##Pôvodný zoznam pri tom ostane bez zmeny.	
##
##flat_list()	
##Funkcia flat_list(zoznam) sploští daný vstupný zoznam.
##Na rozdiel od predchádzajúcej funkcie táto nič nevracia, len modifikuje vstupný zoznam.
##Napríklad:	
##>>> zoz = [[[7]], 8]	
##>>> print(flat_list(zoz))	
##    None	
##>>> zoz	
##    [7, 8]	
##>>> p = [1, 2, 3, [4, 5], 6, [[[7]]], [], 8]	
##>>> flat_list(p)	
##>>> p	
##    [1, 2, 3, 4, 5, 6, 7, 8]	
##
##nested_replace()	
##Funkcia nested_replace(zoznam, hodnota1, hodnota2) vráti kópiu pôvodného zoznamu,
##v ktorom budú všetky prvky vstupného zoznamu s hodnotou hodnota1 change_valuesené hodnotou hodnota2.
##Ak sú nejakými prvkami opäť zoznamy, tak bude hodnota1 change_valuesená hodnotou2
##aj v týchto zoznamoch, aj ich podzoznamoch atď.
##Napríklad:	
##>>> zoz = [[[7]], 8]	
##>>> print(nested_replace(zoz, 7, 'a'))	
##    [[['a']], 8]	
##>>> zoz	
##    [[[7]], 8]	
##>>> print(nested_replace([1, 2, 3, [1, 2], 3, [[[1]]], [], 2], 1, 'x'))	
##    ['x', 2, 3, ['x', 2], 3, [[['x']]], [], 2]	
##>>> print(nested_replace([3, [33, [333, [13], 13]], 36], 3, 'q'))	
##    ['q', [33, [333, [13], 13]], 36]	
##>>> print(nested_replace([3, [33, [333, [13], 13]], 36], [13], 'm'))	
##    [3, [33, [333, 'm', 13]], 36]	
##
##change_values()	
##Funkcia change_values(zoznam, hodnota1, hodnota2) change_valuesí v danom zozname zoznam
##všetky prvky s hodnotou hodnota1 hodnotou hodnota2.
##Ak sú nejakými prvkami opäť zoznamy, tak nahrádza aj v týchto zoznamoch,
##aj v ich podzoznamoch atď. Funkcia nič nevracia, len modifikuje vstupný zoznam.
##Napríklad:	
##>>> zoz = [[[7]], 8]	
##>>> print(change_values(zoz, 7, 'a'))	
##    None	
##>>> zoz	
##    [[['a']], 8]	
##>>> p = [1, 2, 3, [1, 2], 3, [[[1]]], [], 2]	
##>>> change_values(p, 1, 'x')	
##>>> p	
##    ['x', 2, 3, ['x', 2], 3, [[['x']]], [], 2]	
##>>> p = [1, 2, 3, [1, 2], 3, [[[1]]], [], 2]	
##>>> change_values(p, 4, 'z')	
##>>> p	
##    [1, 2, 3, [1, 2], 3, [[[1]]], [], 2]	
##>>> p = ['a', ['dom', [2], 3], [], [[[2]]], 'b']	
##>>> change_values(p, 2, 'abc')	
##>>> p	
##    ['a', ['dom', ['abc'], 3], [], [[['abc']]], 'b']	
##Nemeň mená funkcií. Zrejme využiješ rekurziu.	
##
##Tvoj odovzdaný program s menom riesenie.py musí začínať tromi riadkami komentárov:	
### 7. zadanie: zoznamy	
### autor: Janko Hraško	
### datum: 19.11.2021	
##Projekt riesenie.py odovzdaj na úlohový server https://list.fmph.uniba.sk/
##najneskôr do 23:00 26. novembra, kde ho môžeš nechať otestovať.
##Môžeš zaň získať 5 bodov.
#123456789#123456789#123456789#123456789#123456789#123456789#123456789#123#75
                                                                            #
# 7. zadanie: zoznamy	
# autor: Dalibor Sova	
# datum: 4.3.2023


#úvodní a prázdný řádek:                                                  
print('TÝDENÍ PROJEKT 13 LEKCE')                              
print('''
Program obsahuje 5 funkcí pro práci se seznamami:

1) number_of_lists(seznam) - která vrátí počet seznamů v 2D tabulce

2) get_elements(zoznam) - která vrátí n-tici hodnot z 2D tabulce

3) flat_list(zoznam) - která dělá to samé jako get_elements(zoznam)
ale tentokrát nevrací n-tici ale modifikuje vstupní seznam

4) nested_replace(zoznam, hodnota1, hodnota2) - která vrací kopii
původního seznamu s nahrazenými hodnotami

5) change_values(zoznam, hodnota1, hodnota2) - která dělá to samé
jako předchozí funkce, akorát nyní upravuje (modifikuje) původní seznam
''')

print('\n----------------------------------------------------',)
input('''
Zmáčkni [enter] pro zobrazení výsledků volání 1. funkce
number_of_lists() s následujícími hodnotami:

a = number_of_lists([1, 'a', 2])
b = number_of_lists([[], 1, 'a', [3], 2])
c = number_of_lists(['a', ['dom', [2], 3], [], [[[2]]], 'b'])
d = number_of_lists([1, '[]', 2])
e = number_of_lists((1, 2))
''')


def number_of_lists(seznam):                                                #definice rekurzivní funkce - pro výpočet, kolik seznamů obsahuje vstupní seznam
    '''Funkce vrátí počet seznamů, které se nacházejí
ve vstupním parametru.
(Vstupní parametr může, ale i nemusí být seznam)'''                         #(popis funkce)
                                                                            #
    if isinstance(seznam, list):                                                #podmínka - když vstupní hodnota je seznam
        if len(seznam) == 0:                                                        #podmínka - když seznam neobsahuje žádnou položku
            return 1                                                                    #návratová hodnota - vrať hodnotu '1'
        elif isinstance(seznam[0], list):                                           #podmínka - když 1. položka seznamu je seznam
            a = number_of_lists(seznam[0])                                              #proměná + rekurzivní volání funkce - pro první položku seznamu
            b = number_of_lists(seznam[1:])                                             #proměná + rekurzivní volání funkce - pro zbylí seznamem bez první položky
            return a + b                                                                #návratová hodnota - součet hodnot obou předchozích proměných
        else:                                                                       #podmínka - když 1. položka seznamu není seznam
            return number_of_lists(seznam[1:])                                          #návratová hodnota - rekurzivní volání funkce bez první položky
    return 0                                                                    #podmínka + návratová hodnota - když vstupní hodnota není seznam, vrať hodnotu '0'
                                                                            #

a = number_of_lists([1, 'a', 2])                                            #proměnná + volání rekurzivní funkce
b = number_of_lists([[], 1, 'a', [3], 2])                                   #proměnná + volání rekurzivní funkce
c = number_of_lists(['a', ['dom', [2], 3], [], [[[2]]], 'b'])               #proměnná + volání rekurzivní funkce
d = number_of_lists([1, '[]', 2])                                           #proměnná + volání rekurzivní funkce
e = number_of_lists((1, 2))                                                 #proměnná + volání rekurzivní funkce


print('a = ', a)                                                            #tisk výsledku
print('b = ', b)                                                            #tisk výsledku
print('c = ', c)                                                            #tisk výsledku
print('d = ', d)                                                            #tisk výsledku
print('e = ', e)                                                            #tisk výsledku


print('\n----------------------------------------------------',)
input('''
Zmáčkni [enter] pro zobrazení výsledků volání 2. funkce
get_elements() s následujícími hodnotami:

f = get_elements([1, 2, 3, [4, 5], 6, [[[7]]], [], 8])
g = get_elements(['a', ['dom', [2], 3], [], [[[2]]], 'b'])
h = get_elements([[], [[[]]], []])
i = get_elements([[[7]], 8])
''')


def get_elements(seznam):                                                   #definice rekurzivní funkce - vypočítá a vrátí n-tici obsahující prvky seznamu a všech jeho podseznamů
    '''Funkce vytvoří a vrátí ze seznamu obsahující
podseznamy, n-tici se všemi prvky'''                                        #(popis funkce)
                                                                            #
    if len(seznam) == 0:                                                    #podmínka - když seznam neobsahuje žádnou položku
        return ()                                                               #návratová hodnota - vrať prázdnou n-tici
    elif len(seznam) == 1:                                                  #podmínka - když seznam obsahuje 1 položku
        if isinstance(seznam[0], list):                                         #podmínka - když je položka seznam 
            return get_elements(seznam[0])                                          #návratová hodnota - rekurzivní volání funkce s položkou
        return (seznam[0],)                                                     #podmínka + návratová hodnota - když položka není seznam, vrať n-tici s položkou
    else:                                                                   #podmínka - když seznam obsahuje více položek
        a = get_elements([seznam[0]])                                           #proměná + rekurzivní volání funkce - pro první položku seznamu
        b = get_elements(seznam[1:])                                            #proměná + rekurzivní volání funkce - pro zbylí seznamem bez první položky
        return a + b                                                            #návratová hodnota - součet hodnot obou předchozích proměných
                                                                            #

f = get_elements([1, 2, 3, [4, 5], 6, [[[7]]], [], 8])                      #proměnná + volání rekurzivní funkce
g = get_elements(['a', ['dom', [2], 3], [], [[[2]]], 'b'])                  #proměnná + volání rekurzivní funkce
h = get_elements([[], [[[]]], []])                                          #proměnná + volání rekurzivní funkce
i = get_elements([[[7]], 8])                                                #proměnná + volání rekurzivní funkce


print('f = ', f)                                                            #tisk výsledku
print('g = ', g)                                                            #tisk výsledku
print('h = ', h)                                                            #tisk výsledku
print('i = ', i)                                                            #tisk výsledku


print('\n----------------------------------------------------',)
input('''
Zmáčkni [enter] pro zobrazení výsledků volání 3. funkce
flat_list() s následujícími hodnotami:

j = flat_list([[[7]], 8]
k = flat_list([1, 2, 3, [4, 5], 6, [[[7]]], [], 8])
''')


def flat_list(seznam):                                                      #definice rekurzivní funkce - měnící seznam obsahující podseznami na seznam obsahující všechny prvky v jednom seznamu
    '''Funkce mění seznam obsahující i podseznamy
na seznam obsahující všechny prvky
v jednom základním seznamu'''                                               #(popis funkce)
                                                                            #
    for i in range(len(seznam)):                                            #cyklus - dle počtu položek seznamu
        if not isinstance(seznam[0], list):                                     #podmínka - pokud první položka seznamu není seznam
            seznam.append(seznam.pop(0))                                            #změna - odeber položku a vlož ji na konec seznamu
        else:                                                                   #podmínka - pokud první položka seznamu je seznam
            novy_sez = seznam.pop(0)                                                #proměnná + změna - pro nový seznam vytvořený odebráním položka (seznamu) z aktuálního seznamu
            flat_list(novy_sez)                                                     #rekurzivní volání funkce - s novým seznamem
            seznam.extend(novy_sez)                                                 #přiřazení zpracovaného seznamu (položky) na konec původního seznamu
                                                                            #
j = [[[7]], 8]
flat_list(j)                                                                #proměnná - pro seznam hodnot + volání rekurzivní funkce - dle hodnot zadání a tisk návratové hodnoty: None
print('j = ', j)                                                            #tisk výsledku
k = [1, 2, 3, [4, 5], 6, [[[7]]], [], 8]
flat_list(k)                                                                #proměnná - pro seznam hodnot + volání rekurzivní funkce - dle hodnot zadání a tisk návratové hodnoty: None
print('k = ', k)                                                            #tisk výsledku


print('\n----------------------------------------------------',)
input('''
Zmáčkni [enter] pro zobrazení výsledků volání 4. funkce
nested_replace() s následujícími hodnotami:

l = [[[7]], 8]  // změna hodnoty "7" za "a"
m = [1, 2, 3, [1, 2], 3, [[[1]]], [], 2]  // změna hodnoty "1" za "x"
n = [3, [33, [333, [13], 13]], 36]  // změna hodnoty "3" za "q" 
o = [3, [33, [333, [13], 13]], 36]  // změna hodnoty "[13]" za "m"
''')


def nested_replace(zoznam, hodnota1, hodnota2):                             #definice rekurzivní funkce - navracející kopii původního seznamu s vyměněnými hodnotami 
    '''Funkce vrátí kopii původního seznamu
v kterém budou všechny prvky s hodnotou 1
nahrazeny prvkem s hodnotou 2'''                                            #(popis funkce)
                                                                            #
    novy_sez = zoznam[:]                                                    #proměnná - pro nový seznam vytvořený kopií starého seznamu
    for ix, polozka in enumerate(novy_sez):                                 #cyklus - dle indexu a položky nového seznamu
        if polozka == hodnota1:                                                 #podmínka - pokud se položka shoduje s hodnotou 1
            novy_sez[ix] = hodnota2                                                 #změna - nahraď položku hodnotou 2
        else:                                                                   #podmínka - pokud se položka neshoduje s hodnotou 1
            if isinstance(polozka, list):                                           #podmínka - pokud je položka seznamem
                novy_sez[ix] = nested_replace(polozka, hodnota1, hodnota2)              #rekurzivní volání funkce - se seznamem položky
    return novy_sez                                                         #návratová hodnota - upravený nově vytvořený seznam
                                                                            #
l = [[[7]], 8]                                                              #proměnná - pro seznam hodnot
print('nová kopie seznamu "l" = ', nested_replace(l, 7, 'a'))                   #tisk - návratová hodnota funkce
print('pro kontrolu původní seznam "l": ', l)                                   #tisk - původního (nezměněného) seznamu
print()                                                                     #tisk - prázdný řádek

m = [1, 2, 3, [1, 2], 3, [[[1]]], [], 2]                                    #proměnná - pro seznam hodnot
print('nová kopie seznamu "m" = ', nested_replace(m, 1, 'x'))                   #tisk - návratová hodnota funkce
print('pro kontrolu původní seznam"m": ', m)                                   #tisk - původního (nezměněného) seznamu
print()                                                                     #tisk - prázdný řádek

n = [3, [33, [333, [13], 13]], 36]                                           #proměnná - pro seznam hodnot
print('nová kopie seznamu "n" = ', nested_replace(n, 3, 'q'))                   #tisk - návratová hodnota funkce
print('pro kontrolu původní seznam"n": ', n)                                   #tisk - původního (nezměněného) seznamu
print()                                                                     #tisk - prázdný řádek

o = [3, [33, [333, [13], 13]], 36]                                          #proměnná - pro seznam hodnot
print('nová kopie seznamu "o" = ', nested_replace([3, [33, [333, [13], 13]], 36], [13], 'm')) #tisk - návratová hodnota funkce        
print('pro kontrolu původní seznam "o": ', o)                                   #tisk - původního (nezměněného) seznamu
print()                                                                     #tisk - prázdný řádek


print('\n----------------------------------------------------',)
input('''
Zmáčkni [enter] pro zobrazení výsledků volání 5. funkce
change_values() s následujícími hodnotami:

p = [[[7]], 8] // změna hodnoty "1" za "x"
q = [1, 2, 3, [1, 2], 3, [[[1]]], [], 2] // změna hodnoty "1" za "x" 
r = r = [1, 2, 3, [1, 2], 3, [[[1]]], [], 2] // změna hodnoty "4" za "z"
s = ['a', ['dom', [2], 3], [], [[[2]]], 'b'] // změna hodnoty "2" za "abc"
''')


def change_values(zoznam, hodnota1, hodnota2):                              #definice rekurzivní funkce - měnící hodnoty seznamu
    '''Funkce modifikuje původní seznam,
kdy všechny prvky odpovídající
1. hodnotě, nahrazuje hodnotou 2.'''                                        #(popis funkce)
                                                                            #
    for ix, polozka in enumerate(zoznam):                                   #cyklus - dle indexu a položky seznamu
        if polozka == hodnota1:                                                 #podmínka - pokud se položka shoduje s hodnotou 1
            zoznam[ix] = hodnota2                                                   #změna - nahraď položku hodnotou 2
        else:                                                                   #podmínka - pokud se položka neshoduje s hodnotou 1
            if isinstance(polozka, list):                                           #podmínka - pokud je položka seznamem
                change_values(polozka, hodnota1, hodnota2)                              #rekurzivní volání funkce - se seznamem položky
                                                                            #
p = [[[7]], 8]                                                              #proměnná - pro seznam hodnot
change_values(p, 7, 'a')                                                    #volání rekurzivní funkce - návratová hodnota funkce: None
print('změněný seznam "p": ', p)                                            #tisk 

q = [1, 2, 3, [1, 2], 3, [[[1]]], [], 2]                                    #proměnná - pro seznam hodnot
change_values(q, 1, 'x')                                                    #volání rekurzivní funkce - návratová hodnota funkce: None
print('změněný seznam "q": ', q)                                            #tisk

r = [1, 2, 3, [1, 2], 3, [[[1]]], [], 2]                                    #proměnná - pro seznam hodnot
change_values(r, 4, 'z')                                                    #volání rekurzivní funkce - návratová hodnota funkce: None
print('změněný seznam "r": ', r)                                            #tisk

s = ['a', ['dom', [2], 3], [], [[[2]]], 'b']                                #proměnná - pro seznam hodnot
change_values(s, 2, 'abc')                                                  #volání rekurzivní funkce - návratová hodnota funkce: None
print('změněný seznam "s": ', s)                                            #tisk


print('\n----------------------------------------------------',)
input('''
Zmáčkni [enter] pro ukončení programu
''')














