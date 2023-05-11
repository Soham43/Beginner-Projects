import tkinter
import random
from PIL import Image, ImageTk

# Creating top level widget
root = tkinter.Tk()
root.geometry("500x500") 
root.title("Roll The Damn Dice")

# Adding labels into frames
BlankLine = tkinter.Label(root, text="")
BlankLine.pack()

# Adding labels with different fonts and formatting
HeadingLabel = tkinter.Label(text="Hello from Soham", fg="pale goldenrod", bg="black", font="Impact 13 italic")
HeadingLabel.pack(padx=20,pady=10, fill="x")  

#images
dice = ['die1.png', 'die2.png', 'die3.png', 
    'die4.png', 'die5.png', 'die6.png']

#genereating random dice images between 0 to 6
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

#construct a label widget for image
ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage
ImageLabel.pack(expand=True)

#button function
def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    #update image
    ImageLabel.configure(image=DiceImage)
    ImageLabel.image = DiceImage

#adding button
button = tkinter.Button(root, text="Roll it", fg="black", bg="pale goldenrod", command=rolling_dice)
button.pack(expand=True) 

root.mainloop()
