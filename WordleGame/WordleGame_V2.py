import random

word = random.choice(open('wordle-answers-alphabetical.txt').read().split()).strip()
dictionary = str((open('wordle-dictionary.txt').read().split()))

guess_count = 0


def word_checker(guess):  #inputs guess and checks it against the word to output clues
    answer = ['Grey', 'Grey', 'Grey', 'Grey', 'Grey']
    for i in range(5):
        for j in range(5):
            if word[i] == guess[j] and answer[j] == 'Grey':
                answer[j] = 'Yellow'
                break
        if word[i] == guess[i]:
            answer[i] = 'Green'
    return answer


while guess_count < 6:
    guess = input("What is your guess? ").lower()
    check_length = (len(guess)) == 5
    dictionary_check = guess in dictionary #checks if the word is valid
    if check_length is True: #checking length and dictionary for valid guess
        if dictionary_check is True:
            guess_count += 1
            result = word_checker(guess)
            print(result)
            print("Guess " + str(guess_count) + "/6")
            if result == ['Green', 'Green', 'Green', 'Green', 'Green']:
                print("Congrats you found the word! " + word.upper())
            #saving guess count to file and printing statistics
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


