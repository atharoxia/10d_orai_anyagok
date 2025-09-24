#Olvassunk be számokat, amíg 0-t nem írnak be!
#Írjuk ki a beírt számok összegét!

szam = int(input("Írjon be egy számot: "))
osszeg = 0
while szam != 0:
    osszeg += szam  #osszeg = osszeg + szam
    szam = int(input("Írjon be egy számot: "))
print(f"A számok összege {osszeg}")

#Generáljunk 100 db 1 és 50 közötti véletlen számot!
#Írjuk ki, hogy hány db páros szám volt közte!

import random

db = 0
for i in range(100):
    szam = random.randint(1, 50)
    print(szam)
    if szam % 2 == 0:
        db += 1
print(f"A számok között {db} páros volt.")

#Olvassuk be egy osztály tagjaiank lábméretét!
#A beolvasás végét -1 jelezze.
#Írjuk ki, hogy mennyi a legnagyobb, és hogy hányadik volt a sorban!

meret = int(input("Írja be a lábméretét: "))
max = meret  #A legnagyobb lábméret
hanyadik = 1 #Hányadik a legnagyobb
ssz = 1      #Változó a sorszámozáshoz
while meret != -1:
    meret = int(input("Írja be a lábméretét: "))
    ssz += 1
    if meret > max:
        max = meret
        hanyadik = ssz

print(f"A legnagyobb láb {max}-as, a {hanyadik}-ik volt a sorban.")