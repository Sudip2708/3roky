##Napíš funkciu cele(hodnota),
##ktorá pomocou int prevedie danú hodnotu na celé číslo.
##Ak sa to nedá, funkcia vráti 0.
##Nepoužívaj try-except bez vymenovaných typov chýb.
##Malo by fungovať, napríklad:
##>>> cele(12.3)
##    12
##>>> cele('13')
##    13
##>>> cele([])
##    0
##>>> cele('12.3')
##    0


def cele(hodnota):
    try:
        return int(hodnota)
    except (ValueError, TypeError):
        return 0

print(cele(12.3))
print(cele('13'))
print(cele([]))
print(cele('12.3'))

