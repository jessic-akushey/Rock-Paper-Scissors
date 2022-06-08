import random

print("Lets play Rock, Paper, Scissors")
opt1 = ["R", "P", "S"]
opt = {"R": "Rock", "P": "Paper", "S": "Scissors"}

choic = input("Pick your choice (R, P, S): ").upper()
com = random.choice(opt1)

while choic not in opt or choic == com:
    com = random.choice(opt1)
    if choic not in opt:
        # com = random.choice(opt1)
        choic = input("Invalid input. Try again: ").upper()
    elif choic == com:
        # com = random.choice(opt1)
        print("Player (" + opt[choic] + "): CPU (" + opt[com] + ")")
        choic = input("Its a tie. Try again: ").upper()

if choic == "R" and com == "S":
    print("Player (" + opt[choic] + "): CPU (" + opt[com] + ")")
    print("Player wins")
elif choic == "P" and com == "R":
    print("Player (" + opt[choic] + "): CPU (" + opt[com] + ")")
    print("Player Wins")
elif choic == "S" and com == "P":
    print("Player (" + opt[choic] + "): CPU (" + opt[com] + ")")
    print("Player Wins")
else:
    print("Player (" + opt[choic] + "): CPU (" + opt[com] + ")")
    print("Computer Wins")
