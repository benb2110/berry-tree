Guide_Data = []

with open('Data.txt') as d: #importing data
    for data in d:
        Guide_Data.append(data.strip())
d.close()

print(Guide_Data)


def score_calc(data):
    score = 0
    for i in range(len(data)):
        if data[i][2] == 'Z':#Scissors 3 points
            temp = 3
            if data[i][0] == 'B': #Win 6 points
                score += temp + 6
            elif data[i][0] == 'C': #Draw 3 points
                score += temp + 3
            else: #Lose 0 Points
                score += temp
            temp = 0
        if data[i][2] == 'Y': #Paper 2 Points
            temp = 2
            if data[i][0] == 'A': #Win
                score += temp + 6
            elif data[i][0] == 'B': #Draw
                score += temp + 3
            else: #Lose
                score += temp
            temp = 0
        if data[i][2] == 'X': #Rock 1 Point
            temp = 1
            if data[i][0] == 'C': #Win
                score += temp + 6
            elif data[i][0] == 'A': #Draw
                score += temp + 3
            else: #Lose
                score += temp
            temp = 0
    return score

print(score_calc(Guide_Data))
