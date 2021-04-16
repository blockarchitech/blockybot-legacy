import discord
from discord.ext import commands
client=commands.Bot(command_prefix="blocky.")
class Purge(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('[EXTENSION] The Purge extension has loaded.')

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, *, amount = None):
        await ctx.channel.purge(limit=amount)
        await ctx.send("Complete")


def setup(client):
    client.add_cog(Purge(client))
