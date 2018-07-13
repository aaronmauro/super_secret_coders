from turtle import *
from random import randint

def cross():
    shape("turtle")
    color("green", "yellow")
    for number in range(0,4):
        for i in range(0,3):
            forward(100)
            right(90)
        left(180)

def poly(n_sides):
    shape("turtle")
    color("green", "red")
    begin_fill()
    for number in range(0, n_sides):
            forward(100)
            right(360 / n_sides)
    end_fill()

def shell_advanced(size):
    shape("turtle")
    color("blue")
    for i in range(0, size):
        forward(20)
        if i != 0:
            right(360//i)

def turtle_race():
    for step in range(15):
        speed(10)
        penup()
        write(step, align="center")
        right(90)
        forward(10)
        pendown()
        forward(150)
        penup()
        backward(160)
        left(90)
        forward(20)

    ada = Turtle()
    ada.color('red')
    ada.shape('turtle')
    ada.penup()
    ada.goto(-30,-120)
    ada.pendown()

    uo0p = Turtle()
    uo0p.color('blue')
    uo0p.shape('turtle')
    uo0p.penup()
    uo0p.goto(-30,-90)
    uo0p.pendown()

    xtuk = Turtle()
    xtuk.color('yellow')
    xtuk.shape('turtle')
    xtuk.penup()
    xtuk.goto(-30,-60)
    xtuk.pendown()
    
    nmiks = Turtle()
    nmiks.color('green')
    nmiks.shape('turtle')
    nmiks.penup()
    nmiks.goto(-30,-30)
    nmiks.pendown()
    
    for turn in range(100):
        ada.forward(randint(1,5))
        nmiks.forward(randint(1,5))
        xtuk.forward(randint(1,5))
        uo0p.forward(randint(1,5))

    write("We have a winner!")
    #write(ada.position())
