import random

felezo_hasznalva = False

def felezo(helyes):
    betuk = ["A", "B", "C", "D"]
    betuk.remove(helyes)
    marad_rossz = random.choice(betuk)

    print("\nFelező segítség:")
    print("----------------")
    print(helyes)
    print(marad_rossz)




print(f"\n❤️Üdvözöllek a legyen Ön Is Milliomos játékban!❤️")
print("A válasz megadásához írja be az (A:B:C:D válasz lehgetőségeket!😁")
input(f"\nNyomj ENTER-t a kezdáshez!")

nyeremeny = 0

print(f"\n1. kérdés")
helyes_valasz = "D"
print(f"\nHány foga van a pontynak?")
print("__________________________________")
print("A: 2")
print("B: 3")
print("C: 4")
print("D: 0")

valasz = input("Írd ide a válaszod vagy 50, ha felezni akarsz:")

while valasz.strip().upper() not in ["A", "B", "C", "D", "50"]:
    print("Nem lehetséges válasz lehetőség!")
    valasz = input("Írd ide a válaszod:")

while True:
    if valasz == "50":
        if felezo_hasznalva:
            print("A felezőt már felhasználtad!")
        else:
            felezo(helyes_valasz)
            felezo_hasznalva = True
        valasz = input("Válasz: ")

    elif valasz.strip().upper() in ["A", "B", "C", "D"]:
        valasz = valasz.strip().upper()
        break


if valasz.upper() == "D":
    print("✅Helyes a válasz!")
    nyeremeny += 5000
    print( f"Nyeremenyed eddig: {nyeremeny} Ft ")
else:
    print("❌Vesztettél :(❌")
    print(f"Nyeremenyed: {nyeremeny} Ft ")
    exit()

megall = input("Ha szeretnél megállni írd be->i/n:")

if megall.upper() == "I":
    print(f"Megálltál, nyereményed:{nyeremeny} Ft. ")
    exit()
else:
    print("Mehet tovább")


print(f"\n2. kérdés")
helyes_valasz = "C"
print(f"\nMi az FPS?")
print("__________________________________")
print("A: Frames per silk")
print("B: Fountain Per Snow")
print("C: Frames per second")
print("D: Fekete Pápa Sár")

valasz = input("Írd ide a válaszod vagy 50, ha felezni akarsz:")
while True:
    if valasz == "50":
        if felezo_hasznalva:
            print("A felezőt már felhasználtad!")
        else:
            felezo(helyes_valasz)
            felezo_hasznalva = True
        valasz = input("Válasz: ")

    elif valasz.strip().upper() in ["A", "B", "C", "D"]:
        valasz = valasz.strip().upper()
        break

if valasz.upper() == "C":
    print("✅Helyes a válasz!")
    nyeremeny+=10000
    print( f"Nyeremenyed eddig: {nyeremeny} Ft ")
else:
    print("❌Vesztettél :(❌")
    print(f"Nyeremenyed: {nyeremeny} Ft ")
    exit()

megall = input("Ha szeretnél megállni írd be->i/n:")

if megall.upper() == "I":
    print(f"Megálltál, nyereményed:{nyeremeny} Ft. ")
    exit()
else:
    print("Mehet tovább")


print("3. kérdés")
helyes_valasz = "B"
print(f"\nMelyiket nevezzük a 'vörösbolygó'-nak?")
print("__________________________________")
print("A: Merkúr")
print("B: Mars")
print("C: Neptunusz")
print("D: Jupiter")

valasz = input("Írd ide a válaszod vagy 50, ha felezni akarsz:")
while True:
    if valasz == "50":
        if felezo_hasznalva:
            print("A felezőt már felhasználtad!")
        else:
            felezo(helyes_valasz)
            felezo_hasznalva = True
        valasz = input("Válasz: ")

    elif valasz.strip().upper() in ["A", "B", "C", "D"]:
        valasz = valasz.strip().upper()
        break

if valasz.upper() == "B":
    print("✅Helyes a válasz!")
    nyeremeny += 20000
    print( f"Nyeremenyed eddig: {nyeremeny} Ft ")
else:
    print("❌Vesztettél :(❌")
    print(f"Nyeremenyed: {nyeremeny} Ft ")
    exit()

megall = input("Ha szeretnél megállni írd be->i/n:")

if megall.upper() == "I":
    print(f"Megálltál, nyereményed:{nyeremeny} Ft. ")
    exit()
else:
    print("Mehet tovább")


print("4. kérdés")
helyes_valasz = "B"
print(f"\nKi írta a Vukk-ot?")
print("__________________________________")
print("A: Mikszáth Kálmán")
print("B: Fekete István")
print("C: Petőfi Sándor")
print("D: Arany János")

valasz = input("Írd ide a válaszod vagy 50, ha felezni akarsz:")
while True:
    if valasz == "50":
        if felezo_hasznalva:
            print("A felezőt már felhasználtad!")
        else:
            felezo(helyes_valasz)
            felezo_hasznalva = True
        valasz = input("Válasz: ")

    elif valasz.strip().upper() in ["A", "B", "C", "D"]:
        valasz = valasz.strip().upper()
        break

if valasz.upper() == "B":
    print("✅Helyes a válasz!")
    print( f"Nyeremenyed eddig: {nyeremeny} Ft ")
    nyeremeny+=40000
else:
    print("❌Vesztettél :(❌")
    print(f"Nyeremenyed: {nyeremeny} Ft ")
    exit()

megall = input("Ha szeretnél megállni írd be->i/n:")

if megall.upper() == "I":
    print(f"Megálltál, nyereményed:{nyeremeny} Ft. ")
    exit()
else:
    print("Mehet tovább")


print("5. kérdés")
helyes_valasz = "D"
print(f"\nMelyik Disney-karakter hagyja el üvegcipellőjét egy bálon az alábbiak közül?")
print("__________________________________")
print("A: Pocahontas")
print("B: Elsa")
print("C: Csipkerózsika")
print("D: Hamupipőke")

valasz = input("Írd ide a válaszod vagy 50, ha felezni akarsz:")
while True:
    if valasz == "50":
        if felezo_hasznalva:
            print("A felezőt már felhasználtad!")
        else:
            felezo(helyes_valasz)
            felezo_hasznalva = True
        valasz = input("Válasz: ")

    elif valasz.strip().upper() in ["A", "B", "C", "D"]:
        valasz = valasz.strip().upper()
        break

if valasz.upper() == "D":
    print("✅Helyes a válasz!")
    print( f"Nyeremenyed eddig: {nyeremeny} Ft ")
    nyeremeny+=80000
else:
    print("❌Vesztettél :(❌")
    print(f"Nyeremenyed: {nyeremeny} Ft ")
    exit()


megall = input("Ha szeretnél megállni írd be->i/n:")

if megall.upper() == "I":
    print(f"Megálltál, nyereményed:{nyeremeny} Ft. ")
    exit()
else:
    print("Mehet tovább")


print("6. kérdés")
helyes_valasz = "A"
print(f"\nKi nyerte az első football VB-t?")
print("__________________________________")
print("A: Uruguay")
print("B: Brazília")
print("C: Argentína")
print("D: Németország")

valasz = input("Írd ide a válaszod vagy 50, ha felezni akarsz:")
while True:
    if valasz == "50":
        if felezo_hasznalva:
            print("A felezőt már felhasználtad!")
        else:
            felezo(helyes_valasz)
            felezo_hasznalva = True
        valasz = input("Válasz: ")

    elif valasz.strip().upper() in ["A", "B", "C", "D"]:
        valasz = valasz.strip().upper()
        break

if valasz.upper() == "A":
    print("✅Helyes a válasz!")
    print( f"Nyeremenyed eddig: {nyeremeny} Ft ")
    nyeremeny+=100000
else:
    print("❌Vesztettél :(❌")
    print(f"Nyeremenyed: {nyeremeny} Ft ")
    exit()


megall = input("Ha szeretnél megállni írd be->i/n:")

if megall.upper() == "I":
    print(f"Megálltál, nyereményed:{nyeremeny} Ft. ")
    exit()
else:
    print("Mehet tovább")


print("7. kérdés")
helyes_valasz = "C"
print(f"\nHány megtekintés van a kosrátippek kezdőknek videón?by Kuci and Lada")
print("__________________________________")
print("A: 7k")
print("B: 7,5k")
print("C: 8,5k")
print("D: 9k")

valasz = input("Írd ide a válaszod vagy 50, ha felezni akarsz:")
while True:
    if valasz == "50":
        if felezo_hasznalva:
            print("A felezőt már felhasználtad!")
        else:
            felezo(helyes_valasz)
            felezo_hasznalva = True
        valasz = input("Válasz: ")

    elif valasz.strip().upper() in ["A", "B", "C", "D"]:
        valasz = valasz.strip().upper()
        break

if valasz.upper() == "C":
    print("✅Helyes a válasz!")
    print( f"Nyeremenyed eddig: {nyeremeny} Ft ")
    nyeremeny+=120000
else:
    print("❌Vesztettél :(❌")
    print(f"Nyeremenyed: {nyeremeny} Ft ")
    exit()

megall = input("Ha szeretnél megállni írd be->i/n:")

if megall.upper() == "I":
    print(f"Megálltál, nyereményed:{nyeremeny} Ft. ")
    exit()
else:
    print("Mehet tovább")


print("8. kérdés")
helyes_valasz = "B"
print(f"\nMi a gépjárművek tengelykapcsolójának ismertebb neve?")
print("__________________________________")
print("A: Porlasztó")
print("B: Kuplung")
print("C: Gyertya")
print("D: Akkumlátor")

valasz = input("Írd ide a válaszod vagy 50, ha felezni akarsz:")
while True:
    if valasz == "50":
        if felezo_hasznalva:
            print("A felezőt már felhasználtad!")
        else:
            felezo(helyes_valasz)
            felezo_hasznalva = True
        valasz = input("Válasz: ")

    elif valasz.strip().upper() in ["A", "B", "C", "D"]:
        valasz = valasz.strip().upper()
        break

if valasz.upper() == "B":
    print("✅Helyes a válasz!")
    print( f"Nyeremenyed eddig: {nyeremeny} Ft ")
    nyeremeny+=140000
else:
    print("❌Vesztettél :(❌")
    print(f"Nyeremenyed: {nyeremeny} Ft ")
    exit()


megall = input("Ha szeretnél megállni írd be->i/n:")

if megall.upper() == "I":
    print(f"Megálltál, nyereményed:{nyeremeny} Ft. ")
    exit()
else:
    print("Mehet tovább")



print("9. kérdés")
helyes_valasz = "C"
print(f"\nAz alábbi történelmi alakok közül kit NEM Ádám személyesít meg Az ember tragédiájában?")
print("__________________________________")
print("A: Miltiadész")
print("B: Kepler")
print("C: Michelangelo")
print("D: Danton")

valasz = input("Írd ide a válaszod vagy 50, ha felezni akarsz:")
while True:
    if valasz == "50":
        if felezo_hasznalva:
            print("A felezőt már felhasználtad!")
        else:
            felezo(helyes_valasz)
            felezo_hasznalva = True
        valasz = input("Válasz: ")

    elif valasz.strip().upper() in ["A", "B", "C", "D"]:
        valasz = valasz.strip().upper()
        break

if valasz.upper() == "C":
    print("✅Helyes a válasz!")
    print( f"Nyeremenyed eddig: {nyeremeny} Ft ")
    nyeremeny+=160000
else:
    print("❌Vesztettél :(❌")
    print(f"Nyeremenyed: {nyeremeny} Ft ")
    exit()


megall = input("Ha szeretnél megállni írd be->i/n:")

if megall.upper() == "I":
    print(f"Megálltál, nyereményed:{nyeremeny} Ft. ")
    exit()
else:
    print("Mehet tovább")


print("10. kérdés")
helyes_valasz = "A"
print(f"\nKi a szerelem istene az ősi hindu mitológiában?")
print("__________________________________")
print("A: Káma")
print("B: Coitus")
print("C: Szutra")
print("D: Interrupts")

valasz = input("Írd ide a válaszod vagy 50, ha felezni akarsz:")
while True:
    if valasz == "50":
        if felezo_hasznalva:
            print("A felezőt már felhasználtad!")
        else:
            felezo(helyes_valasz)
            felezo_hasznalva = True
        valasz = input("Válasz: ")

    elif valasz.strip().upper() in ["A", "B", "C", "D"]:
        valasz = valasz.strip().upper()
        break

if valasz.upper() == "A":
    print("✅Helyes a válasz!")
    print( f"Nyeremenyed eddig: {nyeremeny} Ft ")
    nyeremeny+=180000
else:
    print("❌Vesztettél :(❌")
    print(f"Nyeremenyed: {nyeremeny} Ft ")
    exit()


megall = input("Ha szeretnél megállni írd be->i/n:")

if megall.upper() == "I":
    print(f"Megálltál, nyereményed:{nyeremeny} Ft. ")
    exit()
else:
    print("Mehet tovább")


print("11. kérdés")
helyes_valasz = "C"
print(f"\nAz alábbiak közül melyik tudományágban NEM osztanak ki Nobel-díjat?")
print("__________________________________")
print("A: Fizika")
print("B: Kémia")
print("C: Matematika")
print("D: Orvostudomány")

valasz = input("Írd ide a válaszod vagy 50, ha felezni akarsz:")
while True:
    if valasz == "50":
        if felezo_hasznalva:
            print("A felezőt már felhasználtad!")
        else:
            felezo(helyes_valasz)
            felezo_hasznalva = True
        valasz = input("Válasz: ")

    elif valasz.strip().upper() in ["A", "B", "C", "D"]:
        valasz = valasz.strip().upper()
        break

if valasz.upper() == "C":
    print("✅Helyes a válasz!")
    print( f"Nyeremenyed eddig: {nyeremeny} Ft ")
    nyeremeny+=200000
else:
    print("Vesztettél :(")
    print(f"Nyeremenyed: {nyeremeny} Ft ")
    exit()

megall = input("Ha szeretnél megállni írd be->i/n:")

if megall.upper() == "I":
    print(f"Megálltál, nyereményed:{nyeremeny} Ft. ")
    exit()
else:
    print("Mehet tovább")


print(f"\n12. kérdés")
helyes_valasz = "C"
print(f"\nHány évesek e játéknak a készítői, összeadva és 3-mal elosztva?")
print("__________________________________")
print("A: 10,333")
print("B: 15,333")
print("C: 11,333")
print("D: 9,333")

valasz = input("Írd ide a válaszod vagy 50, ha felezni akarsz:")
while True:
    if valasz == "50":
        if felezo_hasznalva:
            print("A felezőt már felhasználtad!")
        else:
            felezo(helyes_valasz)
            felezo_hasznalva = True
        valasz = input("Válasz: ")

    elif valasz.strip().upper() in ["A", "B", "C", "D"]:
        valasz = valasz.strip().upper()
        break
if valasz.upper() == "C":
    print("✅Helyes a válasz!")
    print( f"Nyeremenyed eddig: {nyeremeny} Ft ")
    nyeremeny+=10000000
else:
    print("Vesztettél :(")
    print(f"Nyeremenyed: {nyeremeny} Ft ")
    exit()

print("Elérkeztél a játék végéhez.")
print(f"\n 🎉Gratulálok, a nyereményed {nyeremeny} Ft🎉")