f = open("konyvek.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

class konyv:
    def __init__(self, nev, szulEv, halEv, nemz, cim, hely):
        self.nev = nev
        self.szulEv = int(szulEv)
        self.halEv = int(halEv)
        self.nemz = nemz
        self.cim = cim
        self.hely = int(hely)

konyvek = []
for i in range(1, len(sorok)):
    d = sorok[i].strip().split(";")
    if d[2] == "":
        d[2] = 2005
    k = konyv(d[0], d[1], d[2], d[3], d[4], d[5])
    konyvek.append(k)

print(f"{len(konyvek)} könyv van.")

minhelyezes = 100
miniro = ""
mincim = ""

for i in range(len(konyvek)):
    if konyvek[i].nemz == "magyar" and konyvek[i].hely < minhelyezes:
        minhelyezes = konyvek[i].hely
        miniro = konyvek[i].nev
        mincim = konyvek[i].cim

print(f"{miniro}: {mincim}")

van = False
for i in range(len(konyvek)):
    if konyvek[i].nemz == "német":
        van = True
        break

if van:
    print("Van német könyv")
else:
    print("Nincs német könyv")

for i in range(len(konyvek)):
    if konyvek[i].halEv - konyvek[i].szulEv > 90:
        print(konyvek[i].nev)