#import numpy as np
#import random
import pprint as pprint


#create cube
white_face = ["White", "White", "White", "White", "White", "White", "White", "White", "White"]
green_face = ["Green", "Green", "Green", "Green", "Green", "Green", "Green", "Green", "Green"]
red_face = ["Red", "Red", "Red", "Red", "Red", "Red", "Red", "Red", "Red"]
blue_face = ["Blue", "Blue", "Blue", "Blue", "Blue", "Blue", "Blue", "Blue", "Blue", ]
orange_face = ["Orange", "Orange", "Orange", "Orange", "Orange", "Orange", "Orange", "Orange", "Orange", ]
yellow_face = ["Yellow", "Yellow", "Yellow", "Yellow", "Yellow", "Yellow", "Yellow", "Yellow", "Yellow", ]

def cube_vis():
    print(white_face[0] + white_face[1] + white_face[2])
    print(white_face[3] + white_face[4] + white_face[5])
    print(white_face[6] + white_face[7] + white_face[8])
    print(green_face[0] + green_face[1] + green_face[2] + "  " + red_face[0] + red_face[1] + red_face[2] + "  " + blue_face[0] + blue_face[1] + blue_face[2] + "  " + orange_face[0] + orange_face[1] + orange_face[2])
    print(green_face[3] + green_face[4] + green_face[5] + "  " + red_face[3] + red_face[4] + red_face[5] + "  " + blue_face[3] + blue_face[4] + blue_face[5] + "  " + orange_face[3] + orange_face[4] + orange_face[5])
    print(green_face[6] + green_face[7] + green_face[8] + "  " + red_face[6] + red_face[7] + red_face[8] + "  " + blue_face[6] + blue_face[7] + blue_face[8] + "  " + orange_face[6] + orange_face[7] + orange_face[8])
    print(yellow_face[0] + yellow_face[1] + yellow_face[2])
    print(yellow_face[3] + yellow_face[4] + yellow_face[5])
    print(yellow_face[6] + yellow_face[7] + yellow_face[8])





 # (Key: white top, red north, green east, orange south, blue west, yellow under)
 # If white is rotated clockwise red-> blue-> orange-> green rotate (a,b,c) are shifted
 # If green is rotated clockwise white-> orange-> yellow-> red (c,f,i) are shifted respectively
 # If blue is rotated clockwise white-> orange-> yellow-> red (a,d,g) are shifted respectively
 # If orange is rotated clockwise white-> green-> yellow-> blue (g,h,i) are shifted respectively
 # If red is rotated clockwise white-> blue-> yellow-> green (a,b,c) are shifted respectively
 # If yellow is rotated clockwise blue-> orange-> green-> red (g,h,i) are shifted respectively


#add anticlockwise X
#red rotate does not work X
#MUST FIX CUBE_VIS() BEFORE TESTING
#test all the rotates
#Check yellow is oriented correctly with clockwise and anticlockwise movement

def rotate_white_anticlockwise():
    white_face[0], white_face[1], white_face[2], white_face[3], white_face[5], white_face[6], white_face[7], white_face[8] = white_face[6], white_face[3], white_face[0], white_face[7], white_face[2], white_face[8], white_face[5], white_face[2]           #01234678 -->63072852 Anti clockwise face rotation
    red_face[0], red_face[1], red_face[2], blue_face[0], blue_face[1], blue_face[2], orange_face[0], orange_face[1], orange_face[2], green_face[0], green_face[1], green_face[2] = green_face[0], green_face[1], green_face[2], red_face[0], red_face[1], red_face[2], blue_face[0], blue_face[1], blue_face[2], orange_face[0], orange_face[1], orange_face[2]
def rotate_green_anticlockwise():
    green_face[0], green_face[1], green_face[2], green_face[3], green_face[5], green_face[6], green_face[7], green_face[8] = green_face[6], green_face[3], green_face[0], green_face[7], green_face[2], green_face[8], green_face[5], green_face[2]
    white_face[2], white_face[5], white_face[8], orange_face[2], orange_face[5], orange_face[8], yellow_face[2], yellow_face[5], yellow_face[8], red_face[2], red_face[5], red_face[8] = red_face[2], red_face[5], red_face[8], white_face[2], white_face[5], white_face[8], orange_face[2], orange_face[5], orange_face[8], yellow_face[2], yellow_face[5], yellow_face[8]
def rotate_blue_anticlockwise():
    blue_face[0], blue_face[1], blue_face[2], blue_face[3], blue_face[5], blue_face[6], blue_face[7], blue_face[8] = blue_face[6], blue_face[3], blue_face[0], blue_face[7], blue_face[2], blue_face[8], blue_face[5], blue_face[2]
    white_face[0], white_face[3], white_face[6], orange_face[0], orange_face[3], orange_face[6], yellow_face[0], yellow_face[3], yellow_face[6], red_face[0], red_face[3], red_face[6] = red_face[0], red_face[3], red_face[6], white_face[0], white_face[3], white_face[6], orange_face[0], orange_face[3], orange_face[6], yellow_face[0], yellow_face[3], yellow_face[6]         #a,d,g=0,3,6
def rotate_orange_anticlockwise():
    orange_face[0], orange_face[1], orange_face[2], orange_face[3], orange_face[5], orange_face[6], orange_face[7], orange_face[8] = orange_face[6], orange_face[3], orange_face[0], orange_face[7], orange_face[2], orange_face[8], orange_face[5], orange_face[2]
    white_face[6], white_face[7], white_face[8], green_face[6], green_face[7], green_face[8], yellow_face[6], yellow_face[7], yellow_face[8], blue_face[6], blue_face[7], blue_face[8] = blue_face[6], blue_face[7], blue_face[8], white_face[6], white_face[7], white_face[8], green_face[6], green_face[7], green_face[8], yellow_face[6], yellow_face[7], yellow_face[8]         #g,h,i=6,7,8
def rotate_red_anticlockwise():
    red_face[0], red_face[1], red_face[2], red_face[3], red_face[5], red_face[6], red_face[7], red_face[8] = red_face[6], red_face[3], red_face[0], red_face[7], red_face[2], red_face[8], red_face[5], red_face[2]
    white_face[0], white_face[1], white_face[2], blue_face[0], blue_face[3], blue_face[6],yellow_face[0], yellow_face[3], yellow_face[6], green_face[2], green_face[5], green_face[8] = green_face[2], green_face[5], green_face[8], white_face[0], white_face[1], white_face[2], blue_face[0], blue_face[3], blue_face[6],yellow_face[0], yellow_face[3], yellow_face[6]
def rotate_yellow_anticlockwise():
    yellow_face[0], yellow_face[1], yellow_face[2], yellow_face[3], yellow_face[5], yellow_face[6], yellow_face[7], yellow_face[8] = yellow_face[6], yellow_face[3], yellow_face[0], yellow_face[7], yellow_face[2], yellow_face[8], yellow_face[5], yellow_face[2]
    blue_face[6], blue_face[7], blue_face[8], orange_face[6], orange_face[7], orange_face[8], green_face[6], green_face[7], green_face[8], red_face[6], red_face[7], red_face[8] = red_face[6], red_face[7], red_face[8], blue_face[6], blue_face[7], blue_face[8], orange_face[6], orange_face[7], orange_face[8], green_face[6], green_face[7], green_face[8]


def rotate_white_clockwise():
    white_face[0], white_face[1], white_face[2], white_face[3], white_face[5], white_face[6], white_face[7], white_face[8] = white_face[2], white_face[5], white_face[8], white_face[1], white_face[7], white_face[0], white_face[3], white_face[6] #0,1,2,3,4,5,6,7-> 2,5,8,1,7,0,3,6
    red_face[0], red_face[1], red_face[2], blue_face[0], blue_face[1], blue_face[2], orange_face[0], orange_face[1], orange_face[2], green_face[0], green_face[1], green_face[2] = blue_face[0], blue_face[1], blue_face[2], orange_face[0], orange_face[1], orange_face[2], green_face[0], green_face[1], green_face[2], red_face[0], red_face[1], red_face[2]
def rotate_green_clockwise():
    green_face[0], green_face[1], green_face[2], green_face[3], green_face[5], green_face[6], green_face[7], green_face[8] = green_face[2], green_face[5], green_face[8], green_face[1], green_face[7], green_face[0], green_face[3], green_face[6]
    white_face[2], white_face[5], white_face[8], orange_face[2], orange_face[5], orange_face[8], yellow_face[2], yellow_face[5], yellow_face[8], red_face[2], red_face[5], red_face[8] = orange_face[2], orange_face[5], orange_face[8], yellow_face[2], yellow_face[5], yellow_face[8], red_face[2], red_face[5], red_face[8], white_face[2], white_face[5], white_face[8]
def rotate_blue_clockwise():
    blue_face[0], blue_face[1], blue_face[2], blue_face[3], blue_face[5], blue_face[6], blue_face[7], blue_face[8] = blue_face[2], blue_face[5], blue_face[8], blue_face[1], blue_face[7], blue_face[0], blue_face[3], blue_face[6]
    white_face[0], white_face[3], white_face[6], orange_face[0], orange_face[3], orange_face[6], yellow_face[0], yellow_face[3], yellow_face[6], red_face[0], red_face[3], red_face[6] = orange_face[0], orange_face[3], orange_face[6], yellow_face[0], yellow_face[3], yellow_face[6], red_face[0], red_face[3], red_face[6], white_face[0], white_face[3], white_face[6]
def rotate_orange_clockwise():
    orange_face[0], orange_face[1], orange_face[2], orange_face[3], orange_face[5], orange_face[6], orange_face[7], orange_face[8] = orange_face[2], orange_face[5], orange_face[8], orange_face[1], orange_face[7], orange_face[0], orange_face[3], orange_face[6]
    white_face[6], white_face[7], white_face[8], green_face[6], green_face[7], green_face[8], yellow_face[6], yellow_face[7], yellow_face[8], blue_face[6], blue_face[7], blue_face[8] = green_face[6], green_face[7], green_face[8], yellow_face[6], yellow_face[7], yellow_face[8], blue_face[6], blue_face[7], blue_face[8], white_face[6], white_face[7], white_face[8]
def rotate_red_clockwise():
    red_face[0], red_face[1], red_face[2], red_face[3], red_face[5], red_face[6], red_face[7], red_face[8] = red_face[2], red_face[5], red_face[8], red_face[1], red_face[7], red_face[0], red_face[3], red_face[6]
    white_face[0], white_face[1], white_face[2], blue_face[0], blue_face[3], blue_face[6],yellow_face[0], yellow_face[3], yellow_face[6], green_face[2], green_face[5], green_face[8] = blue_face[0], blue_face[3], blue_face[6],yellow_face[0], yellow_face[3], yellow_face[6], green_face[2], green_face[5], green_face[8], white_face[0], white_face[1], white_face[2]
def rotate_yellow_clockwise():
    yellow_face[0], yellow_face[1], yellow_face[2], yellow_face[3], yellow_face[5], yellow_face[6], yellow_face[7], yellow_face[8] = yellow_face[2], yellow_face[5], yellow_face[8], yellow_face[1], yellow_face[7], yellow_face[0], yellow_face[3], yellow_face[6]
    blue_face[6], blue_face[7], blue_face[8], orange_face[6], orange_face[7], orange_face[8], green_face[6], green_face[7], green_face[8], red_face[6], red_face[7], red_face[8] = orange_face[6], orange_face[7], orange_face[8], green_face[6], green_face[7], green_face[8], red_face[6], red_face[7], red_face[8], blue_face[6], blue_face[7], blue_face[8]


move = None
while move != "end":
    cube_vis()
    move = input("which face would you like to rotate?")
    if move == "white":
        rotate_white_anticlockwise()
    if move == "green":
        rotate_green_anticlockwise()
    if move == "red":
        rotate_red_anticlockwise()
    if move == "blue":
        rotate_blue_anticlockwise()
    if move == "orange":
        rotate_orange_anticlockwise()
    if move == "yellow":
        rotate_yellow_anticlockwise()
    if move == "cy":
        rotate_yellow_clockwise()
    if move == "cg": #clockwise green face is not working
        rotate_green_clockwise()
    if move == "cb":
        rotate_blue_clockwise()
    if move == "cr":
        rotate_red_clockwise()
    if move == "cw":
        rotate_white_clockwise()
    if move == "co":
        rotate_orange_clockwise()






