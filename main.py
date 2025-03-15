import requests
from bs4 import BeautifulSoup
import json
import re
import os

url_random_map = 'https://trackmania.exchange/maprandom'
#Change this to your Trackmania 2020 maps directory
#The slashes must be forward slashes like in the example
user_directory = 'C:/Users/user1/Documents/Trackmania2020/Maps/Downloaded' 
os.chdir(user_directory)

#Get random map from trackmania.exchange
response = requests.get(url_random_map)
soup = BeautifulSoup(response.text, 'html.parser')

#Get map id to download
template_data = soup.find('div', {'template': 'IdView'})['template-data']
get_id = json.loads(template_data)

#Get map name
find_name = soup.find('div', {'class': 'col text-break'})
name = re.sub("<.*?>", "", str(find_name))
name = name.strip()
print(name)

#Download map
base_url = 'https://trackmania.exchange/mapgbx/'
map_url = base_url + str(get_id["Id"])
map = requests.get(map_url)
map_content = map.content

with open(f"{name}.Map.Gbx", mode="wb") as file:
    file.write(map_content)
print("Map downloaded!")

#This automaticaly opens the downloaded map
#os.startfile(f"{name}.Map.Gbx")


