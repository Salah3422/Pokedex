from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pandas as pd
import matplotlib as plt


driver = webdriver.Chrome('C:/Users/Salah/Documents/drivers/chromedriver.exe') # lookup the user input in pokemon database and search for corresponding db entry.

driver.get('https://pokemondb.net/pokedex/all') # get request - opens chrome browser and navigates to URL

driver.maximize_window()


pokemon_id = []
pokemon_id_html = driver.find_elements(By.CLASS_NAME, 'infocard-cell-data') # retrieve the object (pokemon) from the database and output the attributes to display to user
for poke_id in pokemon_id_html:
    pokemon_id.append(poke_id.text)

pokemon_name = []
pokemon_name_html = driver.find_elements(By.CLASS_NAME, 'ent-name')
for name in pokemon_name_html:
    pokemon_name.append(name.text)

pokemon_type = []
pokemon_type_html = driver.find_elements(By.CLASS_NAME, 'cell-icon')
for p_type in pokemon_type_html:
    pokemon_type.append(p_type.text)

pokemon_total = []
pokemon_total_html = driver.find_elements(By.CLASS_NAME, 'cell-total')
for total in pokemon_total_html:
    pokemon_total.append(total.text)

pokemon_hp = []
pokemon_hp_html = driver.find_elements(By.XPATH, "//*[@class='cell-num'][1]")
for hp in pokemon_hp_html:
    pokemon_hp.append(hp.text)

pokemon_attack = []
pokemon_attack_html = driver.find_elements(By.XPATH, "//*[@class='cell-num'][2]")
for attack in pokemon_attack_html:
    pokemon_attack.append(attack.text)

pokemon_defense = []
pokemon_defense_html = driver.find_elements(By.XPATH, "//*[@class='cell-num'][3]")
for defense in pokemon_defense_html:
    pokemon_defense.append(defense.text)

pokemon_special_attack = []
pokemon_special_attack_html = driver.find_elements(By.XPATH, "//*[@class='cell-num'][4]")
for special_attack in pokemon_special_attack_html:
    pokemon_special_attack.append(special_attack.text)

pokemon_special_defense = []
pokemon_special_defense_html = driver.find_elements(By.XPATH, "//*[@class='cell-num'][5]")
for special_defense in pokemon_special_defense_html:
    pokemon_special_defense.append(special_defense.text)

pokemon_speed = []
pokemon_speed_html = driver.find_elements(By.XPATH, "//*[@class='cell-num'][6]")
for speed in pokemon_speed_html:
    pokemon_speed.append(speed.text)


driver.close()  # close driver, end session



columns = ['id', 'name', 'type', 'total', 'hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed'] 

attributes = [pokemon_id, pokemon_name, pokemon_type, pokemon_total, pokemon_hp, pokemon_attack, pokemon_defense, pokemon_special_attack, pokemon_special_defense, pokemon_speed]






