from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import sys
import os
import numpy as np
import pandas as pd
import matplotlib as plt


file_path = 'drivers/chromedriver.exe'

driver = webdriver.Chrome(file_path) # assign the driver path to variable

driver.execute("get", {'url': 'https://pokemondb.net/pokedex/all'})

driver.minimize_window() # minimize window

data = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "table#pokedex"))).get_attribute("outerHTML")

df  = pd.read_html(data)

df = df[0]

driver.close()  # close driver, end session

columns = ['id', 'name', 'type', 'total', 'hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed'] # column names (labels) for dataset


df.set_index("#", inplace=True) # set the id column to be the index

os.makedirs('C:/Users/Salah/Documents/apps/pokedex-app/datasets', exist_ok=True) # create new folder in project directory to store dataset  

df.to_csv("datasets/pokedex.csv", index=False) # converts dataset to csv file

df = pd.read_csv('datasets/pokedex.csv') # read and save file and check the first 5 entries

df.head()


for name in df.Name:
    if name.__contains__('Mega '):
        mega_id = df.index[df['Name'] == name].tolist()
        #print(mega_id)
        df.Name[mega_id] = name.split(' ', 1)[1]

poke_list = list(df.Name[:])

poke_list

df.head(10)