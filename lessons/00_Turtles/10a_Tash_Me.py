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
    image_path = str(image_dir / image_name)  
    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)
screen = turtle.Screen()
screen.setup(width=600, height=600) 
t=turtle.Turtle()
set_turtle_image(t, 'moustache1.gif')
screen.bgcolor('white')
t.turtlesize(stretch_wid=3, stretch_len=3, outline=4)

def set_backround_image(window, image_name):
    from pathlib import Path
    from PIL import Image
    image_dir=Path(__file__).parent/"images"
    image_path = str(image_dir/image_name)
    image=Image.open(image_path)
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)

set_backround_image(screen, "emoji.png")

turtle.exitonclick()