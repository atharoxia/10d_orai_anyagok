def oszthato(szam):
    if szam % 7 == 0 and szam % 3 != 0:
        return True
    else:
        return False

osszeg = 0
db = 0

for i in range(100, 1000):
    if oszthato(i):
        osszeg += i
        db += 1

atlag = osszeg / db
print(f"A számok átlaga: {atlag}")


