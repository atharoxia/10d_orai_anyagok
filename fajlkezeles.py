f = open("be.txt", "r", encoding="utf-8")
a = int(f.readline())
b = int(f.readline())
f.close()
osszeg = a + b
f = open("ki.txt", "w", encoding="utf-8")
print(osszeg, file=f)
f.close()


#Mondatok feldarabolása
f = open("mondatok.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

print(sorok)

f = open("szavak.txt", "w", encoding="utf-8")
for i in range(len(sorok)):
    sorok[i] = sorok[i][0:len(sorok[i])-2]
    darabok = sorok[i].split()
    for j in range(len(darabok)):
        print(darabok[j], file=f)
    print(".", file=f)

f.close()



