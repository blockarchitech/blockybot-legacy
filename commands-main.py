

#Imports commands from discord.ext, imports load_dotenv fron dotenv, and loads OS
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

#Load token and Guild Name from .env file.
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client=commands.Bot(command_prefix="blocky.")

@client.event
async def on_ready():
  print(f"blockybot Is connected to discord!")

@client.command()
async def ping(ctx):
  await ctx.send(f"Pong! Client Latency: {client.latency}ms")

client.run(TOKEN)
