#

#Create Rubix Cube Array X
#Create rotating algo X
#Randomize cube algo
#Rubix cube auto-solving algo
#interesting text visualisation of cube faces

#Rubix Cube Array Ideas
 #  [1a(w), 1b(w), 1c(w)]
 #  [1d(w), 1e(w), 1f(w)]
 #  [1g(w), 1h(w), 1i(w)]
 #
 #  [2a(r), 2b(r), 2c(r)][3a(b), 3b(b), 3c(b)][4a(o), 4b(o), 4c(o)][5a(g), 5b(g), 5c(g)]
 #  [2d(r), 2e(r), 2f(r)][3d(b), 3e(b), 3f(b)][4d(o), 4e(o), 4f(o)][5d(g), 5e(g), 5f(g)]
 #  [2g(r), 2h(r), 2i(r)][3g(b), 3h(b), 3i(b)][4g(o), 4h(o), 4i(o)][5g(g), 5h(g), 5i(g)]
 #
 #  [6a(y), 6b(y), 6c(y)]
 #  [6d(y), 6e(y), 6f(y)]
 #  [6g(y), 6h(y), 6i(y)]
 #
 # (Key: white top, red north, green east, orange south, blue west, yellow under)
 # If white is rotated clockwise red-> blue-> orange-> green rotate (a,b,c) are shifted
 # If green is rotated clockwise white-> orange-> yellow-> red (c,f,i) are shifted respectively
 # If blue is rotated clockwise white-> orange-> yellow-> red (a,d,g) are shifted respectively
 # If orange is rotated clockwise white-> green-> yellow-> blue (g,h,i) are shifted respectively
 # If red is rotated clockwise white-> blue-> yellow-> green (a,b,c) are shifted respectively
 # If yellow is rotated clockwise blue-> orange-> green-> red (g,h,i) are shifted respectively
 #
 # Each position on the cube(6c, 3f, 4g) will have a state(White, Green, Red, Blue, Orange, Yellow)
 #
 #Rotation algorythim
 # def rotate_red_clockwise
 #        1abc, 2abc, 3abc, 4abc, = 2abc, 3abc, 4abc, 1abc   #method one re-order list
 #
 #
 #Randomizer algo
 #create random string of 20 numbers from 0-11
 #map each number to a rotation function
 #
 #
 #
 #
 #
 #
 #
 #
 #
 #
import numpy as np

# swaps
data = np.random.random(4)
print(data)
data[0], data[1], data[2], data[3] = data[3], data[0], data[1], data[2]
print(data)
