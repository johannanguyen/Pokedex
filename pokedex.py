import json
import requests
import datetime
import random
from flask import Flask, render_template
from flask_assets import Bundle, Environment
import pygame
from pygame import mixer

#VARIABLES STARTING WITH j CAME FROM OUR JSON FILE
#VARIABLES STARTING WITH api IS EXTRACTED FROM API
#VARIABLES STARTING WITH p IS CREATED IN .PY BUT USED IN .HTML

app = Flask(__name__)
@app.route("/")

def index():
	cry = f'cries\{jName}.mp3'
	pygame.mixer.init()
	pygame.mixer.music.load(cry)
	pygame.mixer.music.play(0)
	
	data = {'myPokemon': jName}
	return render_template("index.html",
		pName=jName,
		pDes=jDes,
		pNum=jNum + 1,
		pType=apiType,
		pHeight=apiHeight,
		pWeight=apiWeight,
		pPicture=pPicture,
		data=data)

with open('pokemon.json') as f:
	jData = json.load(f)


	#Randomly chooses a num between 0 - 299
def choosePoke(n):
	i = random.randint(0,n)
	return i


	#jNum is a randomized number out of 279 (since we have 280 pokemon)
	#jName is name of random pokemon
	#jDes is the full description of random pokemon
	#pPicture is used to display image of random pokemon
	#f denotes there is a variable in the string
jNum = choosePoke(len(jData['pokemon']))
jName = jData['pokemon'][jNum]['name']
jDes = jData['pokemon'][jNum]['descrip']
pPicture = f'http://www.pokestadium.com/sprites/xy/{jName}.gif'

	#Opens API link
apiLink = f'https://pokeapi.co/api/v2/pokemon/{jName}'
apiData = requests.get(apiLink)

	#Places API data in a usable package
pack_apiData = apiData.json()

	#Sets each desired attribute using JSON
apiNum = pack_apiData['id']
apiType = pack_apiData['types'][0]['type']['name']
apiHeight = pack_apiData['height']
apiWeight = pack_apiData['weight']

	#Used to test if desired attributes were printed (in console)
print(jName, apiNum, apiType, apiHeight, apiWeight)


