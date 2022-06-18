#this is the statistics module
#We need to
#At the end of a game take "guess_count" and write to .txt file
#Organise the data and display to user after the game

from collections import Counter
score = input("Score ")
with open('statistics.txt', 'a') as stats:
    stats.write(score)
    stats.write('\n')
    stats.close()

with open('statistics.txt', 'r') as stats:
    wordle_score = stats.read()
    for i in range (1, 7):
        print(str(i) + ': ' + str(wordle_score.count(str(i))))
    stats.close()
#print(wordle_score)
