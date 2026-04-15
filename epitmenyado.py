f = open("utca.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

class epulet:
    def __init__(self, adosz, utca, hsz, sav, nm):
        self.adosz = adosz
        self.utca = utca
        self.hsz = hsz
        self.sav = sav
        self.nm = int(nm)

darabok = sorok[0].strip().split()
adoA = int(darabok[0])
adoB = int(darabok[1])
adoC = int(darabok[2])

epuletek = []
for i in range(1, len(sorok)):
    darabok = sorok[i].strip().split()
    e = epulet(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4])
    epuletek.append(e)

print(f"2. feladat: A mintában {len(epuletek)} telek szerepel.")

adoszam = input("3. feladat. Egy tulajdonos adószáma: ")
van = False
for i in range(len(epuletek)):
    if epuletek[i].adosz == adoszam:
        van = True
        print(f"{epuletek[i].utca} utca {epuletek[i].hsz}")

if van == False:
    print("Nem található.")

def ado(sav, terulet):
    if sav == "A":
        fizetendo = adoA * terulet
    if sav == "B":
        fizetendo = adoB * terulet
    if sav == "C":
        fizetendo = adoC * terulet

    if fizetendo >= 10000:
        return fizetendo
    else:
        return 0

dbA = 0
dbB = 0
dbC = 0
osszadoA = 0
osszadoB = 0
osszadoC = 0

for i in range(len(epuletek)):
    if epuletek[i].sav == "A":
        dbA += 1
        osszadoA += ado(epuletek[i].sav, epuletek[i].nm)

    if epuletek[i].sav == "B":
        dbB += 1
        osszadoB += ado(epuletek[i].sav, epuletek[i].nm)

    if epuletek[i].sav == "C":
        dbC += 1
        osszadoC += ado(epuletek[i].sav, epuletek[i].nm)

print(f"A sávba {dbA} telek esik, az adó {osszadoA} Ft")
print(f"B sávba {dbB} telek esik, az adó {osszadoB} Ft")
print(f"C sávba {dbC} telek esik, az adó {osszadoC} Ft")

felul = False
for i in range(len(epuletek) - 1):
    if epuletek[i].sav != epuletek[i + 1].sav and epuletek[i].utca == epuletek[i + 1].utca:
        felul = True

    if epuletek[i].utca != epuletek[i + 1].utca:
        if felul == True:
            print(epuletek[i].utca)
            felul = False


adoszamok = set()
for i in range(len(epuletek)):
    adoszamok.add(epuletek[i].adosz)

f = open("fizetendo.txt", "w", encoding="utf-8")
for a in adoszamok:
    osszes = 0
    for i in range(len(epuletek)):
        if epuletek[i].adosz == a:
            osszes += ado(epuletek[i].sav, epuletek[i].nm)

    print(f"{a} {osszes}", file=f)

f.close()