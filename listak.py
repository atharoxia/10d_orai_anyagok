lista = ["alma", "körte", "szőlő", "dilyó"]
print(f"Lista első eleme: {lista[0]}")
print(f"Lista második eleme: {lista[1]}")
print(f"Lista utolsó eleme: {lista[-1]}")

#32 tanuló IQ-ja véletlen számokkal (110, 140)

import random
tanuloiq = [] #üres lista
for i in range(32):
    tanuloiq.append(random.randint(110, 140))

print(tanuloiq)

#A lista 6-iktól 10-ik eleme:
reszlista = tanuloiq[5:10]  #Az első szám a kezdőindex, a második eggyel nagyobb, mint az utolsó
print(reszlista)

#Mennyi az osztály IQ-jának átlaga két tizedes pontossággal:
osszeg = 0
for i in range(32):
    osszeg += tanuloiq[i]

atlag = round(osszeg / 32, 2)
print(f"Az osztály IQ-jának átlaga: {atlag}")

#Hány tanuló IQ-ja 130 feletti:
db = 0
for i in range(32):
    if tanuloiq[i] > 130:
        db += 1
print(f"{db} tanulónak nagyobb 130-nál az IQ-ja.")

#Hányadik a legokosabb tanuló, és mennyi az IQ-ja:

max = 0
maxi = 0
for i in range(32):
    if tanuloiq[i] > max:
        max = tanuloiq[i]
        maxi = i
print(f"A legokosabb a {maxi + 1}-edik tanuló, {max} az IQ-ja.")
