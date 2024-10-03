""" Tash Me

Write a program that:
1) Loads an emoji image as the background
2) Make the turtle shape a moustach
3) Move the moustache to the right spot on the emoji

Hint: See 08a_More Turtle Programs, section 'Change the Background Image' and
'Change the Turtle Shape'
"""

... # Your code here
import turtle
def set_turtle_image(turtle,image_name):
    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = dir(image_dir / image_name)  
    screen = turtle.getscreen()
    screen.addshape(image_path)
screen=turtle.screen()
screen.setup(width=600, hight=600)
t=turtle.Turtle()

screen.bgcolor('white')
