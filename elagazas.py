#Olvassunk be két számot, és írjuk ki, hogy melyik a nagyobb:
szam1 = int(input("Egyik szám: "))
szam2 = int(input("Másik szám: "))

if szam1 > szam2:
    print("Az első szám a nagyobb.")
elif szam2 > szam1:
    print("A második szám a nagyobb.")
else:
    print("A két szám egyenlő.")

#Egy beolvasott számról írjuk, ki hogy pozitív vagy negatív:
szam = int(input("Írjon be egy számot:"))
if szam > 0:
    print("A szám pozitív.")
elif szam < 0:
    print("A szám negatív.")
else:
    print("A szám a nulla.")

#Olvassuk be egy háromszög három oldalának hosszát, dönstük el, hogy a háromszög szerkeszthető-e!
a = int(input("a oldal: "))
b = int(input("b oldal: "))
c = int(input("c oldal: "))

if a + b > c and a + c > b and b + c > a:
    print("A háromszög szerkeszthető.")
else:
    print("A háromszög nem szerkeszthető.")