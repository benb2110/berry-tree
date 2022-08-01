#import turtle
#
#bob = turtle.Turtle()
#print(bob)
#turtle.mainloop()

#print("{0:s}\n?????\n".format("This is an underlined headline.", "_"))

class Animal(object):
    def __init__(self, name, weight, contact_info):
        self.name = name
        self.weight = weight
        self.contact_info = contact_info

    def speak(self):
        print("...")

class Mammal(Animal):
    def speak(self, sound='Grunt'):
        print(sound)
    has_fur = False
