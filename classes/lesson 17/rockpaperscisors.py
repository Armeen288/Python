import random
while True:
    useraction = input("Enter a choice(rock, paper, scissors):  ")
    possibleactions = ["rock" , "paper" , "scissors"]
    computeraction = random.choice(possibleactions)
    print(f"\nYou chose {useraction}, computer chose {computeraction}.\n")
    if useraction == computeraction:
        print("Both Players selected {useraction}. Its a tie!")
    elif useraction == "rock":
        if computeraction == "scissors":
            print("Rock smashes scissors!! you win!")
        else:
            print("paper covers rock! you lose.")
    elif useraction=="paper":
        if computeraction=="rock":
            print("paper covers rock! you win!")
        else:
            print("scissors cuts paper! you lose.")
    elif useraction=="scissors":
        if computeraction == "paper":
            print("scissors cuts paper! you win!")
        else:
            print("rock smashes scissors! you lose.")
            playagain = input("Play again? (y/n):")
            if playagain != "y":
                break