"""
 
"""
import turtle

def set_turtle_image(turtle, image_name):
    image_dir = Path(_file_).parent / "images"
    image_path = str(image_dir) / (image-name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)
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
set_turtle_image(t, "pikachu.gif")
t.penup()
t.speed(3)
for i in range(4):
    t.goto(200, 200)
    t.goto(-200, -200)


turtle.exitonclick()     
```
