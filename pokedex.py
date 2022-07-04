from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pandas as pd
import matplotlib as plt


print("Hello World! \nThis is going to be my introductory commit for my pokedex project! \nMy goal will be to web scrape all pokemon data from the pokemon database and formulate it into a pokeddex program. \nI will do my best and I hope everyone enjoys. Thank you!")



pokemon_lookup = input("Type the name of the pokemon you want to search up: ") # Ask the user to input the pokemon they want to search



pokemon_names = ['bulbasaur', 'ivysaur', 'venasaur', 'charmander', 'charmeleon', 'charizard', 'squirtle', 'wartortle', 'blastoise']

while pokemon_lookup not in pokemon_names: # ensure the user is typing in valid input, if not create a validation loop by reiterating user to give valid pokemon name or id.
    pokemon_lookup = input("That pokemon was not found, please try again: ")



driver = webdriver.Chrome('C:/Users/Salah/Documents/drivers/chromedriver.exe') # lookup the user input in pokemon database and search for corresponding db entry.

driver.get('https://pokemondb.net/pokedex/all') # get request - opens chrome browser and navigates to URL



# retrieve the object (pokemon) from the database and output the attributes to display to user


driver.close() # close driver, end session







