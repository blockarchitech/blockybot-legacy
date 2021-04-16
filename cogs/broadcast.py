#Broadcast extension for BlockyBot

import discord
from discord.ext import commands
client=commands.Bot(command_prefix="blocky.")
class broadcast(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('[EXTENSION] The Broadcast extension has loaded.')

#BC Commands
    @commands.has_permissions(kick_members = True)
    async def bc(self, ctx, *, message, urgent = None):
        if urgent == "True":
            embed=discord.Embed(title=":mega: Urgent ||@everyone||", description=message, color=0x0390fc)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            await ctx.message.add_reaction(emoji="✅")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=":mega: Announcment", description=message, color=0x0390fc)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            await ctx.message.add_reaction(emoji="✅")
            await ctx.send(embed=embed)



#End of file
def setup(client):
    client.add_cog(broadcast(client))
