tabla = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]

def kirajzol(tabla):
    print("  1 2 3")
    for i in range(len(tabla)):
        print(f"{i+1}|", end="")
        for j in range(len(tabla)):
            print(f"{tabla[i][j]}|", end="")
        print()

kirajzol(tabla)

kijon = "X"

def gyozelem(tabla):
    if tabla[0][0] == tabla[0][1] and tabla[0][1] == tabla[0][2]:
        print(f"{kijon} győzött")
    if tabla[1][0] == tabla[1][1] and tabla[1][1] == tabla[1][2]:
        print(f"{kijon} győzött")
    if tabla[2][0] == tabla[2][1] and tabla[2][1] == tabla[2][2]:
        print(f"{kijon} győzött")
    if tabla[0][0] == tabla[1][0] and tabla[1][0] == tabla[2][0]:
        print(f"{kijon} győzött")
    if tabla[0][1] == tabla[1][1] and tabla[1][1] == tabla[1][2]:
        print(f"{kijon} győzött")
    if tabla[0][2] == tabla[1][2] and tabla[1][2] == tabla[2][2]:
        print(f"{kijon} győzött")
    if tabla[0][0] == tabla[1][1] and tabla[1][1] == tabla[2][2]:
        print(f"{kijon} győzött")
    if tabla[0][2] == tabla[1][1] and tabla[1][1] == tabla[2][0]:
        print(f"{kijon} győzött")

def lepes(tabla, kijon):
    kirajzol(tabla)
    print(f"{kijon} következik!")
    sor = int(input("sor: ")) - 1
    oszlop = int(input("oszlop: ")) - 1

    jo = False
    while jo == False:
        if tabla[sor][oszlop] == ".":
            tabla[sor][oszlop] = kijon
            jo = True
        else:
            print("Oda nem léphetsz!")
            sor = int(input("sor: ")) - 1
            oszlop = int(input("oszlop: ")) - 1
            jo = False

    gyozelem(tabla)
    if kijon == "X":
        return "O"
    else:
        return "X"

while True:
    kijon = lepes(tabla, kijon)