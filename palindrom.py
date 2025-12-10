f = open("palindrom.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

f = open("valasz.txt", "w", encoding="utf-8")
for i in range(len(sorok)):
    sorok[i] = sorok[i][0:-2]
    sorok[i] = sorok[i].replace(",", "")
    sorok[i] = sorok[i].replace(" ", "")
    sorok[i] = sorok[i].lower()

    forditott = "".join(reversed(sorok[i]))

    if sorok[i] == forditott:
        print("igen", file=f)
    else:
        print("nem", file=f)

f.close()