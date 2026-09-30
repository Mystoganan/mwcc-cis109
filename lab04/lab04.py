word_list = ["Hangout", "Refill", "Felid"]

import random

random_number = random.randint(0, len(word_list)-1) 

wrong_letters = []

if(random_number == 0):
    letters = ["_", "_", "_", "_", "_", "_", "_"]

elif(random_number == 1):
    letters = ["_", "_", "_", "_", "_", "_"]

elif(random_number == 2):
    letters = ["_", "_", "_", "_", "_"]

enter = "Press [Enter] to continue"

while(True):

    if(len(wrong_letters) == 0):
        hangman_visual = " "
    
    elif(len(wrong_letters) == 1):
        hangman_visual = """
+---+
|
|
|
|   
=======
    """
    elif(len(wrong_letters) == 2):
        hangman_visual = """
+---+
|   |
|
|
|   
=======
        """

    elif(len(wrong_letters) == 3):
        hangman_visual = """
+---+
|   |
|   0
|
|   
=======
        """

    elif(len(wrong_letters) == 4):
        hangman_visual = """
+---+
|   |
|   0
|   |
|   
=======
        """

    elif(len(wrong_letters) == 5):
        hangman_visual = """
+---+
|   |
|   0
|  /|\\ 
|
=======
    """

    elif(len(wrong_letters) == 6):
        hangman_visual = """
+---+
|   |
|   0
|  /|\\
|  / \\ 
=======
    """

    print(f"""
    Welcome to HANGMAN!

    {letters}
    {hangman_visual}
    Bad Guesses: {wrong_letters}
    """)

    #Game Fail
    if(len(wrong_letters) == 6):
        print("You Lose!")
        input(enter)
        break

    #Win Conditions
    
    #Word 1
    if(random_number == 0) and (letters[0] == "H") and (letters[1] == "a") and (letters[2] == "n")  and (letters[3] == "g") and (letters[4] == "o") and (letters[5] == "u") and (letters[6] == "t"):
        print("Congratulations! You Won\nThe word was Hangout")
        input(enter)
        break

    #Word 2
    if(random_number == 1) and (letters[0] == "R") and (letters[1] == "e") and (letters[2] == "f")  and (letters[3] == "i") and (letters[4] == "l") and (letters[5] == "l"):
        print("Congratulations! You Won\nThe word was Refill")
        input(enter)
        break

    #Word 3
    if(random_number == 2) and (letters[0] == "F") and (letters[1] == "e") and (letters[2] == "l")  and (letters[3] == "i") and (letters[4] == "d"):
        print("Congratulations! You Won\nThe word was Felid")
        input(enter)
        break

    guess = input("    Guess a Letter: ")

    #Invalid Answers
    if(len(guess) > 1):
        print("Hey! That's illegal! One letter at a time!\nTry Again")
        input(enter)
        continue

    elif(len(guess) < 1):
        print("Hey... You gotta guess something...\nTry again")
        input(enter)
        continue

    elif not (guess.isalpha()):
        print("Hey! That's a number! I said letter!\n")
        input(enter)
        continue

    elif(guess in wrong_letters) or (guess in letters):
        print("Hey! You guessed that already!")
        input(enter)
        continue

    #Word 1 (Hangout)
    if(random_number == 0) and (guess == "h") or (guess == "H"):
        print("Correct Guess!")
        input(enter)
        letters[0] = "H"
        continue
    
    elif(random_number == 0) and (guess == "a") or (guess == "A"):
        print("Correct Guess!")
        input(enter)
        letters[1] = "a"
        continue
    
    elif(random_number == 0) and (guess == "n") or (guess == "N"):
        print("Correct Guess!")
        input(enter)
        letters[2] = "n"
        continue
    
    elif(random_number == 0) and (guess == "g") or (guess == "G"):
        print("Correct Guess!")
        input(enter)
        letters[3] = "g"
        continue

    elif(random_number == 0) and (guess == "o") or (guess == "O"):
        print("Correct Guess!")
        input(enter)
        letters[4] = "o"
        continue
    
    elif(random_number == 0) and (guess == "u") or (guess == "U"):
        print("Correct Guess!")
        input(enter)
        letters[5] = "u"
        continue

    elif(random_number == 0) and (guess == "t") or (guess == "T"):
        print("Correct Guess!")
        input(enter)
        letters[6] = "t"
        continue

    #Word 2 (Refilll)
    if(random_number == 1) and (guess == "r") or (guess == "R"):
        print("Correct Guess!")
        input(enter)
        letters[0] = "R"
        continue

    elif(random_number == 1) and (guess == "e") or (guess == "E"):
        print("Correct Guess!")
        input(enter)
        letters[1] = "e"
        continue
    
    elif(random_number == 1) and (guess == "f") or (guess == "F"):
        print("Correct Guess!")
        input(enter)
        letters[2] = "f"
        continue
    
    elif(random_number == 1) and (guess == "i") or (guess == "I"):
        print("Correct Guess!")
        input(enter)
        letters[3] = "i"
        continue

    elif(random_number == 1) and (guess == "l") or (guess == "L"):
        print("Correct Guess!")
        input(enter)
        letters[4] = "l"
        letters[5] = "l"
        continue

    #Word 3 (Felid)
    if(random_number == 2) and (guess == "f") or (guess == "F"):
        print("Correct Guess!")
        input(enter)
        letters[0] = "F"
        continue

    elif(random_number == 2) and (guess == "e") or (guess == "E"):
        print("Correct Guess!")
        input(enter)
        letters[1] = "e"
        continue

    elif(random_number == 2) and (guess == "l") or (guess == "L"):
        print("Correct Guess!")
        input(enter)
        letters[2] = "l"
        continue

    elif(random_number == 2) and (guess == "i") or (guess == "I"):
        print("Correct Guess!")
        input(enter)
        letters[3] = "i"
        continue

    elif(random_number == 2) and (guess == "d") or (guess == "D"):
        print("Correct Guess!")
        input(enter)
        letters[4] = "d"
        continue

    #Wrong Answer
    else:
        print("That letter doesn't exist in this word!")
        input(enter)
        wrong_letters.append(guess)
        continue