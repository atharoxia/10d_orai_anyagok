#Írjuk ki 1-től 10-ig a számokat:
for i in range(1, 11):
    print(i)
print("--------------")
#Írjuk ki 2-től 100-ig a páros számokat:
for i in range(2, 101, 2):
    print(i)
print("--------------")
#Írjuk ki 50-től 0-ig visszafelé a számokat:
for i in range(50, -1, -1):
    print(i)

#Olvassunk be számokat, amíg 6-ot nem írnak be:
szam = int(input("Írj be egy számot: "))
while szam != 6:
    szam = int(input("Írj be egy számot: "))


#Olvassunk be egy számot, és írjuk ki az osztóit:
szam = int(input("Írj be egy számot: "))
print("A szám osztói:")
for i in range(1, szam + 1):
    if szam % i == 0:
        print(i)


