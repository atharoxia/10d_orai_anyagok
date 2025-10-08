
tomeg = 0
kicsi = 0
kozepes = 0
nagy = 0
max = tomeg
while tomeg != -1:
    tomeg = int(input("Csomag tömege:"))
    if tomeg > max:
        max = tomeg
    if 0 < tomeg < 10:
        print ("A csomag kicsi méretű")
        kicsi += 1

    elif 10 <= tomeg <= 50:
        print ("A csomag közepes méretű")
        kozepes += 1
    elif 50 < tomeg:
        print("A csomag nagy méretű")
        nagy += 1


print(f"Kis csomagok száma:{kicsi}, közepes csomagok száma:{kozepes}, nagy csomagok száma:{nagy} \n A legnagyobb tömegű: {max} kg ")



