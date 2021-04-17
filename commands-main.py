# BlockyBot Developer Edition - MIT license - read more on github.
#Imports commands from discord.ext, imports load_dotenv fron dotenv, and loads OS
import os
import discord
import time
import random
from discord.ext import commands
from dotenv import load_dotenv

logout_token = random.randrange(1000, 30000)
random.seed(0)
#Load token and Guild Name from .env file.
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client=commands.Bot(command_prefix="blocky.")

#Ready Bot
@client.event
async def on_ready():
  print(f"[SYSTEM] BlockyBot connected to discord.")
  print(f"[WARN] Running on Developer edition. BlockyBot will not log Access Token use and will use a static token!")
  print(f"[SYSTEM] Access Token: {logout_token}")
  print(f"[SYSTEM] BlockyBot is ready!")
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="blocky.help - https://bit.ly/3wvxomK"))



#blocky.ping - Literally just sends the user ping, nothing else.
@client.command()
async def ping(ctx):
  await ctx.send(f"Pong! Client Latency: {client.latency}ms")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed=discord.Embed(title="Unknown Command", description=f"The requested command was not found. Please double-check your spelling and try again.", color=0xFF5733)
        await ctx.send(embed=embed)

# extensions

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    embed=discord.Embed(title="Extension Loaded", description=f"{extension} was loaded.", color=0x61ff5c)
    await ctx.send(embed=embed)

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    embed=discord.Embed(title="Extension Unloaded", description=f"{extension} was unloaded.", color=0xFF5733)
    await ctx.send(embed=embed)


#Load extensions on startup
for filename in os.listdir(r'cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#goodbye!

@client.command()
async def exit(ctx, *, token = None):
    await ctx.send("Checking Access Token...")
    if token == logout_token:

        await ctx.send("Token verified!")
        await ctx.send("BlockyBot is logging off.")
        await ctx.bot.logout()

    else:
        await ctx.send("Invalid/Wrong Token. Error A03 (User-Made)")

#Makes the bot actually work (:D)
client.run(TOKEN)
