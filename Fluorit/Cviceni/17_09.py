##Napíš funkciu sustavy(retazec),
##ktorá sa pokúsi daný reťazec previesť na číslo v rôznych číselných sústavách.
##Využi to, že štandardná funkcia int()
##môže byť zavolaná aj s druhým parametrom - číselnou sústavou,
##napríklad int('ff', 16) vráti 255, t.j. 'ff' je v 16-ovej sústave číslo 255.
##Funkcia sustavy() vráti 17-prvkový zoznam,
##pričom i-ty prvok zoznamu obsahuje prevod daného reťazca na číslo v i-sústave.
##Ak sa to pre nejakú sústavu urobiť nedá,
##prvok zoznamu na danom mieste bude mať hodnotu None.
##Otestuj štandardnú funkciu int, napríklad:
##>>> int('1101')
##    1101
##>>> int('1101', 2)      # dvojkova sustava
##    13
##>>> int('1101', 3)
##    37
##>>> int('1101', 16)
##    4353
##>>> int('3a')
##    ...
##    ValueError: invalid literal for int() with base 10: '3a'
##>>> int('3a', 11)
##    43
##>>> int('3a', 16)
##    58
##Napríklad:
##>>> sustavy('11')
##    [11, None, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
##>>> sustavy('1a1')
##    [None, None, None, None, None, None, None, None, None, None, None, 232, 265, 300, 337, 376, 417]
##>>> sustavy('FF')
##    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 255]
##>>> sustavy('x')
##    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]


def soustavy(retezec):
    seznam = []
    for i in range(17):
        try:
            seznam.append(int(retezec, i))
        except:
            seznam.append(None)
    return seznam

print(soustavy('11'))
print(soustavy('1a1'))
print(soustavy('FF'))
print(soustavy('x'))


