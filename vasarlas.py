ar = int(input("Kérem a termék árát fortintban: "))
arfolyam = float(input("Kérem az euro árfolyamát: "))
euro = float(input("Mennyi euróval rendelkezel: "))

forint = euro * arfolyam

if forint >= ar:
    print("A terméket meg tudod vásárolni.")
else:
    print("Nincs elég euród a termék megvásárlására.")




