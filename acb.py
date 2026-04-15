f = open("eredmenyek.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

class eredmeny:
    def __init__(self, hazai, idegen, hp, ip, hely, ido):
        self.hazai = hazai
        self.idegen = idegen
        self.hp = int(hp)
        self.ip = int(ip)
        self.hely = hely
        self.ido = ido

eredmenyek = []
for i in range(1, len(sorok)):
    darabok = sorok[i].strip().split(";")
    e = eredmeny(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4], darabok[5])
    eredmenyek.append(e)

hazaidb = 0
idegendb = 0

for e in eredmenyek:
    if e.hazai == "Real Madrid":
        hazaidb += 1

    if e.idegen == "Real Madrid":
        idegendb += 1

print(f"Real Madrid: {hazaidb} {idegendb}")

volt = False

for e in eredmenyek:
    if e.hp == e.ip:
        volt = True

if volt == True:
    print("Volt döntetlen")
else:
    print("Nem volt döntetlen")

for e in eredmenyek:
    if e.hazai.__contains__("Barcelona"):
        print(e.hazai)
        break

for e in eredmenyek:
    if e.ido == "2004-11-21":
        print(f"{e.hazai}-{e.idegen} ({e.hp}:{e.ip})")

stadionok = set()
for e in eredmenyek:
    stadionok.add(e.hely)

for s in stadionok:
    db = 0
    for e in eredmenyek:
        if e.hely == s:
            db += 1

    if db > 20:
        print(f"{s} {db}")