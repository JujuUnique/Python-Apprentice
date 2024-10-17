# Tash Me with a Click
# 
# Update your Tash Me program ( copy your old program here )to put 
# the moustache where you click on the screen.
#
# Hint: See 08a_More Turtle Programs, section 'Click on the Screen'
 
... # Your code here
import turtle
def set_turtle_image(turtle,image_name):
    from pathlib import path
    image_dir = path(__file__).parent / "images"
