



#Project 4


!pip install colorama
from colorama import Fore, Back, Style




#Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False):

  # If it's not in the word, display it with a red background
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")






#Display a guess, where each letter is color-coded by it's accuracy


def printGuessAccuracy(guess, actual):


  # Loop through each index/position
  for index in range(0, 6):



    # Grab the letter from the guess
    letter = guess[index]

    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if (letter in actual) :


      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
      if(letter == actual[index]):

        # Then print it out with a green background
        printColorfulLetter(letter, True, True)

      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
      else:

        # ...so we'll print it out with a yellow background
        printColorfulLetter(letter, True, False)
    # ...but if the letter is not in the word at all...
    else:
      # ...print it out with a red background
      printColorfulLetter(letter, False, False)

    # Don't worry about the line of code below, it works. It just handles the transition between colors
    print(Style.RESET_ALL + " ", end="")










#Part 3 - Function that takes in a six-lettered word from the user

def GetSixLetterInput():
    notSixLetters = True
    while notSixLetters:
        guess = input("Enter a six-letter word: ")
        guess = guess.lower()
        if (len(guess) != 6):
            print("You did not enter a six character word, please try again. ")
            continue
        for letter in guess:
            if letter.isdigit() == True:
              print("You did not enter a six character word, please try again")
              break
        else:
            notSixLetters = False
    return guess







### Main Program ###

#Prompt user with game:

print("WELCOME TO WORD PLAY!")
print("=" * 16)
print("You have five tries to get the word correct")
print("The word is SIX CHARACTERS long, and you must enter a guess of this length")
print("Guesses should comprise only of letters and NOT numbers")
print("If a letter is in the correct place, it will be green")
print("If a letter is in the word but NOT in the correct place, it will be yellow")
print("If the letter is NOT in the word, it will be red")
print("")
print("")

#back-end secret answer, known as "acutal", the developer should ONLY CHANGE THIS VALUE when running the game:

actual = "COOKIE"

#standardizes the secret answer to lowercase as all user guesses are also standardized to lower case. This eliminates unintended case-sensitive discrepancies between the user guess and the actual world.

actual = actual.lower()


# Game logic:


for i in range(5):
  guess = GetSixLetterInput()
  printGuessAccuracy(guess, actual)



  #Create the win condition and advise user they won, if they guess the secret number.
  if guess == actual:
    print("Congratulations, You guessed the word, You won!")
    break

  #Create the loss condition, where the user has used up all five of their guesses (i = 4), and never guessed the actual word.
  elif (i == 4) and (guess != actual):
    print("\nYou failed to correctly guess the word in five tries. Better luck next time!")

print("The End!")
