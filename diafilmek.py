f = open("filmek.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

class diafilm:
    def __init__(self, cim, ev, kocka, szines):
        self.cim = cim
        self.ev = int(ev)
        self.kocka = int(kocka)
        self.szines = int(szines)

diafilmek = []
for i in range(len(sorok)):
    darabok = sorok[i].strip().split(";")
    d = diafilm(darabok[0], darabok[1], darabok[2], darabok[3])
    diafilmek.append(d)

print(f"3.2. feladat: A fájlban {len(diafilmek)} diafilm adatai vannak.")

legkorabbi = diafilmek[0]

for d in diafilmek:
    if d.ev < legkorabbi.ev:
        legkorabbi = d

print("A legrégebbi diafilm:")
print(f"\t{legkorabbi.cim}")
print(f"\t{legkorabbi.ev}")
print(f"\t{legkorabbi.kocka}")


evszam = int(input("Írjon be egy évszámot: "))
van = False
for d in diafilmek:
    if d.ev == evszam:
        print(d.cim)
        van = True

if van == False:
    print("Nem található az évszám.")

osszeg = 0
db = 0

for d in diafilmek:
    if d.szines == -1:
        osszeg += d.kocka
        db += 1

atlag = round(osszeg / db, 2)
print(f"A szines diafilmek átlag {atlag} hosszúak.")

