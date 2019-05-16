import discord, asyncio, random, datetime
import config as cfg

from discord.ext import commands

# @TODO make a log file and console

description = """
Je suis Michel, un bot qui va calculer ton flow tout au long de la journée.
Je vais t'envoyer un formulaire à remplir plusieurs fois par jour, tu pourras acceder aux résultats sur une page web.
"""

help = """
    **help** - Display this message
    **start** - Active l'envois automatique du formulaire
    **stop** - Désactive l'envois automatique du formulaire
    **status** - Affiche si l'envois automatique est on/off
"""

average_time_between_test = 1.5 #in hour
minimal_time_between_test = 0.25 #in hour
maximal_time_between_test = (average_time_between_test - minimal_time_between_test) + average_time_between_test

bot = commands.Bot(command_prefix='!', description=description)
taskList = {}

@bot.event
async def on_ready():
    print('Logged in')

@bot.event
async def on_message(message):
    if message.author != bot.user:
        await exec_commands(message)
        #await bot.process_commands(message)

async def exec_commands(message):
    # Do not execute function if it's not a DM
    if not isinstance(message.channel, discord.channel.DMChannel):
        return

    message_split = message.content.split()
    command = message_split[0]

    # Start the task : send link to online form
    if command == 'start':
        if str(message.channel.recipient.id) in taskList:
            await message.channel.send("L'envois de formulaire est déja activé.")
        else:
            # check if there is parameters
            if len(message_split) > 1:
                try:
                    int(message_split[1])
                    int(message_split[2])
                except:
                    await message.channel.send("Commande invalide.")
                    return

                taskList[str(message.channel.recipient.id)] = asyncio.ensure_future(send_form(message.channel, int(message_split[1]), int(message_split[2])))
                await message.channel.send("Je vais t'envoyer le formulaire entre {} h et {} h.".format(message_split[1], message_split[2]))

            else:
                taskList[str(message.channel.recipient.id)] = asyncio.ensure_future(send_form(message.channel))
                await message.channel.send("Je vais t'envoyer le formulaire au cours de la journée.")

    # Stop task
    elif command == 'stop':
        if str(message.channel.recipient.id) in taskList:
            taskList[str(message.channel.recipient.id)].cancel()
            del taskList[str(message.channel.recipient.id)]
            await message.channel.send("L'envois de formulaire est désactivé.")
        else:
            await message.channel.send("L'envois de formulaire n'était pas activé.")

    # Send status to user
    elif command == 'status':
        if str(message.channel.recipient.id) in taskList:
            await message.channel.send("L'envois de formulaire est activé.")
        else:
            await message.channel.send("L'envois de formulaire est désactivé.")

    # Display help message
    elif command == 'help':
        embed = discord.Embed()
        embed.title = "Michel"
        embed.description = description
        embed.add_field(name="Commandes", value=help, inline=False)

        await message.channel.send(embed=embed)

    else:
        await message.channel.send("Je comprends pas ce que tu dis gros.")


async def send_form(channel, start_hour=0, end_hour=24):
    time_in_min = random.randint(int(minimal_time_between_test * 60), int(maximal_time_between_test * 60))
    print("send to {} in {} min".format(channel.recipient ,time_in_min))
    await asyncio.sleep(time_in_min*60)
    if int(datetime.datetime.now().hour) >= start_hour and int(datetime.datetime.now().hour) < end_hour:
        await channel.send("C'est l'heure de répondre aux questions : {}".format(cfg.FORM_URL))
    await send_form(channel, start_hour, end_hour)

def dump(obj):
   """
    Use for debug : dump an objects properties and methods
   :param obj:
   """
   for attr in dir(obj):
       if hasattr( obj, attr ):
           print( "obj.%s = %s" % (attr, getattr(obj, attr)))

if __name__ == '__main__':
    bot.run(cfg.TOKEN)