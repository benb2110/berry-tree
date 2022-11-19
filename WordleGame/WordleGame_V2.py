word = 'abbey'
guess = input("Guess:  ")


def word_checker(guess):
    answer = ['Grey', 'Grey', 'Grey', 'Grey', 'Grey']
    for i in range(5):
        for j in range(5):
            if word[i] == guess[j] and answer[j] == 'Grey':
                answer[j] = 'Yellow'
                break
        if word[i] == guess[i]:
            answer[i] = 'Green'
    return answer


print(word_checker(guess))
