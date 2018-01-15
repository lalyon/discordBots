# vist http://discordpy.readthedocs.io/en/latest/api.html 
#for more on the discord api
import discord
import asyncio
import random
import requests
import json
import giphypop

client = discord.Client()
f=open("key.txt")
for l in f:
    l=l.strip()
    client_key=l
@client.event
async def on_ready():
    print("logged in as:")
    print("client.user.name")
    print("ID")
    print (client.user.id)
    print("Ready to use!")
def coin_flipper():
    random.seed(None)
    x= random.randint(1,2)
    if x==1:
        return "Heads"
    else :
        return "Tails"
g = giphypop.Giphy()
#@client.event
#def system_write(x):
 #   await client.send_message(message.channel, x)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("!how is my code coming along"):
        await client.send_message(message.channel, "The sun is rising, 2/10 test cases passed")
    elif message.content.startswith("!did bot do good"):
        await client.send_message(message.channel, "https://imgur.com/4uYVWOn")
    elif message.content.startswith("!ping"):
        await client.send_message(message.channel, "pong!")
    elif message.content.startswith("!flip"):
        await client.send_message(message.channel, coin_flipper())
    elif message.content.startswith("!gif"):
        img = g.translate(message.content[5:])
        await client.send_message(message.channel, img)
    elif message.content.startswith("!dadjoke"):
        headers = {'Accept': 'text/plain'}
        img = requests.get('https://icanhazdadjoke.com/', headers=headers)
        joke = img.text
        await client.send_message(message.channel, joke)
    elif message.content.startswith("!test"):
        await client.send_message(message.channel, "Your mama")
    elif message.content.startswith("!exit"):  # this is broken.
        return 0
client.run(client_key)