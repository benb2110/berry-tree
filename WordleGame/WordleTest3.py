#to-do
#Statistics
#Break up length and dictionary check X
#Double yellow hint mechanic breaks in the event that the second guess letter is Green. Fix?
#UI

import random
word = random.choice(open('wordle-answers-alphabetical.txt').read().split()).strip()
dictionary = str((open('wordle-dictionary.txt').read().split()))
guess_count = 0

while guess_count < 6:
    guess = input("What is your guess? ").lower()
    check_length = (len(guess)) == 5
    dictionary_check = guess in dictionary
    if check_length is True: #checking length and dictionary for valid guess
        if dictionary_check is True:
            guess_count += 1
            #checking first letter in guess against the word
            a_green = guess[0] == word[0]
            a_yellow = guess[0] in word
            if a_green is True:
                A = "Green"
            elif a_yellow is True:
                A = "Yellow"
            else:
                A = "Grey"
            #checking second letter in guess against the word
            b_green = guess[1] == word[1] #is the guess letter the same as the word letter
            b_yellow = guess[1] in word #is the guess letter in the word somewhere
            guess_double = guess[1] == guess[:1]  #Has guess letter appeared in the guess already
            double_check = sum(char == guess[1] for char in word) #Does the guess letter appear in the word twice
            word_double = double_check > 1
            if b_green is True:
                B = "Green"
            elif b_yellow is True:
                if word_double is False and guess_double is True:
                    B = "Grey"
                else:
                    B = "Yellow"
            else:
                B = "Grey"
            #checking third letter in guess against the word
            c_green = guess[2] == word[2]
            c_yellow = guess[2] in word
            guess_double = guess[2] in guess[:2]
            double_check = sum(char == guess[2] for char in word)
            word_double = double_check > 1
            if c_green is True:
                C = "Green"
            elif c_yellow is True:
                if word_double is False and guess_double is True:
                    C = "Grey"
                else:
                    C = "Yellow"
            else:
                C = "Grey"
            #checking fourth letter in guess against the word
            d_green = guess[3] == word[3]
            d_yellow = guess[3] in word
            guess_double = guess[3] in guess[:3]
            double_check = sum(char == guess[3] for char in word)
            word_double = double_check > 1
            if d_green is True:
                D = "Green"
            elif d_yellow is True:
                if word_double is False and guess_double is True:
                    D = "Grey"
                else:
                    D = "Yellow"
            else:
                D = "Grey"
            #checking fifth letter in guess against the word
            e_green = guess[4] == word[4]
            e_yellow = guess[4] in word
            guess_double = guess[4] in guess[:4]
            double_check = sum(char == guess[4] for char in word)
            word_double = double_check > 1
            if e_green is True:
                E = "Green"
            elif e_yellow is True:
                if word_double is False and guess_double is True:
                    E = "Grey"
                else:
                    E = "Yellow"
            else:
                E = "Grey"
            #printing feedback to the user
            print(A,  B,  C,  D,  E,)
            print("Guess " + str(guess_count) + "/6")
            if guess == word:
                print("Congrats you found the word! " + word.upper())
                #Write guess_count to file
                #Print Statistics
                break
        else:
            print("Sorry that guess is not a real word. Try again.")
            print("Guess " + str(guess_count) + "/6")
    else:
        print("Sorry your guess needs to contain five letters. Try again. ")
        print("Guess " + str(guess_count) + "/6")
else:
    print("You have run out of guesses :( The word was " + word.upper())




