# =====================================
# Legyen Ön is Milliomos!
# Készítette: Kovács Réka, Czombos Noel és Radics Bence
# Osztály: 10.D
# =====================================

questions = [
    ["Mi Magyarország fővárosa?", "A) Debrecen", "B) Budapest", "C) Szeged", "D) Pécs", "B"],
    ["Hány bit egy byte?", "A) 4", "B) 8", "C) 16", "D) 32", "B"],
    ["Melyik programozási nyelv?", "A) HTML", "B) Python", "C) HTTP", "D) URL", "B"],
    ["Melyik bolygó van legközelebb a Naphoz?", "A) Föld", "B) Mars", "C) Merkúr", "D) Jupiter", "C"],
    ["Hány oldalú egy négyzet?", "A) 3", "B) 4", "C) 5", "D) 6", "B"],
    ["Melyik NEM operációs rendszer?", "A) Windows", "B) Linux", "C) Android", "D) Excel", "D"],
    ["Mi a víz képlete?", "A) CO2", "B) O2", "C) H2O", "D) NaCl", "C"],
    ["Melyik tantárgy tartozik az informatikához?", "A) Programozás", "B) Földrajz", "C) Biológia", "D) Irodalom", "A"],
    ["Hány perc egy óra?", "A) 30", "B) 45", "C) 60", "D) 90", "C"],
    ["Melyik egy keresőmotor?", "A) Facebook", "B) Google", "C) Instagram", "D) TikTok", "B"]
]

# Klasszikus nyereménylétra
prizes = [
    5000, 10000, 25000, 50000, 100000,
    250000, 500000, 1000000, 2000000, 5000000
]

# Biztonsági szintek
safe_levels = [3, 6]  # indexek (50 000 és 500 000)

current_money = 0
last_safe_money = 0

used_5050 = False
used_tel = False
used_nez = False

print("🎉 Legyen Ön is Milliomos! 🎉")
print("Válasz: A, B, C, D")
print("Megállás: STOP")
print("Segítségek: 50 | TEL | NEZ (mindegyik 1x)")
print("-" * 50)

for i in range(10):
    print(f"\n{i+1}. kérdés – Tét: {prizes[i]} Ft")
    print(questions[i][0])
    print(questions[i][1])
    print(questions[i][2])
    print(questions[i][3])
    print(questions[i][4])

    answer = input("Válaszod: ").upper()

    # Megállás
    if answer == "STOP":
        print("🛑 Megálltál.")
        print("Hazavitt nyeremény:", current_money, "Ft")
        break

    # 50:50
    if answer == "50" and not used_5050:
        used_5050 = True
        print("🆘 50:50 segítség")
        print("A helyes válasz biztosan:", questions[i][5])
        continue

    # Telefon
    if answer == "TEL" and not used_tel:
        used_tel = True
        print("📞 Telefonos segítség:")
        print("Szerintem a jó válasz:", questions[i][5])
        continue

    # Nézők
    if answer == "NEZ" and not used_nez:
        used_nez = True
        print("👥 Nézők szavazása:")
        print(f"{questions[i][5]} kapta a legtöbb szavazatot (kb. 70%)")
        continue

    # Ellenőrzés
    if answer == questions[i][5]:
        current_money = prizes[i]
        print("✅ Helyes válasz!")

        # Biztonsági szint ellenőrzése
        if i in safe_levels:
            last_safe_money = prizes[i]
            print("🔒 Elérted a biztonsági szintet!")

    else:
        print("❌ Rossz válasz!")
        print("A játék véget ért.")
        print("Visszaesel:", last_safe_money, "Ft-ra")
        break

if current_money == prizes[-1]:
    print("🏆 Gratulálok! Megnyerted az 5 000 000 Ft-ot!")
