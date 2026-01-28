#Írjunk függvényt, ami visszadja, hogy egy szám negavtív vagy pozitív

def poznev(szam):
    if szam >= 0:
        return "pozitiv"
    else:
        return "negativ"


szam = int(input("Írjon be egy számot: "))
if poznev(szam) == "pozitiv":
    print("A szám pozitív")
else:
    print("A szám negatív")

print(poznev(6))

#Abszolútérték függvény
def abszolut(szam):
    if szam >= 0:
        return szam
    else:
        return -szam

import random
for i in range(100):
    vel = random.randint(-50, 50)
    print(abszolut(vel))

#Írjunk függvényt, amely két számról eldönti, hogy melyik a nagyobb
#Igaz értékkel térjen vissza, ha az első, hamissal, ha a második

def kisnagy(a, b):
    if a >= b:
        return True
    else:
        return False

egyik = int(input("Egyik szám: "))
masik = int(input("Másik szám: "))

if kisnagy(egyik, masik):
    print("Az első szám a nagyobb")
else:
    print("A második szám a nagyobb")

#A függvény egy listából szedje ki a párosakat és adja vissza

def parosok(szamok):
    paros = []
    for i in range(len(szamok)):
        if szamok[i] % 2 == 0:
            paros.append(szamok[i])
    return paros

teszt = []
for i in range(50):
    teszt.append(random.randint(1, 100))

print(teszt)
print(parosok(teszt))

