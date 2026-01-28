f = open("meccs.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

class merkozes:
    def __init__(self, ford, hg, vg, hfg, vfg, hazai, vendeg):
        self.ford = int(ford)
        self.hg = int(hg)
        self.vg = int(vg)
        self.hfg = int(hfg)
        self.vfg = int(vfg)
        self.hazai = hazai
        self.vendeg = vendeg

merkozesek = []
for i in range(1, len(sorok)):
    darabok = sorok[i].strip().split()
    m = merkozes(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4], darabok[5], darabok[6])
    merkozesek.append(m)

ford = int(input("Forduló száma: "))
for i in range(len(merkozesek)):
    if merkozesek[i].ford == ford:
        print(f"{merkozesek[i].hazai}-{merkozesek[i].vendeg}: {merkozesek[i].hg}-{merkozesek[i].vg} ({merkozesek[i].hfg}-{merkozesek[i].vfg})")

for i in range(len(merkozesek)):
    if merkozesek[i].hg > merkozesek[i].vg and merkozesek[i].hfg < merkozesek[i].vfg:
        print(f"{merkozesek[i].ford} {merkozesek[i].hazai}")

    if merkozesek[i].hg < merkozesek[i].vg and merkozesek[i].hfg > merkozesek[i].vfg:
        print(f"{merkozesek[i].ford} {merkozesek[i].vendeg}")

csapat = input("Írja be egy csapat nevét: ")

lott = 0
kapott = 0

for i in range(len(merkozesek)):
    if merkozesek[i].hazai == csapat:
        lott += merkozesek[i].hg
        kapott += merkozesek[i].vg

    if merkozesek[i].vendeg == csapat:
        lott += merkozesek[i].vg
        kapott += merkozesek[i].hg

print(f"lőtt: {lott} kapott: {kapott}")

veretlen = True
for i in range(len(merkozesek)):
    if merkozesek[i].hazai == csapat and merkozesek[i].vg > merkozesek[i].hg:
        print(f"{merkozesek[i].ford} {merkozesek[i].vendeg}")
        veretlen = False
        break

if veretlen == True:
    print("A csapat otthon veretlen maradt.")

kategoriak = set() #Üres halmaz, minden elem csak egyszer fordul elő benne, az előforduló eredmények
eredmenyek = []    #Az összes eredmény

for i in range(len(merkozesek)):
    if merkozesek[i].vg > merkozesek[i].hg:
        eredm = f"{merkozesek[i].vg}-{merkozesek[i].hg}"
    else:
        eredm = f"{merkozesek[i].hg}-{merkozesek[i].vg}"

    kategoriak.add(eredm)
    eredmenyek.append(eredm)

f = open("stat.txt", "w", encoding="utf-8")

for k in kategoriak:
    print(f"{k}: {eredmenyek.count(k)} darab", file=f)

f.close()



