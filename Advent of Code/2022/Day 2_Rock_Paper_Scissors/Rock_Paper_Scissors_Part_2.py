# X Lose, Y Draw, Z Win
#1 rock 2 paper 3 scissors
Guide_Data = []

with open('Data.txt') as d: #importing data
    for data in d:
        Guide_Data.append(data.strip())
d.close()

print(Guide_Data)

def score_calc(data):
    score = 0
    for i in range(len(data)):
        if data[i][0] == 'A': #If Rock
            if data[i][2] == 'X': #Lose Scissors 3+0
                score += 3
            elif data[i][2] == 'Y': #Draw Rock 1+3
                score += 4
            else:               #Win Paper 2+6
                score += 8
        if data[i][0] == 'B': #Paper
            if data[i][2] == 'X': #Lose Rock 1+0
                score += 1
            elif data[i][2] == 'Y': #Draw Paper 2+3
                score += 5
            else:
                score += 9
        if data[i][0] == 'C': #Scissors
            if data[i][2] == 'X': #Lose Paper 2+0
                score += 2
            elif data[i][2] == 'Y': #Draw Scissors 3+3
                score += 6
            else:
                score += 7
    return score

print(score_calc(Guide_Data))
