


import random
word = random.choice(open('WordList.txt').read().split()).strip()
guess_count = 0

while guess_count < 7:
    guess = input("What is your guess? ")
    check_length = (len(guess)) == 5
#check_dictionary =     check dictionary here (optional for now)
    if check_length == True:
        guess_count += 1
        A_green = word[0] == guess[0]
        A_yellow = guess[0] in word
        if A_green is True:
            A = "Green"
            print(A)
        elif A_yellow == True:
            A = "Yellow"
            print("Yellow")
        else:
            print("Grey")
        B_green = word[1] == guess[1]
        B_yellow = guess[1] in word
        if B_green is True:
            B = "Green"
            print(B)
        elif B_yellow == True:
            B = "Yellow"
            print(B)
        else:
            print("Grey")
        C_green = word[2] == guess[2]
        C_yellow = guess[2] in word
        if C_green is True:
            C = "Green"
            print(C)
        elif C_yellow == True:
            C = "Yellow"
            print("Yellow")
        else:
            print("Grey")
        D_green = word[3] == guess[3]
        D_yellow = guess[3] in word
        if D_green is True:
            D = "Green"
            print(D)
        elif D_yellow == True:
            D = "Yellow"
            print(D)
        else:
            print("Grey")
        E_green = word[4] == guess[4]
        E_yellow = guess[4] in word
        if E_green is True:
            E = "Green"
            print(E)
        elif E_yellow == True:
            E = "Yellow"
            print("Yellow")
        else:
            print("Grey")
    #print(word) #troubleshooting
        if guess == word:
            print("Congrats you found the word! " + word)
    else:
        guess_check = False
        print("Sorry your guess needs five letters")
else:
    print("You have run out of guesses :( The word was " + word)
