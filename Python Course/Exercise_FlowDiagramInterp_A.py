#Greater Number Printer
a = input("Input a... ")
b = input("Input b... ")
c = input("Input c... ")

if a > b:
    if a > c:
        print("A is the greatest number (" + str(a) + ")")
    else:
        print("C is the greatest number (" + str(c) + ")")
else:
    if b > c:
        print("B is the greatest number (" + str(b) + ")")
    else:
        print("C is the greatest number (" + str(c) + ")")
