##Atribúty meno, typ a zvuk prerob na property:
##    o najprv ich všetky premenuj tak, aby začínali
##    znakom podčiarkovník
##    o v triede Zviera pre všetky z nich zadefinuj
##    zodpovedajúci getter v tvare daj_atribút
##    o atribúty meno a zvuk budú mať aj svoj setter:
##         metóda zmen_meno nastaví prvé písmeno mena na veľké
##        a ostatné na malé
##         metóda zmen_zvuk najprv zistí, či nový zvuk obsahuje znak '‐'
##        a ak nie, tak zvuk zreťazí za seba a vloží znak '‐',
##
##Napríklad:
##>>> z3.zmen_zvuk('vrr')
##>>> z3.daj_zvuk()
##'vrr‐vrr'
##>>> z4.zmen_zvuk('GA‐GA')
##>>> z4.daj_zvuk()
##'GA‐GA'
##
##    o vyrob meno, typ a zvuk ako property, pričom typ nebude mať
##    definovaný setter (zapíšeš typ = property(daj_typ))
##
##Otestuj, napríklad:
##>>> z3.zvuk = 'vrr'
##>>> z4.meno = 'grETA'
##>>> z2.typ = 'cat'


#úvodní a prázdný řádek:                                                  
print('TŘÍDA ZVIERA - POUŽITÍ PROPERTY')                              
print('''
Následující program obsahuje tyto třídy:
class Zviera; class Pes(Zviera); class Macka(Zviera); class Kacka(Zviera):

Přičemž třída Zviera je základní a ostatní třídy jsou odvozené
a obsahují pouze informaci o typu a zvuk.
V tomto programu jde o to, vyzkoušet funkci property,
která zjednodušuje zápis při výpisu a změně (nejen) soukromý satributů.

Program má vstupní zadání:
z1 = Pes('dunčo')
z2 = Macka('mica')
z3 = Pes('bono')
z4 = Kacka('gréta')
''')
input('''>> Zmáčkni [enter] pro výpis instancí <<
''')


#definice základní třídy:
class Zviera:
    def __init__(self, meno):                   #nastavení inicializace - povynný údaj - Jméno
        self._meno = meno.capitalize()              #změna jména na formát první velké písmeno, ostatní malé, a přiřazení do soukromého atributu self._meno

    def __str__(self):                          #nastavení textového popisu
        return f'zviera {self.typ} má meno {self.meno} a robí {self.zvuk}'

    def get_meno(self):                         #nastavení getter pro jméno
        return self._meno

    def get_typ(self):                          #nastavení getter pro typ
        return self._typ
    
    def get_zvuk(self):                         #nastavení getter pro zvuk
        return self._zvuk

    def set_meno(self, meno):                   #nastavení setter pro jméno
        Zviera.__init__(self, meno)                 #volání __init__

    def set_zvuk(self, zvuk):                   #nastavení setter pro zvuk
        if '-' not in zvuk:                         #kontrola, zda řetězes obsahuje znak '_'
            zvuk += f'-{zvuk}'                          #pokud ne, znak se vloží a zvuk se ještě jednou zopakuje
        self._zvuk = zvuk                           #přiřazení zvuku

    meno = property(get_meno, set_meno)         #definice property pro jméno
    zvuk = property(get_zvuk, set_zvuk)         #definice property pro zvuk
    typ = property(get_typ)                     #definice property pro typ

        
#definice odvozených tříd:        
class Pes(Zviera):
    _typ = 'pes'
    _zvuk = 'haf-haf'

class Macka(Zviera):
    _typ = 'mačka'
    _zvuk = 'mnau-mnau'

class Kacka(Zviera):
    _typ = 'kačka'
    _zvuk = 'ga-ga'


#definice instancí:
z1 = Pes('dunčo')
z2 = Macka('mica')
z3 = Pes('bono')
z4 = Kacka('gréta')

#kontrola nastavení instancí
for z in z1, z2, z3, z4:
    print(z)


###testování setteru pro nastavení zvuku:
##z3.set_zvuk('vrr')
##z4.set_zvuk('GA-GA')
##
###kontrola nastavení setteru pro zvuku:
##print(z3.get_zvuk())
##print(z4.get_zvuk())
##
##
###testování nastavení property setteru:
##z3.zvuk = 'vrr'
##z4.meno = 'grETA'
##
###kontrola nastavení property setteru:
##print(z3.zvuk)
##print(z4.meno)
##print(z2.typ)


input('''
Nyní následují tyto příkazy, měnící atributy daných instancí:

z3.zvuk = 'vrr'
z4.zvuk = 'GA-GA'
z4.meno = 'grEeTA'

>> Zmáčkni [enter] pro nový výpis instancí <<
''')

#nastavení atributů:
z3.zvuk = 'vrr'
z4.zvuk = 'GA-GA'
z4.meno = 'grEeTA'

#kontrola nastavení instancí
for z in z1, z2, z3, z4:
    print(z)


input('''
>> zmáčkni [enter] pro ukončení programu <<
''')


###definice základní třídy se skrácenou formou property:
##class Zviera:
##    def __init__(self, meno):                   #nastavení inicializace - povynný údaj - Jméno
##        self._meno = meno.capitalize()              #změna jména na formát první velké písmeno, ostatní malé, a přiřazení do soukromého atributu self._meno
##
##    def __str__(self):                          #nastavení textového popisu
##        return f'zviera {self.typ} má meno {self.meno} a robí {self.zvuk}'
##
##    @property
##    def meno(self):                         #nastavení getter pro jméno
##        return self._meno
##
##    @property
##    def typ(self):                          #nastavení getter pro typ
##        return self._typ
##
##    @property
##    def zvuk(self):                         #nastavení getter pro zvuk
##        return self._zvuk
##
##    @meno.setter
##    def meno(self, meno):                   #nastavení setter pro jméno
##        Zviera.__init__(self, meno)                 #volání __init__
##
##    @zvuk.setter
##    def zvuk(self, zvuk):                   #nastavení setter pro zvuk
##        print(zvuk)
##        if '-' not in zvuk:                         #kontrola, zda řetězes obsahuje znak '_'
##            zvuk += f'-{zvuk}'                          #pokud ne, znak se vloží a zvuk se ještě jednou zopakuje
##        self._zvuk = zvuk                           #přiřazení zvuku
##
