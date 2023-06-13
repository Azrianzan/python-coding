import random

# create a greeting
print("Welcome to Hangman!")
print("You need to guess all letters in a word")
print("You have 5 guesses (hearts)")
print("Good luck!")

# create your word list
words = ["hacker", "bounty", "coding", "random"]
# randomly choose a word from the list you have created
# create an empty list
# for each letter in the secretWord add a "_" that will be
#   printed to the console
# Example if the word is hacker "_", "_", "_", "_", "_", "_"
secretWord = random.choice(words)
displayWord = []
for letter in secretWord:
    displayWord += "_"
print(displayWord)

# use while loop so your game keeps going
# until the word has been guessed

# you can put the input inside the while loop
#   so this won't be an infinite loop and you need to input
#   new letter to run the loop again
# loop through each of the letters in the chosen word
# if the letter is in the word, replace the "_" with the letter
# it should be look like this "_", "a", "_", "_", "_", "_"
gameOver = False
hearts = 5

while not gameOver:
    guess = input("Guess a letter! ").lower()
    for position in range(len(secretWord)):
        letter = secretWord[position]
        if letter == guess:
            displayWord[position] = letter
    # you can make the guesser have 5 guesses (hearts)
    if guess not in secretWord:
        hearts -= 1
        print("Wrong guess! You only have " + str(hearts) + " heart(s) left")
    if hearts == 0:
        gameOver = True
        print("You lose! You only have 5 guesses for wrong letter")
        print("And you've failed to guess all letter in the word")
    print(displayWord)

    # finish the game after all the letters have been guessed
    if "_" not in displayWord:
        gameOver = True
        print("You win the game!")
        print("The word is " + str(displayWord))





