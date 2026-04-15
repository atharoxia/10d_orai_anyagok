''''
Made by: Szilvási Hunor, Barta Sándor, Éder Millica
'''

print("LEGYEN ÖN IS MILLIOMOS!")
print("----------------------")

# nyeremények
nyeremenyek = [
    100000, 200000, 500000, 1000000, 2000000,
    3000000, 5000000, 8000000, 15000000, 30000000
]

f = open("kerdesek.txt", "r", encoding="utf-8")     #Beolvassa a txt-t
sorok = f.read().split("\n")
f.close()

kerdesek = []   #feldolgozott kerrdesek lesznek eltarolva
i = 0           #Vegig lepked a sorokon

while i < len(sorok):           #sor ures a program atugorja
    if sorok[i].strip() == "":
        i += 1
        continue

    kerdes = sorok[i]       #kerdes, valasz, helyes v kiolvassas
    a = sorok[i + 1]
    b = sorok[i + 2]
    c = sorok[i + 3]
    d = sorok[i + 4]
    helyes = sorok[i + 5]

    kerdesek.append([kerdes, a, b, c, d, helyes]) #kerdes es a hozza tartozo adatok egy listaba kerulnek
    i += 6

nyeremeny = 0

for i in range(len(kerdesek)):
    print()
    print(str(i + 1) + ". kérdés:")     #Kiirja az aktualis kerdes sorszamat es szoveget.
    print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
    print(kerdesek[i][0])
    print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
    print("A)", kerdesek[i][1])
    print("B)", kerdesek[i][2])
    print("C)", kerdesek[i][3])
    print("D)", kerdesek[i][4])
    print("-------------------------------------------------------")
    print("Nyeremény:", nyeremenyek[i], "Ft")
    print("-------------------------------------------------------")
    print("Írd be a választ (A/B/C/D) vagy S = megállok")
    print("___________________________________________________________")
    valasz = input("Válasz: ").upper()

    if valasz == "S":
        print("<><><><><><><><><><><><><><><><><><><><><><><>")
        print("Megálltál.")
        print("<><><><><><><><><><><><><><><><><><><><><><><>")
        print("Hazavitt nyeremény:", nyeremeny, "Ft")
        break

    if valasz == kerdesek[i][5]:
        nyeremeny = nyeremenyek[i]
        print("______________________________________________")
        print("Ügyi!")
        print("______________________________________________")
        print("Jelenlegi nyeremény:", nyeremeny, "Ft")
    else:
        print("<><><><><><><><><><><><><><><><><><><><><><><>")
        print("HAHHAHA ELBASZTAD!")
        print("______________________________________________")
        print("A helyes válasz:", kerdesek[i][5])
        print("<><><><><><><><><><><><><><><><><><><><><><><>")
        print("Számodra véget ért koma!!")
        print("<><><><><><><><><><><><><><><><><><><><><><><>")
        print("Nyereményed:", nyeremeny, "Ft")
        break

if nyeremeny == nyeremenyek[-1]:
    print()
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("Kifosztottad a kasszát!!:", nyeremeny, "Ft")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")