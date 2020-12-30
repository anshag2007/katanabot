import discord
import json
import os
from discord.ext import commands
def get_prefix(bot,message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix=get_prefix)
bot.load_extension('jishaku')
@bot.command(hidden=True)
@commands.is_owner()
async def load(ctx,extension,hidden=True):
    bot.load_extension(f'cogs.{extension}')
    
@bot.command(hidden=True)
@commands.is_owner()
async def unload(ctx,extension):
    bot.unload_extension(f'cogs.{extension}')
    
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
#########################     
######################### 
#########################
@bot.event
async def on_guild_join(guild):
    with open('prefixes.json','r') as f:
        prefixes =json.load(f)
    prefixes[str(guild.id)] = '>>'
    
    with open('prefixes.json','w') as f:
        json.dump(prefixes,f,indent=4)
        
@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json','r') as f:
        prefixes =json.load(f)
    prefixes.pop(str(guild.id))
    
    with open('prefixes.json','w') as f:
        json.dump(prefixes,f,indent=4)
        
        
@bot.command(brief=f'change bot\'s prefix')
@commands.has_guild_permissions(manage_guild=True)
async def prefix(ctx,prefix):
    with open('prefixes.json','r') as f:
        prefixes =json.load(f)
    prefixes[str(ctx.guild.id)] = prefix
    
    with open('prefixes.json','w') as f:
        json.dump(prefixes,f,indent=4)
    await ctx.send(f'Prefix changed to {prefix}')
        
          

bot.run('NzkwODc0NDA3NTA5NTU3Mjc4.X-G9MA.CtWYzyUyoYmJSV2T6f6OT3SydeQ')

    
