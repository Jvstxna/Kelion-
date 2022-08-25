import random
x = random.randint(1, 6)
print('Pasirinktas skaičius - ', x)

# Austerlitz maršrutas
if x == 1 or x == 2:
    print('Pasirinktas maršrutas į Austerlitz mūšio vietą')
    x_aus = random.randint(10, 20)
    print('Turime pinigų ekskursijai - ', x_aus)

    # Perkame paslaugas Austerlitz mūšio vietoje
    if x_aus >= 3:
        print('Nusipirkome bilietą į muziejų')
        x_aus -= 3
        print('Likutis po bilieto pirkimo yra: ', x_aus)

    if x_aus >= 2:
        print('Nusipirkome kavinėje maisto ir gėrimų')
        x_aus -= 2
        print('Likutis po maisto ir gėrimų pirkimo yra: ', x_aus)

    if x_aus >= 3:
        print('Nusipirkome suvenyrų draugams')
        x_aus -= 3
        print('Likutis po suvenyrų pirkimo draugams yra: ', x_aus)
    else:
        print('Jei nepakaks pinigų, bėgu pas draugą skolintis')

else:
    print('Žaidimo pabaiga')

# Vaterlo maršrutas
if x == 3 or x == 4:
    print('Pasirinktas maršrutas į Vaterlo mūšio vietą')
    x_vat = random.randint(10, 20)
    print('Turime pinigų ekskursijai - ', x_vat)

    # Perkame paslaugas Austerlitz mūšio vietoje
    if x_vat >= 3:
        print('Nusipirkome bilietą į muziejų')
        x_vat -= 3
        print('Likutis po bilieto pirkimo yra: ', x_vat)

    if x_vat >= 2:
        print('Nusipirkome kavinėje maisto ir gėrimų')
        x_vat -= 2
        print('Likutis po maisto ir gėrimų pirkimo yra: ', x_vat)

    if x_vat >= 3:
        print('Nusipirkome suvenyrų draugams')
        x_vat -= 3
        print('Likutis po suvenyrų pirkimo draugams yra: ', x_vat)
    else:
        print('Jei nepakaks pinigų, bėgu pas draugą skolintis')

else:
    print('Žaidimo pabaiga')


# Borodino maršrutas
if x == 5 or x == 6:
    print('Pasirinktas maršrutas į Borodino mūšio vietą')
    x_bor = random.randint(10, 20)
    print('Turime pinigų ekskursijai - ', x_bor)

    # Perkame paslaugas Austerlitz mūšio vietoje
    if x_bor >= 3:
        print('Nusipirkome bilietą į muziejų')
        x_bor -= 3
        print('Likutis po bilieto pirkimo yra: ', x_bor)

    if x_bor >= 2:
        print('Nusipirkome kavinėje maisto ir gėrimų')
        x_bor -= 2
        print('Likutis po maisto ir gėrimų pirkimo yra: ', x_bor)

    if x_bor >= 3:
        print('Nusipirkome suvenyrų draugams')
        x_bor -= 3
        print('Likutis po suvenyrų pirkimo draugams yra: ', x_bor)
    else:
        print('Jei nepakaks pinigų, bėgu pas draugą skolintis')

else:
    print('Žaidimo pabaiga')
