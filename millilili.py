f = open("milliomosok.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

import random

class kerdes:
    def __init__(self, szam, kerdes, Av, Bv, Cv, Dv, helyesv, felez1, felez2, valasz):
        self.szam = int(szam)
        self.kerdes = kerdes
        self.Av = Av
        self.Bv = Bv
        self.Cv = Cv
        self.Dv = Dv
        self.helyesv = helyesv
        self.felez1 = felez1
        self.felez2 = felez2
        self.valasz = valasz

konnyu = []
for i in range(10):
    darabok = sorok[i].strip().split("|")
    k = kerdes(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4], darabok[5], darabok[6], darabok[7], darabok[8], darabok[9])
    konnyu.append(k)


kozepes = []
for i in range(10, 20):
    darabok = sorok[i].strip().split("|")
    k = kerdes(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4], darabok[5], darabok[6], darabok[7], darabok[8], darabok[9])
    kozepes.append(k)

nehez = []
for i in range(20, 30):
    darabok = sorok[i].strip().split("|")
    k = kerdes(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4], darabok[5], darabok[6], darabok[7], darabok[8], darabok[9])
    nehez.append(k)


def kozonseg():
    global ksz
    valaszok=["A", "B", "C", "D"]
    tudjake=random.randint(1,3)
    if tudjake<3:
        x=konnyu[ksz].helyesv
        xsz=random.randint(25,50)


        y = random.choice(valaszok)
        while y==x:
            y=random.choice(valaszok)
        ysz=50-xsz


        z=random.choice(valaszok)
        while z==y or z==x:
            z=random.choice(valaszok)
        zsz=random.randint(0,50)
        wsz=50-zsz

        w=random.choice(valaszok)
        while w==z or w==x or w==y:
            w=random.choice(valaszok)

        kevero=random.randint(1,4)
        if kevero==1:
            print("A közönség válaszolt!")
            print(f"{x}) {xsz}%    {y}) {ysz}%    {z}) {zsz}%     {w}) {wsz}%")
        elif kevero==2:
            print("A közönség válaszolt!")
            print(f"{y}) {ysz}%    {x}) {xsz}%    {z}) {zsz}%     {w}) {wsz}%")
        elif kevero==3:
            print("A közönség válaszolt!")
            print(f"{z}) {zsz}%    {y}) {ysz}%    {x}) {xsz}%     {w}) {wsz}%")
        else:
            print("A közönség válaszolt!")
            print(f"{w}) {wsz}%    {y}) {ysz}%    {z}) {zsz}%     {x}) {xsz}%")
    else:
        w=konnyu[ksz].helyesv
        wsz=random.randint(25,50)


        y = random.choice(valaszok)
        while y==w:
            y=random.choice(valaszok)
        ysz=50-wsz


        z=random.choice(valaszok)
        while z==y or z==w:
            z=random.choice(valaszok)
        zsz=random.randint(0,50)
        xsz=50-zsz

        x=random.choice(valaszok)
        while x==z or x==w or x==y:
            x=random.choice(valaszok)

        kevero=random.randint(1,4)
        if kevero==1:
            print("A közönség válaszolt!")
            print(f"{x}) {xsz}%    {y}) {ysz}%    {z}) {zsz}%     {w}) {wsz}%")
        elif kevero==2:
            print("A közönség válaszolt!")
            print(f"{y}) {ysz}%    {x}) {xsz}%    {z}) {zsz}%     {w}) {wsz}%")
        elif kevero==3:
            print("A közönség válaszolt!")
            print(f"{z}) {zsz}%    {y}) {ysz}%    {x}) {xsz}%     {w}) {wsz}%")
        else:
            print("A közönség válaszolt!")
            print(f"{w}) {wsz}%    {y}) {ysz}%    {z}) {zsz}%     {x}) {xsz}%")


def felezes():
    global kor
    if kor <=3:
        if konnyu[ksz].felez1=="A" or konnyu[ksz].felez2=="A":
            konnyu[ksz].Av="A) XXXXXXXXX"

        if konnyu[ksz].felez1=="B" or konnyu[ksz].felez2=="B":
            konnyu[ksz].Bv="B) XXXXXXXXX"

        if konnyu[ksz].felez1=="C" or konnyu[ksz].felez2=="C":
            konnyu[ksz].Cv="C) XXXXXXXXX"

        if konnyu[ksz].felez1=="D" or konnyu[ksz].felez2=="D":
            konnyu[ksz].Dv="D) XXXXXXXXX"

    elif kor <= 6:
        if kozepes[ksz].felez1 == "A" or kozepes[ksz].felez2 == "A":
            kozepes[ksz].Av = "A) XXXXXXXXX"

        if kozepes[ksz].felez1 == "B" or kozepes[ksz].felez2 == "B":
            kozepes[ksz].Bv = "B) XXXXXXXXX"

        if kozepes[ksz].felez1 == "C" or kozepes[ksz].felez2 == "C":
            kozepes[ksz].Cv = "C) XXXXXXXXX"

        if kozepes[ksz].felez1 == "D" or kozepes[ksz].felez2 == "D":
            kozepes[ksz].Dv = "D) XXXXXXXXX"

    else:
        if nehez[ksz].felez1 == "A" or nehez[ksz].felez2 == "A":
            nehez[ksz].Av = "A) XXXXXXXXX"

        if nehez[ksz].felez1 == "B" or nehez[ksz].felez2 == "B":
            nehez[ksz].Bv = "B) XXXXXXXXX"

        if nehez[ksz].felez1 == "C" or nehez[ksz].felez2 == "C":
            nehez[ksz].Cv = "C) XXXXXXXXX"

        if nehez[ksz].felez1 == "D" or nehez[ksz].felez2 == "D":
            nehez[ksz].Dv = "D) XXXXXXXXX"

    if kor <=3:
        print(f"Válaszlehetőségek (felezéssel): {konnyu[ksz].Av}, {konnyu[ksz].Bv}, {konnyu[ksz].Cv}, {konnyu[ksz].Dv}")
    elif kor <=6:
        print(f"Válaszlehetőségek (felezéssel): {kozepes[ksz].Av}, {kozepes[ksz].Bv}, {kozepes[ksz].Cv}, {kozepes[ksz].Dv}")
    else:
        print(f"Válaszlehetőségek (felezéssel): {nehez[ksz].Av}, {nehez[ksz].Bv}, {nehez[ksz].Cv}, {nehez[ksz].Dv}")


def telefon():
    ran = random.randint(1, 4)
    if ran == 1:
        ran = "A"
    elif ran == 2:
        ran = "B"
    elif ran == 3:
        ran = "C"
    elif ran == 4:
        ran = "D"
    trisz = [f"Pfu tesó éppen programozom a CockBeater2000-et (KakasVerő2000), hát szerintem a {ran} a jó.", "Szia, Big T 4 éves lány barátja vagyok. Big T éppen a koliban kardozik, nem ér rá. Nem tudom mit jelentenek ezek a szavak, de legyen a C mert szeretem a cicákat!", f"Csá, éppen eszem a húgommal  a túrót, de ő azt mondta, hogy a {ran} válasz jónak hangzik."]
    micsi = [f"Sorry bro, I’m sitting in english class at the moment, I don’t understand any of your words, but pick {ran}, trust me.",f"Hello, éppen a wc-n ülök de mondjad. ...*csobbanás*... Tesó pont csobbant és nem értettem, de jelöljed a {ran} választ." f"Csáo, mizu? Pfu ez nehéz kérdés, idehívom a down-kóros kistesóm Ladát. Lada, melyik a jó válasz? -Sha, sha, shakira *twerkelni kezd*-  Na jó Lada most nem tud segíteni, legyen a {ran} válasz."]
    tel = input(f"3 nagyon éles érett férfi áll rendelkezésedre: Big T(=T), Krisz(=K) és Micsike(=M). \n Jól fontold meg kit választasz, összes jó választás, de mindig van egy jobb. Írd be a nevek nagy kezdőbetűjét a kiválasztáshoz")
    if tel == "K":
        if kor <= 3:
            print(konnyu[ksz].valasz)
        elif kor <= 6:
            print(kozepes[ksz].valasz)
        else:
            print(nehez[ksz].valasz)

    if tel == "T":
        print(random.choice(trisz))

    if tel == "M":
        print(random.choice(micsi))



def segitseg():
    global kor
    global segitsegek
    global felezesvane
    global telefonvane
    global kozonsegvane
    print(f"Kedves {nev}! Hogyan látja? Nehéz? Vagy nem annyira? Vagy csak ön kevés hozzá kedves {nev}?")
    ker=input(f"Kér segítséget kedves {nev}? (i=igen, n=nem)")
    if ker == "i":
        print("-----------------------------------!!!SEGÍTSÉG KÉRÉS!!!-----------------------------------")
        print("Őszintén megmondom láttam, hogy ön kevés lesz hozzá.")
        print(f"Én megmondom magának amikor feljött a szinpadra már akkor láttam kedves {nev}, hogy ön a {kor}. kérdésnél el fog vérezni.")
        print(f"De nem baj az ilyenek miatt vannak a segítségek. Mint ön kedves {nev}!")
        print(f"Önnek még pontosan {len(segitsegek)} segítsége van.")
        ms=input(f"Önnek a {segitsegek} segítség(ek) állnak rendelkezésére kedves {nev}. Melyiket használja fel? (ha mégse kér segítséget=X)")
        while ms != "F" and ms != "X" and ms != "T" and ms != "K" :
            ms = input(f"Tudna érthetőbben fogalmazni? Önnek a {segitsegek} segítség(ek) áll(nak) rendelkezésére. (ha mégse kér segítséget=X)")
        if ms == "F":
            if felezesvane==True:
                print("----------------------FELEZÉS-------------------")
                felezes()
                segitsegek.remove("Felezés (=F)")
                print("------------------------------------------------")
                felezesvane=False
            else:
                print(f"Ügyes próbálkozás kedves {nev} de ez most nem jött be (önnek már csak a {segitsegek} segítségei vannak meg)")

        elif ms=="T":
            if telefonvane==True:
                print("----------------------TELEFON-------------------")
                telefon()
                segitsegek.remove("Telefon (=T)")
                print("------------------------------------------------")
                telefonvane = False
            else:
                print(f"Ügyes próbálkozás kedves {nev} de ez most nem jött be (önnek már csak a {segitsegek} segítségei vannak meg)")

        elif ms == "K":
            if kozonsegvane == True:
                print("----------------------KÖZÖNSÉG-------------------")
                kozonseg()
                segitsegek.remove("Közönség (=K)")
                print("------------------------------------------------")
                kozonsegvane = False
            else:
                print(f"Ügyes próbálkozás kedves {nev} de ez most nem jött be (önnek már csak a {segitsegek} segítségei vannak meg)")
        elif ms == "X":
            print("Ó szóval azt hiszi egyedül is menni fog? Na lássuk!")

    elif ker == "n":
        print("-----------------------------------!!!NEM KÉR SEGÍTSÉGET!!!-----------------------------------")
        print("Ó szóval azt hiszi egyedül is menni fog? Na lássuk!")

    else:
        print("-----------------------------------!!!NEM KÉR SEGÍTSÉGET!!!-----------------------------------")
        print(f"Ha nem bír beírni egy kis i betűt akkor ön reménytelen kedves {nev} nem is érdemli meg a segítségeket.")




jo = False

def kerdes(konnyu, kozepes, nehez, kor):
    global jo
    global ksz
    global ksz1
    global ksz2
    ksz = random.randint(0, 9)
    while ksz==ksz1 and ksz==ksz2:
        ksz = random.randint(0, 9)
    biztos = False
    if kor <= 3:
        print(f"Az {kor}. kérdésem Önhöz tisztelt {nev}. {konnyu[ksz].kerdes}")
        print(f"Válaszlehetőségek: {konnyu[ksz].Av}, {konnyu[ksz].Bv}, {konnyu[ksz].Cv}, {konnyu[ksz].Dv}")

        while biztos != True:
            segitseg()
            valasz = input(f"Jól gondolja meg a válaszát kedves {nev} Válaszod: ").strip()

            while valasz != "A" and valasz != "B" and valasz != "C" and valasz != "D":
                valasz = input(f"Tudom, hogy okosnak hiszi magát {nev} de ez ide kevés lesz, kérem írja be a válasza betűjelét! (A,B,C,D){konnyu[ksz].kerdes}")
            biztosan = input("Bizosan megjelöli? (i=igen, n=nem)")
            if biztosan == "i":
                biztos = True

    elif kor <= 6:
        print(f"Az {kor}. A következő kérdésem tisztelt {nev} {kozepes[ksz].kerdes}")
        print("Ez már nem olyan egyszerű, igaz?")
        print(f"Válaszlehetőségek: {kozepes[ksz].Av}, {kozepes[ksz].Bv}, {kozepes[ksz].Cv}, {kozepes[ksz].Dv}")

        while biztos != True:
            segitseg()
            valasz = input(f"Jól gondolja meg a válaszát {nev}. Válaszod: ")

            while valasz != "A" and valasz != "B" and valasz != "C" and valasz != "D":
                valasz = input(f"Kérem ne szórakozzon velem {nev}, kérem írja be a válasza betűjelét! (A,B,C,D) Nem olyan bonyolult! El mondom mégegyszer a kérdést: {kozepes[ksz].kerdes}")
            biztosan = input("Bizosan megjelöli? (i=igen, n=nem)")
            if biztosan == "i":
                biztos = True

    else:
        print(f"Az {kor}.A kérdésem tisztelt {nev} {nehez[ksz].kerdes}")
        print("Sajnálom, de tudja ez egy ilyen játék. Vannak akik tudják a választ, meg itt van Ön.")
        print(f"Válaszlehetőségek: {nehez[ksz].Av}, {nehez[ksz].Bv}, {nehez[ksz].Cv}, {nehez[ksz].Dv}")

        while biztos != True:
            segitseg()
            valasz = input(f"Jól gondolja meg a válaszát kedves {nev}. Válaszod: ")

            while valasz != "A" and valasz != "B" and valasz != "C" and valasz != "D":
                valasz = input(f"Tudom okosnak hiszi magát {nev}, de ez ide kevés lesz, kérem írja be a válasza betűjelét! (A,B,C,D){nehez[ksz].kerdes}")
            biztosan = input("Bizosan megjelöli? (i=igen, n=nem)")
            if biztosan == "i":
                biztos = True

    if valasz == konnyu[ksz].helyesv or valasz == kozepes[ksz].helyesv or valasz == nehez[ksz].helyesv:
        jo = True
    else:
        jo = False





kor = 1
penz = 10000
ksz1=0
ksz2=0
nyert=True
telefonvane=True
segitsegek=["Felezés (=F)","Telefon (=T)","Közönség (=K)"]
felezesvane=True
kozonsegvane=True



print("Üdvözlöm a Legyen Ön is Milliomos játékban! Reméljük okosabb válaszokat ad mint ahogy kinéz")
nev = input("Hogyan szólíthatom, KedvesASDVaDF:")

while kor <= 10:
    kerdes(konnyu, kozepes, nehez, kor)
    if kor % 2 == 0:
         ksz1=ksz

    elif kor % 3 == 0:
        ksz1 = 0
        ksz2 = 0
    else:
        ksz2 = ksz

    kor=kor+1
    if jo == False:
        print(f"Sajnos nem valami okos, kedves {nev}! Remélem még találkozunk, egy szebb és okosabb életben! (Ahol Ön nem ilyen BUTA) :D ")
        nyert=False
        break

    else:
        penz = penz * 2
        print("--------------------------------------!!!!!(Drámai zene)!!!!!--------------------------------------------")
        print(f"Helyes válasz! Tudtam hogy sikerülni fog! Egy percig sem kételkedtem! Eddigi nyereményed: {penz} Ft.")
        if kor>5:
            megall=input(f"Kedves {nev} ön elérkezett a(z) {kor}. kerdéesheZ! Önnek pontosan {penz}Ft-ja van Most döntenie kell! Megáll vagy tovább folytatja? (Meg állás=M, Folytatás=F)")
            if megall == "M":
                print("-----------------------------NEM FOLYTATJA------------------------------")
                break
            else:
                megall="F"
                print("-----------------------------FOLYTATJA------------------------------")
        print("---------------------------------------!!!!!dudututuru!!!!!----------------------------------------------")


if nyert == True:
    print(f'GRATULÁLOK!!! ön {penz}Ft-ot nyert!!')
    print(f"Hát kedves {nev} nem gondoltam volna ,hogy idáig eljut. Nem mondanám, hogy örülök, de önnek biztos sokat jelent ennyi pénz. (Én ezért az estéért ennyit kapok :) )")
else:
    print ('Sajnos ön ma nem nyert')
    print (f"Hát sejtettem, hogy ez lesz a vége, Ez van kedves {nev}!")


