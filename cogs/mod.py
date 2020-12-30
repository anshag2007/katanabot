import discord
import random
from discord.ext import commands
class Mod(commands.Cog):
    def __init__(self,bot):
        self.bot = bot 
    @commands.command(aliases=['purge'],brief='clears a certain amount of messages')
    @commands.has_guild_permissions(manage_messages=True)
    async def clear(self,ctx,amount=5):
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)
    @commands.command(brief='kicks the mentioned user')
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self,ctx,member:discord.Member,*,reason='not specified'):
        await member.kick(reason=reason)
        kbed = discord.Embed(description=f'Kicked {member} with reason {reason}\nAction Taken By {ctx.message.author}',color=random.randint(0,0xffffff)) 
        await ctx.send(embed=kbed)
    @commands.command(brief='bans the mentioned user')
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self,ctx,member:discord.Member,*,reason='not specified'):
        await member.ban(reason=reason)
        bbed = discord.Embed(description=f'Banned {member} with reason {reason}\nAction Taken By {ctx.message.author}',color=random.randint(0,0xffffff)) 
        await ctx.send(embed=bbed)
    @commands.command(brief='unbans a user')
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self,ctx,member,*,reason='not specified'):
        member = await self.bot.fetch_user(int(member))
        await ctx.guild.unban(member,reason=reason)
        ubbed = discord.Embed(description=f'Unbanned {member} with reason {reason}\nAction Taken by {ctx.message.author}',color=random.randint(0,0xffffff))
        await ctx.send(embed=ubbed)

    @kick.error
    async def kick_error(self,ctx,error):
        
        if isinstance(error,commands.BadArgument):
            
            await ctx.send("Please Provide a valid member.")
        elif isinstance(error,commands.MissingPermissions):
            await ctx.send("You don't have permissions to perform that action.")

def setup(bot):
    bot.add_cog(Mod(bot))