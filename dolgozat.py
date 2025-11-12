
import random
szamok = []
for i in range(70):
    szamok.append(random.randint(-40,50))

print(szamok)

print("1. Feladat")
for i in range(len(szamok)):
    if szamok[i] % 5 == 0 and szamok[i] % 4 == 0:
        print(szamok[i])
        break

print("2. Feladat")
Igaz = True
sor = 0
for i in range(len(szamok)):
    if -10 > szamok[i] > -30:
        sor = i
        Igaz = False
        break

if Igaz == False:
    print(f"Van -10-nél kisebb, de -30-nál nagyobb szám a sorozatban, Az első ilyen a {sor}.")
else:
    print("Nincs -10-nél kisebb, de -30-nál nagyobb szám a sorozatban")

print("3. Feladat")
harmincasok = 0
for i in range(len(szamok)):
    if szamok[i] > 30:
        harmincasok += 1
print(f"Ennyi 30-nál nagyobb szám van a sorozatban: {harmincasok}")

print("4. Feladat")
min = 70
mini = 0
for i in range(len(szamok)):
    if szamok[i] < min and szamok[i] >= 0:
        min = szamok[i]
        mini = i
print(f"A legkisebb pozitív szám indexe: {mini}")

print("5. Feladat")
Van = True
db = 0
for i in range(len(szamok)):
    if szamok[i-1] > szamok[i] and szamok[i+1] > szamok[i]:
        db = i
        Van = False
        break

if Van == False:
    print(f"Van olyan szám, amely kisebb az előtte és az utána álló számnál is, Az első ilyen a: {db}.")
else:
    print("Nincs ilyen szám, amely kisebb az előtte és az utána álló számnál is")
