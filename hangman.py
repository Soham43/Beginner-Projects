import random
import time

print("\nWelcome to Hangman\n")
Name = input("Enter your name: ")
print("Best of luck " + Name + " Get ready")
time.sleep(2)
print("The Game is about to begin ≖‿≖")
time.sleep(2)

def Main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["January","motor","physics","phone","gaming","lamp",
                      "flexible","channel","python","programming","science"]
    
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_'*length
    already_guessed = []
    play_game = " "

    # Creating a loop to re-execute a the game when round ends

def Play_loop():
    global play_game
    play_game = input("Do you wish to play again? 乁(ツ)ㄏ y = yes , n = no\n")
    while play_game not in ["y","n","Y","N"]:
        play_game = input("Do you wish to play again? 乁(ツ)ㄏ y = yes , n = no\n")
    if play_game == "y":
        Main()
    elif play_game == "n":
        print("Thanks for playing " + Name + ", come back soon")
        exit()

    # initialise all conditions for Hangman

def Hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the hangman word:  " + display + " Enter you guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess.isdigit():
        print("Invalid input , try a letter\n")
        Hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + '_' + word[index + 1 :]
        display = display[:index] + guess + display[index + 1 :]
        print(display + "\n")
    elif guess in already_guessed:
        print("Try another letter\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("  ______  \n "
                  " |        \n "
                  " |        \n "
                  " |        \n "
                  " |        \n "
                  " |        \n "
                  " |        \n "
                  " |        \n "
                  "_|_\n ")
            print("Wrong guess " +str(limit-count) + " guess remaining\n")

        elif count == 2:
            time.sleep(1)
            print( "   ______   \n"
                   " |      |   \n"
                   " |      |   \n"
                   " |          \n"
                   " |         \n"
                   " |         \n"
                   " |         \n"
                   "_|_         \n")
            print("Wrong guess " + str(limit-count) + " guess remaining\n")

        elif count == 3:
            time.sleep(1)
            print( "   ______   \n"
                   " |      |   \n"
                   " |      |   \n"
                   " |      |    \n"
                   " |         \n"
                   " |         \n"
                   " |         \n"
                   "_|_         \n")
            print("Wrong guess " + str(limit-count) + " guess remaining\n")

        elif count == 4:
            time.sleep(1)
            print( "   ______   \n"
                   " |      |   \n"
                   " |      |   \n"
                   " |      |    \n"
                   " |      o   \n"
                   " |         \n"
                   " |         \n"
                   "_|_         \n")
            print("Wrong guess " + str(limit-count) + " last guess remaining (✦థ ｪ థ)\n")

        elif count == 5:
            time.sleep(1)
            print( "   ______   \n"
                   " |      |   \n"
                   " |      |   \n"
                   " |      |    \n"
                   " |      o   \n"
                   " |     /|\   \n"
                   " |     / \  \n"
                   "_|_         \n")
            print("Wrong guess you are hanged!!! ಠ⌣ಠ \n")
            print("The word was: ",already_guessed,word)
            Play_loop()

    if  word == '_'*length:
        print("Congrats you have guessed the word correctly (｡-_-｡ )人( ｡-_-｡)")
        Play_loop()

    elif count != limit:
        Hangman()

Main()

Hangman()