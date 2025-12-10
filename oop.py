class etel:
    def __init__(self, nev, kaloria, eheto):
        self.nev = nev
        self.kaloria = kaloria
        self.eheto = eheto


class ember:
    def __init__(self, szul_datum, nev, anyja, magas, lab, nem, telitettseg):
        self.szul_datum = szul_datum
        self.nev = nev
        self.anyja = anyja
        self.magas = magas
        self.lab = lab
        self.nem = nem
        self.telitettseg = telitettseg

    def koszones(self, masik):
        print(f"{self.nev} vagyok. Szia {masik.nev}!")

    def eves(self, mit: etel):
        if mit.eheto == "nem":
            print("Ezt nem eszem meg!")
        elif self.telitettseg > 2000:
            print("Nem vagyok már éhes!")
        else:
            print(f"Megettem egy {mit.nev}-t. Finom volt!")
            self.telitettseg += mit.kaloria



e1 = ember("1999-01-01", "Kovács Béla", "Nagy Renáta", 176, 42, "ferfi", 0)
e2 = ember("2000-01-01", "Kiss Enikő", "Közepes Klára", 160, 37, "no", 0)

print(e1.nev)
print(e2.nev)

e1.koszones(e2)

rhus = etel("rántott hús", 300, "igen")
gyilkos = etel("gyilkos galóca", 200, "nem")

e1.eves(rhus)
e1.eves(rhus)
e1.eves(gyilkos)
e1.eves(rhus)
e1.eves(rhus)
e1.eves(rhus)
e1.eves(rhus)
e1.eves(rhus)
e1.eves(rhus)

