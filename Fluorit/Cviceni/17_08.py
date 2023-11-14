##Napíš funkciu rgb(r, g, b),
##ktorá z troch celých čísel vyrobí znakový reťazec.
##ktorý reprezentuje príslušnú farbu vo formáte '#rrggbb'.
##Funkcia pomocou troch príkazov assert skontroluje,
##či sú všetky tri parametre v poriadku.
##Napríklad:
##>>> rgb(100, 150, 20.0)
##    ...
##    AssertionError: chybny treti parameter b
##>>> rgb(100, 350, 20.0)
##    ...
##    AssertionError: chybny druhy parameter g
##>>> rgb('100', 350, 20.0)
##    ...
##    AssertionError: chybny prvy parameter r
##>>> rgb(100, 150, 200)
##    '#6496c8'



def rgb(r, g, b):
    assert isinstance(r, int), 'chybný první parametr'
    assert r < 256, 'chybný první parametr'
    assert isinstance(g, int), 'chybný druhý parametr'
    assert g < 256, 'chybný druhý parametr'
    assert isinstance(b, int), 'chybný třetí parametr'
    assert b < 256, 'chybný třetí parametr'
    return f'#{r:02x}{g:02x}{b:02x}'
    

print(rgb(100, 150, 200))
