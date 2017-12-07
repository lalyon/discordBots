import discord
import asyncio
import random
client = discord.Client()
f=open("bot1key.txt")
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
#@client.event
#def system_write(x):
 #   await client.send_message(message.channel, x)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("?how is my code coming along"):
        await client.send_message(message.channel, "The sun is rising, 2/10 test cases passed")
    elif message.content.startswith("?did bot do good"):
        await client.send_message(message.channel, "https://imgur.com/4uYVWOn")
    elif message.content.startswith("?ping"):
        await client.send_message(message.channel, "pong!")
    elif message.content.startswith("?flip"):
        await client.send_message(message.channel, coin_flipper())
    elif message.content.startswith("?test"):
        system_write("this Cheese workss")
        #await client.send_message(message.channel, "Your mama")
    elif message.content.startswith("??exit"):  # this is broken.
        return 0
client.run(client_key)