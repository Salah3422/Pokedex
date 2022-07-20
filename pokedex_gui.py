import tkinter as tk
from turtle import width
#from pokedex import *



#window
window = tk.Tk()  #main

window.title('Universal Pokedex')
window.configure(background="red")

bg_image = tk.PhotoImage(file="images/pokedex.gif")

canvas = tk.Canvas(window, height=700, width=800)
canvas.pack()

frame = tk.Frame(window, bg='red')
frame.place(relwidth=1, relheight=1)
#window




#phsyical properties
label_1 = tk.Label(window, text="Welcome to the Universal Pokedex! This app returns the stats of all pokemon currently listed on the online pokemon database.", bg='white')
label_1.place(relx=0, rely=0, relwidth=1, relheight=0.1)

label_2 = tk.Label(window, text="Enter a pokemon name to see a list of its stats: ", bg='white')
label_2.place(relx=0, rely=0.78, relwidth=1, relheight=0.1)

entry = tk.Entry(window, bg='white')
entry.place(relx=0.42, rely=0.89, relwidth=0.15, relheight=0.04)

button = tk.Button(window, text="Search", bg='gray')
button.place(relx=0.42, rely=0.94, relwidth=0.15, relheight=0.05)
#physical properties




#Button(window, text="Exit", width=14, command=close_window).grid(row=7, column=0, sticky=W) #exit button


window.mainloop()  #mainloop




'''
pokemon_name = tuple(pokemon_name)
poke_dictionary = {
    pokemon_name : attributes
}




#click function
def click():
   entered_text = text_entry.get() # collects text from text entry box
   output.delete(0.0, END)
    try:
        definition = poke_dictionary[entered_text]
    except:
        definition = "sorry there is no such pokemon"
    output.insert(END, definition)


# Exit function
def close_window():
    window.destroy()
    exit()

'''