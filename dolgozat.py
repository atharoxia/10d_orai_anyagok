
import random
def kategoria ():
    nyertes=[]
    szamok = []
    kategoria = int(input('Adja meg, hogy milyen kategóriában játszana.\n Lehetséges módok:\n 90-ből 5 (Írja be, hogy "5")\n 45-ből 6 (Írja be, hogy "6")\n Melyikkel kíván játszani? '))
    if kategoria ==5:
        nyertes = random.sample(range(1, 91), 5)
        szamok=input('Tegye meg tétjeit (5db számot szóközökkel válasszon el):').split()
        szamok = list(map(int, szamok))
        max_szam=90

    if kategoria == 6:
        nyertes = random.sample(range(1, 46), 6)
        szamok=input('Tegye meg tétjeit (6db számot szóközökkel válasszon el)').split()
        szamok = list(map(int, szamok))
        max_szam=45
    else:
        print('Nem létezik ilyen kategória.')

    for i in range(len(szamok)):
            if szamok[i] > max_szam:
                print("Nem adható meg ilyen szám!")

    talalat = len(set(nyertes) & set(szamok))
    print('Találatok:', talalat)
    nyeremeny=print(f'A nyereménye {talalat**2*1000}-Ft.')
    return nyertes, szamok
print(kategoria())
