instructions = []

with open('Test Data.txt') as d: #importing data
    for line in d:
        instructions.append(line.split())
d.close()

sprite_pos = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']


#init CRT display
CRT = []
for l in range(6):
    line = []
    for i in range(40):
        line.append('.')
    CRT.append(line)
#print(CRT)


def sprite_update(x):
    global sprite_pos, CRT
    sprite_pos = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    sprite_pos[x] = '#'
    sprite_pos[x-1] = '#'
    sprite_pos[x+1] = '#'
    #print(sprite_pos)


def draw_cycle(step, cycle):
    global sprite_pos, CRT
    if sprite_pos[cycle-1] == '#':
        CRT[step][cycle-1] = '#'


def operations(inputs):
    x = 1
    cycle = 1
    step = 0
    for i in range(len(inputs)):
        if cycle == 40:
            print(CRT[step])
            step += 1
            cycle -= 40
        sprite_update(x)     #update sprite position
        if str(inputs[i][0]) == 'addx':
            for loop in range(2):
                draw_cycle(step, cycle)   #draw sprite
                cycle += 1
                if cycle == 40:
                    print(CRT[step])
                    step += 1
                    cycle -= 40
            x += int(inputs[i][1])
        else:
            draw_cycle(step, cycle)     #draw sprite
            cycle += 1



operations(instructions)

