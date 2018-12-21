# Work with Python 3.6
import discord
import re
import requests
import json
import os

TOKEN = os.environ['botToken']

client = discord.Client()

@client.event
async def on_message(message):
	# we do not want the bot to reply to itself
	if message.author == client.user:
		return
	searchObj = re.search( r'quran \b([1][0,1][0,1,2,3,4]|[1-9][0-9]?)\b:([0-9]{1,3})\b', message.content.lower(), re.I)
	if (searchObj):
		print (searchObj.group(0))
		print (searchObj.group(1))
		print (searchObj.group(2))

		msg = requests.get(url = f'http://api.alquran.cloud/ayah/{searchObj.group(1)}:{searchObj.group(2)}/en.asad')
		# print(type(msg))
		# print(dir(msg))
		response_text = json.loads(msg.text)
		ayah_ar = response_text['data']['text']
		print(ayah_ar)

		await client.send_message(message.channel, ayah_ar)

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(TOKEN)
