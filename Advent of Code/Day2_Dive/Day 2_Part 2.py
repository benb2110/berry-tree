#inputs = "forward", 5, "down", 5, "forward", 8, "up", 3, "down", 8, "forward", 2
inputs = open('Day 2_Dive_Inputs.txt').read().split()

direction = inputs[0:-1:2]
movement = inputs[1::2]
#print(direction)
#print(movement)

pos_horizontal = 0
pos_depth = 0
aim = 0

for i in range(len(direction)):
    if direction[i] == "forward":
        pos_horizontal += int(movement[i])
        pos_depth += aim * int(movement[i])
    elif direction[i] == "up":
        aim -= int(movement[i])
    elif direction[i] == "down":
        aim = int(aim) + int(movement[i])
    else:
        print("error")

print("horizontal_position: " + str(pos_horizontal))
print("depth_position: " + str(pos_depth))

coordinates = pos_horizontal*pos_depth
print("coordinates: " + str(coordinates))
