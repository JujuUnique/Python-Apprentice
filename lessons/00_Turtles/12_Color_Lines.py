"""
Color Lines

1) Finish the program to make Tina draw a square with each side being a different color. 

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

t = turtle.Turtle()                  # Create a turtle named tina

t.shape('turtle')                    # Set the shape of the turtle to a turtle
t.speed(1.5)                           # Make the turtle move as fast, but not too fast. 


colors = [ 'red', 'blue', 'black', 'orange']    # define a list of colors

for item in colors:                            # loop through the colors
    ... # Your code here
    t.color(colors)
    t.forward(200)
    t.left(90)

turtle.exitonclick()


# 2) Make another square, but put the colors in reverse order, using a negative index. 

... # Your code here




