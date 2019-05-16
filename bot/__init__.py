import discord
import config as cfg
import asyncio

from discord.ext import commands, tasks

# @TODO need to work only with private messages

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

bot = commands.Bot(command_prefix='!', description=description)
taskList = {}

@bot.event
async def on_ready():
    print('Logged in as')

@bot.event
async def on_message(message):
    if message.author != bot.user:
        await exec_commands(message)
        #await bot.process_commands(message)

async def exec_commands(message):
    # Do not execute function if it's not a DM
    if not isinstance(message.channel, discord.channel.DMChannel):
        return

    # Start the task : send link to online form
    if message.content == 'start':
        if str(message.channel.recipient.id) in taskList:
            await message.channel.send("L'envois de formulaire est deja activé")
        else:
            taskList[str(message.channel.recipient.id)] = asyncio.ensure_future(send_form(message.channel))
            await message.channel.send("Je vais t'envoyer le formulaire au cours de la journée")

    # Stop task
    elif message.content == 'stop':
        if str(message.channel.recipient.id) in taskList:
            taskList[str(message.channel.recipient.id)].cancel()
            del taskList[str(message.channel.recipient.id)]
            await message.channel.send("L'envois de formulaire est désactivé")
        else:
            await message.channel.send("L'envois de formulaire n'était pas activé")

    # Send status to user
    elif message.content == 'status':
        if str(message.channel.recipient.id) in taskList:
            await message.channel.send("L'envois de formulaire est activé")
        else:
            await message.channel.send("L'envois de formulaire est désactivé")

async def send_form(channel):
    await asyncio.sleep(5)
    await channel.send("Voila le formulaire : {}".format(cfg.FORM_URL))
    await send_form(channel)

def dump(obj):
   """
    Use for debug : dump an objects properties and methods
   :param obj:
   """
   for attr in dir(obj):
       if hasattr( obj, attr ):
           print( "obj.%s = %s" % (attr, getattr(obj, attr)))

bot.run(cfg.TOKEN)