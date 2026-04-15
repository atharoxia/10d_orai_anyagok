from email.encoders import encode_quopri

f = open("kolcsonzesek.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

class kolcsonzes:
    def __init__(self, nev, azon, kora, kperc, vora, vperc):
        self.nev = nev
        self.azon = azon
        self.kora = int(kora)
        self.kperc = int(kperc)
        self.vora = int(vora)
        self.vperc = int(vperc)

kolcsonzesek = []
for i in range(1, len(sorok)):
    darabok = sorok[i].strip().split(";")
    k = kolcsonzes(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4], darabok[5])
    kolcsonzesek.append(k)

print(f"5. feladat: Kölcsönzések száma: {len(kolcsonzesek)}")

nev = input("6. feladat: Kérek egy nevet: ")

van = False

for i in range(len(kolcsonzesek)):
    if kolcsonzesek[i].nev == nev:
        van = True
        print(f"{kolcsonzesek[i].kora}:{kolcsonzesek[i].kperc} - {kolcsonzesek[i].vora}:{kolcsonzesek[i].vperc}")

if van == False:
    print("Nem volt ilyen nevű kölcsönző")

idopont = input("7. feladat: Adjon meg egy időpontot: ")
darabok = idopont.strip().split(":")

percben = int(darabok[0]) * 60 + int(darabok[1])

for i in range(len(kolcsonzesek)):
    if kolcsonzesek[i].kora * 60 + kolcsonzesek[i].kperc <= percben and kolcsonzesek[i].vora * 60 + kolcsonzesek[i].vperc >= percben:
        print(f"\t{kolcsonzesek[i].kora}:{kolcsonzesek[i].kperc} - {kolcsonzesek[i].vora}:{kolcsonzesek[i].vperc} : {kolcsonzesek[i].nev}")

osszeg = 0

for i in range(len(kolcsonzesek)):
    eltelt = (kolcsonzesek[i].vora * 60 + kolcsonzesek[i].vperc) - (kolcsonzesek[i].kora * 60 + kolcsonzesek[i].kperc)
    felorak = eltelt // 30
    if eltelt // 30 != eltelt / 30:
        felorak += 1

    osszeg += felorak * 2400

print(osszeg)

f = open("F.txt", "w", encoding="utf-8")

for i in range(len(kolcsonzesek)):
    if kolcsonzesek[i].azon == "F":
        print(f"{kolcsonzesek[i].kora}:{kolcsonzesek[i].kperc} - {kolcsonzesek[i].vora}:{kolcsonzesek[i].vperc} : {kolcsonzesek[i].nev}", file=f)

f.close()

azonositok = set()
for i in range(len(kolcsonzesek)):
    azonositok.add(kolcsonzesek[i].azon)

azonositolista = list(azonositok)
azonositolista.sort()

for a in azonositolista:
    db = 0
    for i in range(len(kolcsonzesek)):
        if kolcsonzesek[i].azon == a:
            db += 1
    print(f"{a} - {db}")


szotar = {
    "alma": 3,
    "korte": 4,
    "szilva": 6
}

print(szotar["alma"])

berlesek = {}

for k in kolcsonzesek:
    if berlesek.keys().__contains__(k.azon):
        berlesek[k.azon] += 1
    else:
        berlesek[k.azon] = 1

print(berlesek)



