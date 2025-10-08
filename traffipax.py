seb = int(input("Írjon be egy sebességet: "))
traffipax = []
while seb != 0:
    traffipax.append(seb)
    seb = int(input("Írjon be egy sebességet: "))

#Gyorshajtók irányonként:
gyorshajto_kecsk = 0  #pluszosok
gyorshajto_kkf = 0    #minuszsok

for i in range(len(traffipax)):
    if traffipax[i] > 90:
        gyorshajto_kecsk += 1

    if traffipax[i] < -90:
        gyorshajto_kkf += 1

print(f"Az egyik irányban {gyorshajto_kecsk}, a másik irányban {gyorshajto_kkf} gyorhajtó volt.")

#Leggyorsabbak irányoként?
leggy_kecsk = 0
leggy_kkf = 0
hanyadik_kecsk = 0
hanyadik_kkf = 0

for i in range(len(traffipax)):
    if traffipax[i] > leggy_kecsk:
        leggy_kecsk = traffipax[i]
        hanyadik_kecsk = i

    if traffipax[i] < leggy_kkf:
        leggy_kkf = traffipax[i]
        hanyadik_kkf = i

print(f"Az egyik irányban a leggyorsabb a {hanyadik_kecsk + 1}-ik, aitó volt, {leggy_kecsk}-tel ment.")
print(f"Az másik irányban a leggyorsabb a {hanyadik_kkf + 1}-ik, aitó volt, {-leggy_kkf}-tel ment.")

#Az átlagsebesség irányonként

db_kecsk = 0
db_kkf = 0
osszeg_kecsk = 0
osszeg_kkf = 0

for i in range(len(traffipax)):
    if traffipax[i] > 0:
        osszeg_kecsk += traffipax[i]
        db_kecsk += 1
    else:
        osszeg_kkf += traffipax[i]
        db_kkf += 1

print(f"Az egyik irányban {osszeg_kecsk / db_kecsk} volt az átlag.")
print(f"A másik irányban {-osszeg_kkf / db_kkf} volt az átlag.")




