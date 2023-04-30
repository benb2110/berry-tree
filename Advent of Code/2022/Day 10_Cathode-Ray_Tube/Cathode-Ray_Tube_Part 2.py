instructions = []

with open('Test Data.txt') as d: #importing data
    for line in d:
        instructions.append(line.split())
d.close()

signal_sums = 0
ref = 20

sprite_pos = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']

#init CRT display
CRT = []
for l in range(6):
    line = []
    for i in range(40):
        line.append('.')
    CRT.append(line)
print(CRT)


def sprite_update(x):
    global sprite_pos, CRT
    sprite_pos = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    sprite_pos[x] = '#'
    sprite_pos[x-1] = '#'
    sprite_pos[x+1] = '#'


def draw_cycle(step, cycle):
    global sprite_pos, CRT
    if sprite_pos[cycle] == '#':
        CRT[step][cycle] = '#'


def operations(inputs):
    x = 1
    cycle = 0
    step = 0
    for i in range(len(inputs)):
        if cycle == 39:
            step += 1
            cycle -= 39
        sprite_update(x)    #update sprite position
        if str(inputs[i][0]) == 'addx':
            for loop in range(2):
                sprite_update(x) #possibly redundant
                draw_cycle(step, cycle)   #draw sprite
                cycle += 1
            x += int(inputs[i][1])
        else:
            draw_cycle(step, cycle)     #draw sprite
            cycle += 1



operations(instructions)
#print(signal_sums)
