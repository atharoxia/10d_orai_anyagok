
f = open("be.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

szamok = []
for i in range(len(sorok)):
    szamok.append(int(sorok[i]))

print(szamok)


print("1. feladat")
hszam = False
for i in range(len(szamok)):
    if szamok[i] % 21 == 0:
        hszam = True
        break

if hszam == True:
    print("Van a sorozatban 21-gyel osztható szám")
else:
    print("Nincs a sorozatban 21-gyel osztható szám")


print("2. feladat")
for i in range(len(szamok)):
    if szamok[i] % 6 == 0 and szamok[i] % 13 == 0:
        print(f"Az első 6-tal és 13-mal osztható szám indexe: {i}")
        break


print("3. feladat")
osszeg = 0
for i in range(len(szamok)):
    osszeg += szamok[i]

atlag = osszeg / len(szamok)
print(f"A sorozatban található számok átlagának az ötszöröse: {atlag*5}")


print("4. feladat")
min = 1000
for i in range(len(szamok)):
    if szamok[i] <= min and szamok[i] > 20:
        min = szamok[i]

print(f"A legkisebb szám a 20-nál nagyobbak közül a: {min}")


print("5. feladat")
kii = open("kii.txt", "w", encoding="utf-8")
for i in range(len(szamok)):
    if szamok[i] < 25 and szamok[i] > -25:
        print(szamok[i], file=kii)

kii.close()

