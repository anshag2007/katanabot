import discord
import urllib.request # at top
import json # at top
import random
from discord.ext import commands
class Memes(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def meme(self,ctx):
        url = "https://meme-api.herokuapp.com/gimme/dankmemes"
        response = urllib.request.urlopen(url)      
        data = json.loads(response.read()) 
        img_url = data['url']   
        post_link = data['postLink']
        img_title = data['title']
        memebed = discord.Embed(title=img_title,url=img_url,color=random.randint(0,0xffffff))
        memebed.set_image(url=img_url)
        await ctx.send(embed=memebed)


# now u can use these img_url, post_link variables in your message 
def setup(bot):
    bot.add_cog(Memes(bot))
