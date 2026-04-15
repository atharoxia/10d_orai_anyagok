# Készítette: Szabó Júlia, Faragó Dávid és Némedi-Varga Máté
kerdes = []
talalat = True
folytatas = "y"
darabok = []
nyeremeny  = 5
vegig = False
fixnyeremeny = 0
szamlalo = -1
mimika = True
f = open("kérdések.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

print("_________________________________________________________________________________________________________________")
print("Üdvözöljük a 'Legyen Ön is Milliomos' játékunkban!")
print()
print("Köszönjük, hogy játszol a játékunkkal.")
print("                                            Köszönettel: Szabó Júlia, Faragó Dávid és Némedi-Varga Máté")
print("_________________________________________________________________________________________________________________")

print("A mai házigazdánk: Faragó Dávid")
print("_________________________________________________________________________________________________________________")

class kerdesek:
    def __init__(self, kerdes, av, bv, cv, dv, jo):
        self.kerdes = kerdes
        self.av = av
        self.bv = bv
        self.cv = cv
        self.dv = dv
        self.jo = jo

for  i in range(0, len(sorok), 5):
        darabok1 = sorok[i].replace("\n", "")
        darabok2 = sorok[i+1].replace("\n", "")
        darabok3 = sorok[i+2].replace("\n", "")
        darabok4 = sorok[i+3].replace("\n", "")
        darabok5 = sorok[i+4].replace("\n", "")
        if "!" in darabok2:
            darabok2 = darabok2.replace("!", "")
            darabok6 = "a"
        if "!" in darabok3:
            darabok3 = darabok3.replace("!", "")
            darabok6 = "b"
        if "!" in darabok4:
            darabok4 = darabok4.replace("!", "")
            darabok6 = "c"
        if "!" in darabok5:
            darabok5 = darabok5.replace("!", "")
            darabok6 = "d"
        m = kerdesek(darabok1, darabok2, darabok3, darabok4, darabok5, darabok6)
        kerdes.append(m)

elso = input("Jöhet az első kérdés? (y/n) ")
if elso == "y" :
    print("Jó játékot, sok szerencsét!")
    print("_________________________________________________________________________________________________________________")
    for i in range(15):
        szamlalo += 1
        if i > 0:
            nyeremeny *= 2
        if i == 4 or i == 9:
            if nyeremeny >= 1000:
                print(f"{i + 1}. kérdés, dobbantó {nyeremeny // 1000} millió Forintért: {kerdes[i].kerdes}", )
            else:
                print(f"{i + 1}. kérdés, dobbantó {nyeremeny} ezer Forintért: {kerdes[i].kerdes}",)
        else:
            if nyeremeny >= 1000:
                print(f"{i + 1}. kérdés {nyeremeny // 1000} millió Forintért: {kerdes[i].kerdes}", )
            else:
                print(f"{i + 1}. kérdés {nyeremeny} ezer Forintért: {kerdes[i].kerdes}", )
        print(kerdes[i].av)
        print(kerdes[i].bv)
        print(kerdes[i].cv)
        print(kerdes[i].dv)
        megoldas = input("Melyik a helyes válasz Ön szerint? ")
        print()
        megoldas = megoldas.lower()
        if megoldas == kerdes[i].jo:
            print("Helyes válasz. Gratulálunk, csak így tovább!")
            if i == 4 or i == 9:
                fixnyeremeny = nyeremeny*2
            print("____________________________________________________________________________________________________________")
        else:
            talalat = False
            print(f"Sajnos helytelen a válaszod. A helyes válasz: {kerdes[i].jo} volt.")
            nyeremeny = 0
            mimika = False
            print("____________________________________________________________________________________________________________")
            break
        if i != 14:
            if (nyeremeny * 2) >= 1000:
                folytatas = input(f"Folytatja-e {(nyeremeny * 2)//1000} millió Forintért? y/n: ")
            else:
                folytatas = input(f"Folytatja-e {nyeremeny * 2} ezer Forintért? y/n: ")
            print("____________________________________________________________________________________________________________")
        else:
            vegig = True
        if folytatas == "y":
            continue
        else:
            if nyeremeny >= 1000:
                print(f"Sajnáljuk, hogy nem folytatja a játékunkat. A nyereménye {nyeremeny // 1000} millió Forint.")
            else:
                print(f"Sajnáljuk, hogy nem folytatja a játékunkat. A nyereménye {nyeremeny} ezer Forint.")
            break

elif elso != "y":
    print()
    print("Sajnáljuk, hogy nem szeretnél most játszani, ha meggondolod magad bármikor újraindíthatod és elkezdheted.")

if talalat == False and fixnyeremeny == 0:
    print("Köszönjük, hogy velünk játszott.")
if talalat == False and fixnyeremeny != 0:
    if fixnyeremeny <= 1000:
        print(f"Köszönjük, hogy velünk játszott. A nyereménye : {fixnyeremeny} ezer Forint.")
    else:
        print(f"Köszönjük, hogy velünk játszott. A nyereménye : {fixnyeremeny // 1000} millió Forint.")
elif vegig == True:
    print("Gratulálunk, ön egy milliomos!")
    print(f"A nyereménye {nyeremeny // 1000} millió Forint")
elif vegig == False  and szamlalo > 0 and mimika == True:
    if nyeremeny >= 1000:
        print(f"Ön {nyeremeny // 1000} millió Forintot nyert.")
    else:
        print(f"Ön {nyeremeny} ezer Forintot nyert.")