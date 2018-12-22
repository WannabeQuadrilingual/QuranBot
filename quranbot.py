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
	searchObj = re.search( r'qur\'?an \b([1][0,1][0,1,2,3,4]|[1-9][0-9]?)\b:([0-9]{1,3})\b-?(\b([0-9]{1,3})\b)?', message.content.lower(), re.I)
	if (searchObj):
		if(searchObj.group(3)):
			print (searchObj.group(0))
			print (searchObj.group(1))
			
			start = int(searchObj.group(2))
			end = int(searchObj.group(3))

			print (start)
			print (end)

			for x in range (start,end+1):

				msg = requests.get(url = f'http://api.alquran.cloud/ayah/{searchObj.group(1)}:{str(x)}/en.yusufali')
				response_text = json.loads(msg.text)
				ayah_ar = "Qur'an " + searchObj.group(1) + ":" + str(x) + "\n" + response_text['data']['text']
				print(ayah_ar)
				await client.send_message(message.channel, ayah_ar)

		else:
			print (searchObj.group(0))
			print (searchObj.group(1))
			print (searchObj.group(2))
			msg = requests.get(url = f'http://api.alquran.cloud/ayah/{searchObj.group(1)}:{searchObj.group(2)}/en.yusufali')
			response_text = json.loads(msg.text)
			ayah_ar = "Qur'an " + searchObj.group(1) + ":" + searchObj.group(2) + "\n" + response_text['data']['text']
			print(ayah_ar)
			await client.send_message(message.channel, ayah_ar)

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(TOKEN)
