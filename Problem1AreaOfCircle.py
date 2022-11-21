# Emanuel Ramos
# 11/15/2022
#
# Description: make a function that calculates the area of a circle when given the radius

import math


# defining a function called areaOfCircle()
def areaOfCircle(r):
    # area formula
    a = math.pi * (r ** 2)
    # print the output of the area formula
    print(a)


# calling the function so it runs the code within it
areaOfCircle(10)  # <-- change input to radius length

# ask for input and place it within the called function
r = int(input("What is the radius of the circle?\n"))
areaOfCircle(r)