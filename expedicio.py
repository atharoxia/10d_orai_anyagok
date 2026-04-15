f = open("veetel.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

class vetel:
    def __init__(self, nap, amator, uzenet):
        self.nap = int(nap)
        self.amator = int(amator)
        self.uzenet = uzenet

vetelek = []

for i in range(0, len(sorok), 2):
    darabok = sorok[i].strip().split()
    v = vetel(darabok[0], darabok[1], sorok[i+1].strip())
    vetelek.append(v)

print(f"Első üzenet rögzítője: {vetelek[0].amator}")
print(f"Utolsó üzenet rögzítője: {vetelek[-1].amator}")


for v in vetelek:
    if v.uzenet.__contains__("farkas"):
        print(f"{v.nap} {v.amator}")

for nap in range(1, 12):
    db = 0
    for v in vetelek:
        if v.nap == nap:
            db += 1
    print(f"{nap}. nap: {db}")


f = open("adaas.txt", "w", encoding="utf-8")

for nap in range(1, 12):
    alap = ["#"] * 90
    for v in vetelek:
        if v.nap == nap:
            for i in range(len(v.uzenet)):
                if v.uzenet[i] != "#":
                    alap[i] = v.uzenet[i]
    print("".join(alap), file=f)

f.close()

nap = int(input("Írjon be egy napot: "))
amator = int(input("Írja be egy amatőr számát: "))

vizsgalando = ""
for v in vetelek:
    if v.nap == nap and v.amator == amator:
        vizsgalando = v.uzenet.split(" ")[0]

if vizsgalando == "":
    print("Nincs ilyen feljegyzés!")
else:
    darabok = vizsgalando.split("/")
    if len(darabok) != 2:
        print("Nincs információ!")
    else:
        if darabok[0].isdigit() and darabok[1].isdigit():
            print(int(darabok[0]) + int(darabok[1]))
        else:
            print("Nincs információ!")

