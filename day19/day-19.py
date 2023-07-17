#python higher order funcitons and event listners.


from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun= move_forwards)
screen.exitonclick()


# def function_a(something):
#     #do this with something
#     #then do this
#     #finally do this

# def function_b():
#     #do this

# function_a(function_b)


#example

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator(n1, n2, func):
    return func(n1, n2)

result = calculator(2, 3, divide)
print(result)


#coding challenge:  etch-a-sketch

from turtle import Turtle, Screen

tim = Turtle()
Screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

Screen.listen()
Screen.onkey(move_forward, "w")
Screen.onkey(move_backward, "s")
Screen.onkey(turn_left, "a")
Screen.onkey(turn_right, "d")
Screen.onkey(clear, "c")
# Screen.onkey()

Screen.exitonclick()
