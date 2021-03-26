# Python Discord Bot Rewrite - Attempt 2 - Self hosted edition - github.com/blockarchitech
# Testing script and simple command - imports required stuff

# import discord.py and python-dotenv
import os

import discord
from dotenv import load_dotenv
client = commands.Bot(command_prefix='.')
#get token and guild id fron .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#discord client
client = discord.Client()

#prints the name of guild and ID that the bot is currently in or specified in .env
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
#end of the guild name

#self-check manual command - not ideal because it would be alot easier with a PREFIX = 'blocky.' varible, but oh well, ill work on that later
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'blocky.test':
        response = 'test complete!'
        await message.channel.send(response)

#commands located in commands.py

#The end
#DO NOT DELETE THIS LINE - CRITICAL FOR MAKING THE BOT WORK
client.run(TOKEN)