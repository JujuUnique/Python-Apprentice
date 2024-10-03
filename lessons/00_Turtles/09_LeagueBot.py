""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables.
"""

import turtle
def set_turtle_image(turtle, image_name):
    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)
    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)
screen = turtle.Screen()
screen.setup(width=600, height=600)
t = turtle.Turtle()
set_turtle_image(t, 'leaguebot_bolt.gif')

screen.bgcolor('white')

t.turtlesize(stretch_wid=10, stretch_len=10, outline=4)

t.pencolor('blue')
def draw_polygon(sides):
    angle = 360/sides
    for i in range(sides):
        t.forward(50)
        t.left(angle)
draw_polygon(6)
turtle.exitonclick()

... # Your Code Here