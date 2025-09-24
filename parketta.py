szeles = float(input("Kérem a szoba szélességét: "))
hossz = float(input("Kérem a szoba hosszúságát: "))
csomag = int(input("Hány csomag parketta van: "))

terulet = szeles * hossz
print(f"A szoba területe {terulet} négyzetméter.")

if csomag * 2 >= terulet:
    print("Van elegendő parketta.")
else:
    print("Szükséges még parkettát vásárolni.")


termek_ft = int(input("Kérem a termék árát forintban: "))
euro_arf = float(input("Kérem az euro árfolyamát: "))
euro = int(input("Mennyi euróval rendelkezel: "))

penz_ft = euro * euro_arf
if penz_ft >= termek_ft:
    print("A terméket meg tudod venni.")
else:
    print("Nincs elég pénzed.")

#Olvassuk be egy téglalap két oldalát és egy kör sugarát
#Számítsuk ki a kerületüket, és írjuk ki, hogy melyik a nagyobb


