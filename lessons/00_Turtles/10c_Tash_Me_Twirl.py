
""" Tash Me with a Twirl
 
Update your Tash Me Click program ( copy your old program here )
so the moustache will twirl when you click on it. 

Hint: See 08a_More Turtle Programs, section 'Click on the Turtle'
"""

... # Your code here

import turtle
def set_turtle_image(turtle,image_name):
    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)
    screen=turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

screen=turtle.Screen()
screen.setup(width=600, height=600)
t=turtle.Turtle()
set_turtle_image(t, 'moustache1.gif')
screen.bgcolor('white')
t.turtlesize(stretch_wid=3, stretch_len=3, outline=4)

def set_backround_image(window, image_name):
    from pathlib import Path
    from PIL import Image
    image_dir=Path(__file__).parent/"images"
    image_path=str(image_dir/image_name)
    image=Image.open(image_path)
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)

set_backround_image(screen, "emoji.png")
t.penup()
def screen_clicked(x, y):
    t.goto(x, y)

screen.onclick(screen_clicked)

turtle.done()