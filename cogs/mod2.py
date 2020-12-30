import discord
import random
from discord.ext import commands

class AlsoMod(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def mute(self,ctx,member:discord.Member):
        guild = ctx.guild
        muted_role =discord.utils.get(guild.roles, name = "Muted")
    
        await member.add_roles(muted_role)
        await ctx.send(f'Muted {member}')
        
    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def unmute(self,ctx,member:discord.Member):
        guild = ctx.guild
        muted_role = discord.utils.get(guild.roles, name = "Muted")
        await member.remove_roles(muted_role)
        await ctx.send(f'Unmuted {member}')
        
        
def setup(bot):
    bot.add_cog(AlsoMod(bot))