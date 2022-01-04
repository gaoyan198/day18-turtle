from turtle import Turtle, Screen
from random import randint
import random

myTurtle = Turtle()
myTurtle.shape("turtle")

# for _ in range(4):
#   myTurtle.forward(100)
#   myTurtle.left(90)

# for _ in range(50):
#   myTurtle.forward(1)
#   myTurtle.penup()
#   myTurtle.forward(3)
#   myTurtle.pendown()

# def drawShape(numOfSides):
#   angle = 360 / numOfSides
#   for _ in range(numOfSides):
#     myTurtle.forward(100)
#     myTurtle.right(angle)
  

# for i in range(10):
#   myTurtle.color(random.choice(colors))
#   drawShape(i + 3)

directions = [0, 90, 180, 270]

def randomColor():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    return (r, g, b)

for _ in range(200):
  myTurtle.color(randomColor())
  myTurtle.forward(30)
  myTurtle.setheading(random.choice(directions))

myScreen = Screen()
myScreen.exitonclick()