from turtle import Turtle, Screen

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)


# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)

# import turtle as t

# tim = t.Turtle()

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# import turtle as t
# import random

# tim = t.Turtle()

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)


import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# direction = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed("fastest")

# for _ in range(20000):
#     tim.color(random_color())
#     tim.forward(20)
#     tim.setheading(random.choice(direction))

tim.speed("fastest")


def spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

spirograph(5)

screen = t.Screen()
screen.exitonclick()