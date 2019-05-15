import discord
import config as cfg

from discord.ext import commands, tasks


description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

bot = commands.Bot(command_prefix='!', description=description)
userList=[]

@bot.event
async def on_ready():
    print('Logged in as')

@bot.event
async def on_message(message):
    if message.author != bot.user:
        print(message.author)
        await bot.process_commands(message)

@bot.command()
async def start(ctx):
    print(ctx.author)
    if ctx.author in userList:
        await ctx.send("L'envois de formulaire est deja activé")
    else:
        userList.append(ctx.author)
        await ctx.send("Je vais t'envoyer le formulaire au cours de la journée")

@bot.command()
async def stop(ctx):
    if ctx.author in userList:
        userList.remove(ctx.author)
        await ctx.send("L'envois de formulaire est désactivé")
    else:
        await ctx.send("L'envois de formulaire n'était pas activé")

@bot.command()
async def status(ctx):
    if ctx.author in userList:
        await ctx.send("L'envois de formulaire est activé")
    else:
        await ctx.send("L'envois de formulaire est désactivé")


bot.run(cfg.TOKEN)