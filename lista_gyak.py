import random
szamok = []
for i in range(50):
    szamok.append(random.randint(-60, 100))

print(szamok)

print("1. feladat")
szorzat = 1
for i in range(len(szamok)):
    szorzat *= szamok[i]
print(f"A számok szorzata: {szorzat}")

print("2. feladat")
for i in reversed(range(len(szamok))):
    if szamok[i] % 5 == 0 or szamok[i] % 7 == 0:
        print(i)
        break

print("3. feladat")
for i in range(len(szamok)):
    if szamok[i] % 3 == 0 and szamok[i] % 7 == 0:
        print(i)
        break

print("4. feladat")
mindnegativ = True
for i in range(len(szamok)):
    if szamok[i] >= 0:
        mindnegativ = False
        break

if mindnegativ == True:
    print("Minden szám negatív")
else:
    print("Van közte pozitív")

print("6. feladat")
db = 0
for i in range(len(szamok)):
    if szamok[i] % 18 == 0:
        db += 1
print(db)

print("7. feladat")
min = szamok[0]
mini = 0

for i in range(len(szamok)):
    if szamok[i] < min:
        min = szamok[i]
        mini = i
print(mini)