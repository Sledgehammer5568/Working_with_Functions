# Emanuel Ramos
# 11/15/2022
#
# Description: checks if a number that is inputted is within a range of numbers or if it is outside the range

# make a function called Check_Range(number)
def check_range(input_number):  # <-- number is the only input needed for this function
    # check if number is in the range of 1 - 10
    if 1 <= input_number <= 10:  # <-- range can be changed to anything here
        # print out True if number is within range
        print(True)
    # if number isn't within range than it is outside the range
    else:
        # print out False if number is not within range
        print(False)


# make the variable number == input
number = int(input("What is your number?\n"))
# assign input into created function
check_range(number)

# the function can be used either with the input or by using it like a normal function
# by writing Check_Range(#) and write any number where # is written
# Check_Range(20)  # if you uncomment this line it should print out False since you gave the function an input of 20
