"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk
# Create a window object
window=Tk()
window.withdraw()

# Hide the window, hint: use the withdraw method

# Ask the user for the first number   
number=simpledialog.askinteger("", "give a number")
# Ask the user for the second number
number2=simpledialog.askinteger("","another number")
# Display the sum of the two numbers 
messagebox.showinfo('',"your numbers equal " +str(number+number2))
# Keep the window open oh yeah also click trash otherwise it wont work lol
#window.mainloop()


