#Ban and kick extension for BlockyBot - ban-kick.py - rev. 2
import discord
from discord.ext import commands
client=commands.Bot(command_prefix="blocky.")
class mod(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('[EXTENSION] The Moderation extension has loaded.')


#Ban
    @client.command(pass_context=True)
    #Gather Data like User ID and permissions, and also the reason e.g. blocky.kick @Someone reason
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, *, reason = None):

        #Ban the user for the specified Reason
        await member.ban(reason = reason)

        #Send embed and a Reaction
        embed=discord.Embed(title="User Banned", description=f"{member} was sucsessfully banned for the reason {reason}", color=0xFF5733)
        embed.set_author(name=f"{member}")
        await ctx.message.add_reaction(emoji="✅")
        await ctx.send(embed=embed)
#End Ban


#Kick
#blocky.kick
    @client.command()
    #Does the user who ran the command have the kick members permission?
    @commands.has_permissions(kick_members = True)
    #If yes,
    #Get the data needed to kick the member, Like the user ID and reason
    async def kick(self, ctx, member : discord.Member, *, reason = None):

        #Kick The Member For The Specified Reason
        await member.kick(reason = reason)
        #Send an Embed and a Reaction saying the user was kicked.
        embed=discord.Embed(title="Kicked Sucsessfully.", description=f"Reason: {reason}, sent by BlockyBot", color=0xfcf403)
        embed.set_author(name=f"{member}")
        await ctx.message.add_reaction(emoji="✅")
        await ctx.send(embed=embed)
#End Kicked




def setup(client):
    client.add_cog(mod(client))

# End of file
