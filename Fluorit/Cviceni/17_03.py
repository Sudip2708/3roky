##Napíš funkciu desatinne(retazec),
##ktorá zistí, či je daný reťazec desatinným číslom.
##Funkcia vráti True alebo False.
##Napríklad:
##>>> desatinne('123')
##    True
##>>> desatinne('  22.7 ')
##    True
##>>> desatinne('22/7')
##    False


def desetina(retezec):
    try:
        float(retezec.strip())
        return True
    except:
        return False



print(desetina('123'))
print(desetina('  22.7 '))
print(desetina('22/7'))
