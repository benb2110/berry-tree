
outcome = ["Grey", "Grey", "Grey", "Grey", "Grey"]

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
            for i in range(0, 5):
                if word[i] == guess[i]:
                    outcome[i] = "Green"
                else:
                    for j in range(0, 5):
                        if word[i] == guess[j] and outcome[j] == "Grey" and word[j] != guess[j]:
                            outcome[j] = "Yellow"
                            break
            print(outcome)
            print(word)
            print("Guess " + str(guess_count) + "/6")
            if guess == word:
                print("Congrats you found the word! " + word.upper())
                with open('statistics.txt', 'a') as stats:
                    stats.write(str(guess_count))
                    stats.write('\n')
                    stats.close()
                with open('statistics.txt', 'r') as stats:
                    wordle_score = stats.read()
                    for i in range(1, 7):
                        print(str(i) + ': ' + str(wordle_score.count(str(i))))
                    stats.close()
                break
        else:
            print("Sorry that guess is not a real word. Try again.")
            print("Guess " + str(guess_count) + "/6")
    else:
        print("Sorry your guess needs to contain five letters. Try again. ")
        print("Guess " + str(guess_count) + "/6")
else:
    print("You have run out of guesses :( The word was " + word.upper())

