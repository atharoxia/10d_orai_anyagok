f = open("hegyekMo.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

class hegy:
    def __init__(self, nev, hegyseg, magas):
        self.nev = nev
        self.hegyseg = hegyseg
        self.magas = magas

hegyek = []
for i in range(1, len(sorok)):
    darabok = sorok[i].strip().split(";")
    h = hegy(darabok[0], darabok[1], int(darabok[2]))
    hegyek.append(h)

print(hegyek)

print(f"3. feladat: Hegycsúcsok száma: {len(hegyek)}")

osszeg = 0
for i in range(len(hegyek)):
    osszeg += hegyek[i].magas

atlag = osszeg / len(hegyek)
print(f"4. feladat: A hegycsúcsok átlagos magassága: {atlag} m")

max = hegyek[0]
for i in range(1, len(hegyek)):
    if hegyek[i].magas > max.magas:
        max = hegyek[i]

print("5. feladat: A legmagasabb hegycsúcs adatai:")
print(f"\tNév: {max.nev}")
print(f"\tHegység: {max.hegyseg}")
print(f"\tMagasság: {max.magas} m")

bemagas = int(input("6. feladat: Írjon be egy magasságot: "))
van = False
for i in range(len(hegyek)):
    if hegyek[i].magas > bemagas and hegyek[i].hegyseg == "Börzsöny":
        van = True
        break

if van == True:
    print(f"Van {bemagas} méternél magasabb hegy a Börzsönyben.")
else:
    print(f"Nincs {bemagas} méternél magasabb hegy a Börzsönyben.")

lab = 3.28
db = 0
for i in range(len(hegyek)):
    if hegyek[i].magas * lab > 3000:
        db += 1

print(f"7. feladat: 3000 lábnál magasabb csúcsok száma {db} db")

f = open("bukk-videk.txt", "w", encoding="utf-8")
print("Hegycsúcs neve; Magasság láb", file=f)
for i in range(len(hegyek)):
    if hegyek[i].hegyseg == "Bükk-vidék":
        print(f"{hegyek[i].nev};{round(hegyek[i].magas * lab, 1)}", file=f)

f.close()
