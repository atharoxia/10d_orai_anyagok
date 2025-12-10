f = open("03_000.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

szamok = []
for i in range(len(sorok)):
    szamok.append(int(sorok[i]))

print(szamok)

print("1. feladat: ")
van = False
for i in range(len(szamok)):
    if szamok[i] % 100 == 0:
        van = True
        break

if van == True:
    print("Van közte 100-zal osztható.")
else:
    print("Nincs közte 100-zal osztható.")

print("2. feladat:")
for i in reversed(range(len(szamok))):
    if szamok[i] % 7 == 0:
        print(f"Az utolsó 7-tel osztható indexe {i}")
        break

print("3. feladat:")
for i in range(len(szamok)):
    if szamok[i] % 19 == 0:
        print(f"Az első 19-cel osztható indexe {i}")
        break

print("4. feladat:")
osszeg = 0
for i in range(len(szamok)):
    osszeg += szamok[i]

atlag = osszeg / len(szamok)
negyzet = atlag * atlag
print(f"A számok átlagának négyzete {negyzet}")

print("6. feladat:")
db = 0
for i in range(len(szamok)):
    if szamok[i] < 0:
        db += 1
print(f"{db} negatív szám van.")

print("10. feladat:")
min = szamok[0]
for i in range(len(szamok)):
    if szamok[i] < min:
        min = szamok[i]

print(f"A legkisebb szám fele {min / 2}")

print("11. feladat:")
negativ = open("negativ.txt", "w", encoding="utf-8")
pozitiv = open("pozitiv.txt", "w", encoding="utf-8")

for i in range(len(szamok)):
    if szamok[i] < 0:
        print(szamok[i], file=negativ)
    else:
        print(szamok[i], file=pozitiv)

negativ.close()
pozitiv.close()

