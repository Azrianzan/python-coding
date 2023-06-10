#Rock, Paper, Scissors game with Python
import random

gameOver = False
rpsList = ["rock", "paper", "scissors"]
compScore = 0
PlayerScore = 0

print("Welcome to the Rock, Paper, Scissors game")
print("player will fight against computer")

while not gameOver:
    print("a. Rock")
    print("b. Paper")
    print("c. Scissors")
    playerInput = input("choose one (example: a): ").lower()
    print("-" * 60)

    if playerInput == "a":
        print("Your choice is Rock")
        compInput = random.choice(rpsList)
        print(f"Computer choice is {compInput}")
    elif playerInput == "b":
        print("Your choice is Paper")
        compInput = random.choice(rpsList)
        print(f"Computer choice is {compInput}")
    elif playerInput == "c":
        print("Your choice is Scissors")
        compInput = random.choice(rpsList)
        print(f"Computer choice is {compInput}")
    else:
        #gameOver = True
        print("Please choose the provided option correctly")

    if playerInput == "a" and compInput == "rock":
        print("DRAW!!")
    elif playerInput == "a" and compInput == "paper":
        print("Computer Win!!")
        compScore += 1
    elif playerInput == "a" and compInput == "scissors":
        print("You win!!")
        PlayerScore += 1
    elif playerInput == "b" and compInput == "rock":
        print("You win!!")
        PlayerScore += 1
    elif playerInput == "b" and compInput == "paper":
        print("DRAW!!")
    elif playerInput == "b" and compInput == "scissors":
        print("Computer win!!")
        compScore += 1
    elif playerInput == "c" and compInput == "rock":
        print("Computer win!!")
        compScore += 1
    elif playerInput == "c" and compInput == "paper":
        print("You win!!")
        PlayerScore += 1
    elif playerInput == "c" and compInput == "scissors":
        print("DRAW!!")

    print("-" * 60)
    print(f"Your score : {PlayerScore}")
    print(f"Computer score : {compScore}")
    playAgain = False
    while playAgain == False:
        more = input("play the game again (y/n)? ").lower()
        if more == "y":
            playAgain = True
        elif more == "n":
            playAgain = True
            gameOver = True
            print("Thank you for playing this simple game")
        else:
            print("Please answer it correctly")
