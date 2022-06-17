import datetime
#t0 = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
#d = datetime.datetime.now().strftime("Date: %d")
x = datetime.datetime.now()
print(x)
has_walked = False
walk_time = "11-06-2022 16:08"

input_has_walked = input("Dog has walked?") #Boolean
if input_has_walked == "Yes":
    has_walked = True
    walk_time = datetime.datetime.now().strftime("%d-%m-%Y %H:/%p")


while has_walked is True:
    t0 = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
    if t0 >= walk_time + "14 hours":
        if has_walked is True:
            has_walked = False
