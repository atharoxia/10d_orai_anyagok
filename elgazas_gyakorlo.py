#Beolvassa, hogy hány óra van, és a napszaknak megfelelően köszön!

ora = int(input("Hány óra van? "))

if ora < 0 or ora > 23:
    print("Nincs ilyen óra!")
elif ora >= 6 and ora <= 10:
    print("Jó reggelt!")
elif ora >= 11 and ora <= 17:
    print("Jó napot!")
elif ora >= 18 and ora <= 21:
    print("Jó estét!")
else:
    print("Jó éjszakát!")

#Olvassuk be egy dolgozat pontszámát és az összpontszámot, számítsuk ki, hogy hány százalék lett, és adjunk rá jegyet!

pont = int(input("Mennyi pontot értél el? "))
ossz = int(input("Mennyi az összpontszám? "))

szazalek = pont / ossz * 100
print(f"Százalék: {szazalek}%")

if szazalek >= 0 and szazalek < 40:
    print("1-es lett.")
elif szazalek >= 40 and szazalek < 50:
    print("2-es lett.")
elif szazalek >= 50 and szazalek < 60:
    print("3-as lett.")
elif szazalek >= 60 and szazalek < 80:
    print("4-es lett.")
elif szazalek >= 80 and szazalek <= 100:
    print("5-ös lett.")
else:
    print("Ilyen eredmény nem lehetséges!")
