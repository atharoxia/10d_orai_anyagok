print("WELCOME TO ROCK-PAPER-SCISSORS 3000!")
jatekos = input("CHOOSE YOUR DESTINY! ROCK/PAPER/SCISSORS: ")
jatekos = jatekos.lower()

if jatekos != "rock" and jatekos != "paper" and jatekos != "scissors":
    print("INVALID CHOICE!")
else:
    import random
    sors = random.randint(1, 3)
    if sors == 1:
        szgep = "rock"
    elif sors == 2:
        szgep = "paper"
    else:
        szgep = "scissors"

    print(f"The computer chooses {szgep}!")

    if jatekos == szgep:
        print("DRAW!")
    elif jatekos == "rock" and szgep == "scissors":
        print("YOU WIN!")
    elif jatekos == "paper" and szgep == "rock":
        print("YOU WIN!")
    elif jatekos == "scissors" and szgep == "paper":
        print("YOU WIN!")
    else:
        print("COMPUTER WINS! FATALITY!")


