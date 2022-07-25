from os import times
import tkinter as tk
#from tkinter import ttk
from PIL import ImageTk, Image
from turtle import color, width
from xmlrpc.client import loads
from pokedex import *


#window
window = tk.Tk()  #main

window.title('Universal Pokedex')
window.configure(background="red")
window.iconbitmap("images/icon.ico")

bg_image = tk.PhotoImage(file="images/pokedex.gif")

canvas = tk.Canvas(window, height=700, width=800)
canvas.pack()

frame = tk.Frame(window, bg='red')
frame.place(relwidth=1, relheight=1)
#window


def validate_text():
    global entry
    string = entry.get()
    #label_2.configure(text=string)
    string = string.title() # capitalize first letter of entry to match database

    if string not in poke_list:   # ensure the user is typing in valid input, if not create a validation loop by reiterating user to give valid pokemon name or id.
        label_2.configure(text="That pokemon was not found, please try again: ") # validation look/error trap
    string = string.title()

    if string in poke_list:
        print("Searching for {} ... ".format(string))
        print("{} Found!".format(string))
        poke_stats = df.loc[df['Name'] == string] # return pokemon stats to user if successfully located
        label_2.configure(text=poke_stats)



#phsyical properties
label_1 = tk.Label(window, text="Welcome to the Universal Pokedex! This program contains the statistics of all the pokemon stored in the official Pokemon Database. \n Begin by entering a pokemon name below.", bg='red', font=("Cambria", 25))
label_1.place(relx=0, rely=0.05, relwidth=1, relheight=0.1)

label_2 = tk.Label(window, text="Enter a pokemon name to see a list of its stats: ", bg='#5CB3FF', font=("Courier", 20))
label_2.place(relx=0, rely=0.78, relwidth=1, relheight=0.1)

img1 = ImageTk.PhotoImage(Image.open("images/johto-starters.gif"))
img2 = ImageTk.PhotoImage(Image.open("images/pokeball.gif"))

label_3 = tk.Label(window, bg='red', image=img1) # This label will contain the entered pokemon's image
label_3.place(relx=0.25, rely=0.25, relwidth=0.50, relheight=0.50)

label_4 = tk.Label(window, bg='white', image=img2)
label_4.place(relx=0.05, rely=0.3, relwidth=0.2, relheight=0.3)

label_5 = tk.Label(window, bg='white', image=img2)
label_5.place(relx=0.75, rely=0.3, relwidth=0.2, relheight=0.3)

entry = tk.Entry(window, bg='white')
entry.place(relx=0.42, rely=0.89, relwidth=0.15, relheight=0.04)

button = tk.Button(window, text="Search", command=validate_text, bg='grey')
button.place(relx=0.42, rely=0.94, relwidth=0.15, relheight=0.05)
#physical properties





#widgets

#widgets

window.mainloop()  #mainloop