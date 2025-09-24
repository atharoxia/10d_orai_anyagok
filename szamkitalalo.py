e = 1 #intervallum első eleme
u = 1000 #intervallum utolsó eleme
k = (e + u) // 2 #intervallum középső eleme

print("Welcome to Mind-Reader 5000!")
print(f"Think of a number between {e} and {u}.")
while True:
    valasz = input(f"Is your number {k}? (y/n) ")
    if valasz == "y" or valasz == "Y" or valasz == "yes":
        