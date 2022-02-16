import turtle
from turtle import Turtle, Screen
import random

squirtle = Turtle()
squirtle.shape("turtle")
squirtle.color("black")
squirtle.get_shapepoly()
squirtle.speed("fastest")
screen = Screen()
turtle.colormode(255)

color_list = [(222, 152, 103), (233, 237, 240), (128, 172, 199), (221, 130, 149), (221, 73, 90), (243, 208, 99),
              (17, 121, 157), (118, 176, 147), (34, 120, 82), (18, 165, 204), (230, 74, 70), (142, 86, 60),
              (116, 85, 102), (162, 209, 162), (13, 169, 120), (171, 183, 219), (177, 154, 75), (213, 222, 213)]


def draw_hirst_painting(matrix_size):
    for i in range(matrix_size):
        squirtle.penup()
        squirtle.setposition(-300, -300 + i * 50)
        for j in range(matrix_size):
            chosen_color = random.choice(color_list)
            squirtle.dot(20, chosen_color)
            squirtle.forward(50)


squirtle.hideturtle()
draw_hirst_painting(10)
screen.exitonclick()
