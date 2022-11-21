# Emanuel Ramos
# 11/15/2022
#
# Description: Draw 5 perfect squares within each other with the length provided by the user

import turtle


def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    # draw the first square
    for i in range(4):
        t.forward(sz)
        t.left(90)
    # go to starting position of second square
    t.penup()
    t.goto(sz / 10, sz / 10)
    t.pendown()

    # draw the second square
    for i in range(4):
        t.forward(sz - (sz / 10 * 2))
        t.left(90)
    # go to starting position of third square
    t.penup()
    t.goto(sz / 10 * 2, sz / 10 * 2)
    t.pendown()

    # draw the third square
    for i in range(4):
        t.forward(sz - (sz / 10 * 4))
        t.left(90)
    # go to starting position of fourth square
    t.penup()
    t.goto(sz / 10 * 3, sz / 10 * 3)
    t.pendown()

    # draw fourth square
    for i in range(4):
        t.forward(sz - (sz / 10 * 6))
        t.left(90)
    # go to starting position of fifth square
    t.penup()
    t.goto(sz / 10 * 4, sz / 10 * 4)
    t.pendown()

    # draw fifth square
    for i in range(4):
        t.forward(sz - (sz / 10 * 8))
        t.left(90)
    # return turtle marker to starting position
    t.penup()
    t.goto(0, 0)


size = int(input("give me a number between 100 and 300:"))
wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")
alex.shape("turtle")
alex.speed(3)
drawSquare(alex, size)

wn.exitonclick()
