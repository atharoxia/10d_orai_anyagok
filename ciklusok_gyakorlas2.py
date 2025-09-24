#Generáljuk le egy hét hőmérsékleteit véletlen számokkal (-5, 10)
#Hány olyan nap volt, amikor fagyott?

fagy = 0
import random
for i in range(7):
    hom = random.randint(-5, 10)
    print(f"{hom}, ", end="")
    if hom < 0:
        fagy += 1
print(f"{fagy} napon fagyott.")

#Olvassuk be egy osztály tanulóinak magasságát, amíg 0-t nem írnak be
#Írjuk ki, hogy hányadik tanuló a legalacsonyabb, és hány cm!

magas = int(input("Írd be a magasságot: "))
min = magas
ssz = 1
hanyadik = ssz
while magas != 0:
    magas = int(input("Írd be a magasságot: "))
    ssz += 1
    if magas < min and magas != 0:
        min = magas
        hanyadik = ssz

print(f"A legalacsonyabb a {hanyadik}, {min} cm magas.")


#Olvassuk be egy dolgozat pontszámait, amíg -1-et nem írnak be!
#Minden pontszámra írjuk, ki hányas a dolgozat!
#Végül írjuk ki a jegyek átlagát!

osszeg = 0
db = 0
pont = int(input("Következő pontszám: "))
while pont != -1:
    if pont < 40:
        print("1-es lett!")
        osszeg += 1
    elif pont >= 40 and pont < 50:
        print("2-es lett!")
        osszeg += 2
    elif pont >= 50 and pont < 60:
        print("3-es lett!")
        osszeg += 3
    elif pont >= 60 and pont < 80:
        print("4-es lett!")
        osszeg += 4
    else:
        print("5-es lett!")
        osszeg += 5
    pont = int(input("Következő pontszám: "))
    db += 1

atlag = osszeg / db
print(f"A jegyek átlaga {atlag}")