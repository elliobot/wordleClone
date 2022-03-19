import random

#variables to store the count and secret word
totalWords = 0
chosenWord = ""

listName="listofwords.txt"

#defining the colours
greenLetter = "\033[1;37;42m"
yellowLetter = "\033[1;30;43m"
greyLetter = "\033[1;30;47m"
blackLetter = "\033[0;30;41m"
redLetter = "\033[1;30;41m"

#keyboard layout
keyboard = "qwertyuiop\nasdfghjkl\nzxcvbnm"

#open the list
wordList = open(listName, "r")

#empty list to store user guesses
guesslist = ["", "", "", "", ""]

#counting the amm of words
for line in wordList:
    totalWords += 1

#select a random index of this list
wordNum = random.randint(0, totalWords)

wordList = open(listName, "r")

#refreshes the keyboard output with the key colours
def keyboardUpdate():
    for k in keyboard:
        guessed = 0
        if k in greenGuessed:
            guessed = 1
        elif k in yellowGuessed:
            guessed = 2
        elif k in wrongGuessed:
            guessed = 3
        else:
            guessed = 0

        if guessed == 1:
            print(greenLetter + k, end="")
        elif guessed == 2:
            print(yellowLetter + k, end="")
        elif guessed == 3:
            print(blackLetter + k, end="")
        else:
            print(greyLetter + k, end="")

#look for the selected word in the list
browsenum = 0
for line in wordList:
    if browsenum == wordNum:
        chosenWord = line.lower()
    browsenum += 1
wordList.close()

#the values that track the current checked letter
word1Count = 0
word2Count = 0

#counting the green, yellow and wrong letters
correctLetters = 0
closeLetters = 0
wrongLetters = 0

#counts the numbers of correct letters
progress = 0

#track the current guess count
guesses = 0
lives = 5
#empty lists that add the new letter guesses
greenGuessed = ""
yellowGuessed = ""
wrongGuessed = ""

#variable that stores the user's guess
playerGuess = ""

#Prints the current life count
print("\033[0;30;41mLIVES:", lives, "\033[1;37;40m")

#while the letters arent guessed and the player has not made 5 guesses
while progress != 5 and lives != 0:
    #take the user's guess
    playerGuess = input("\n\033[1;37;40m What is your guess?\n")
    #while the guess is not 5 letters long, take again
    while len(playerGuess) != 5:
        playerGuess = input("\n\033[1;37;40m Please use a 5 letter word\n")
    #reset the correct letters in the current guess
    progress = 0
    word1Count = 0

    #for every letter in the player guess:
    for x in playerGuess:
        #reset the last word's checks
        word2Count = 0
        correctLetters = 0
        closeLetters = 0
        wrongLetters = 0

        #for every letter in the correct word
        for y in chosenWord:
            #check if the location and char is correct
            if x == y and word1Count == word2Count:
                correctLetters += 1
                progress += 1
                #if not found before, add to correct list
                if x not in greenGuessed:
                    greenGuessed += x
            elif x == y and word1Count != word2Count:
                closeLetters += 1
                if x not in yellowGuessed:
                    yellowGuessed += x
            else:
                wrongLetters += 1
                if x not in wrongGuessed:
                    wrongGuessed += x
            word2Count += 1

        if correctLetters > 0:
            guesslist[guesses] += greenLetter + x
        elif closeLetters > 0:
            guesslist[guesses] += yellowLetter + x

        else:
            guesslist[guesses] += greyLetter + x
        word1Count += 1
    print("\033[1;37;40m\n" * 10)
    if progress != 5:
      lives -= 1

    print("\033[0;30;41mLIVES:", lives, "\033[1;37;40m")
    for x in range(guesses+1):
        print("\033[1;37;40m")
        print(guesslist[x], end="")
        print("\033[1;37;40m", end="")

    print("\033[1;37;40m\n")
    keyboardUpdate()
    print("\033[1;37;40m\n")
    guesses +=1

if guesses < 6 and progress == 5:
    print(greenLetter + "YOU GOT IT, THE WORD WAS", chosenWord.upper())
else:
    print(redLetter + "GAME OVER. THE WORD WAS", chosenWord.upper())
