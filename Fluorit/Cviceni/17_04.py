##Napíš funkciu zoznam(retazec),
##ktorá zo znakového reťazca retazec vyrobí zoznam čísel.
##Predpokladaj, že reťazec začína a končí znakmi '[' a ']'
##a prvky zoznamu sú oddelené znakmi ','.
##Daj pozor, aby sa celé čísla v reťazci prerobili na celé,
##desatinné na desatinné a nečíselné prvky ignoruj.
##Napríklad:
##>>> z = zoznam('[0, 1., 2, 3.14]')
##>>> z
##    [0, 1.0, 2, 3.14]
##>>> zoznam('[0, -.1, None, +2, [7], a5, -3.14, "8"]')
##    [0, -0.1, 2, -3.14]


def seznam(retezec):
    seznam = []
    polozky = retezec[1:-1].split(',')
    for polozka in polozky:
        if '.' in polozka:
            try:
                seznam.append(float(polozka))
            except:
                pass
        else:
            try:
                seznam.append(int(polozka))
            except:
                pass
    return seznam
        




z = seznam('[0, 1., 2, 3.14]')
print(z)
z = seznam('[0, -.1, None, +2, [7], a5, -3.14, "8"]')
print(z)
