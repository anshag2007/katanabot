import discord
import random
from discord.ext import commands
class Info(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot Is Ready')
       
    @commands.command(brief='gives bot latency')
    async def ping(self,ctx):
        pbed = discord.Embed(description=f'Pong! {round(self.bot.latency*1000)}ms.',color=random.randint(0,0xffffff))
        await ctx.send(embed=pbed)
    @commands.command(brief='do a poll')
    async def poll(self,ctx,*,message):
        await ctx.message.delete()
        botmsg = await ctx.send(f'{ctx.message.author} asks: {message}')
        await botmsg.add_reaction('<:upvote:791947138661613568>')
        await botmsg.add_reaction('<:downvote:791947157509898270>')
        await botmsg.add_reaction('<:shuurug:791947661006602240>')

def setup(bot):
    bot.add_cog(Info(bot))