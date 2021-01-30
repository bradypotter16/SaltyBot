import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
     if client.user.id != message.author.id:
          if message.content == "ping":
               await message.channel.send('pong')

client.run(TOKEN)



