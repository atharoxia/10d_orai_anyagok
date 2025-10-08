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


