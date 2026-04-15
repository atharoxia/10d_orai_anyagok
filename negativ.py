import random


def negativ(szam):
    if szam < 0:
        return True
    else:
        return False

db = 0
for i in range(100):
    a = random.randint(-50, 50)
    if negativ(a) == True:
        db += 1

print(f"A számok között {db} negatív szerepel.")


