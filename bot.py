'''
bot: discord.py API version 1.3.3
made by im.ri0t
'''

import json
from pathlib import Path
import asyncio
import os
from random import randint, choice

import discord as d
from discord.ext import commands

from termcolor import cprint
try:
    import colorama
    colorama.init()
except ImportError:
    pass

from util import lists as l

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f'{cwd}')

def _pre(bot, message):
    '''prefix setting for the bot'''
    prefixes = ['-']
    if not message.guild:
        return '-'
    return commands.when_mentioned_or(*prefixes)(bot, message)

secret = json.load(open(cwd+'/config/secrets.json'))
bot=commands.Bot(command_prefix=_pre, owner_id=313168485591154688, case_insensitive=True)

token = secret['token']
url = 'https://discordapp.com/api/oauth2/authorize?client_id=699160052015300649&permissions=8&scope=bot'

for file in os.listdir('cogs'):
    if file.endswith('.py'):
        name = file[:-3]
        bot.load_extension(f'cogs.{name}')

#async def status_loop():
#    while True:
#        while True:
#            stat = randint(1,1)
#            asyncio.sleep(3)
#
#        if stat == 1:
#            name_sel = choice(l.playingStat)
#            await bot.change_presence(activity=d.Game(name=name_sel))
#            return
#        elif stat == 2:
#            name_sel = choice(l.listeningStat)
#            await bot.change_presence(activity=d.Activity(type=d.ActivityType.listening, name=name_sel))
#            return
#        elif stat == 3:
#            name_sel = choice(l.watchingStat)
#            await bot.change_presence(activity=d.Activity(type=d.ActivityType.watching, name=name_sel))
#            return
#
#        else:
#            return



@bot.event
async def on_ready():
    '''printed in the console on startup'''
    cprint('------------------------------------------------------------------------------------------------------------------------', 'cyan')
    print('{0}'.format(bot.user))
    print('discord.py API version', '{0}'.format(d.__version__))
    print('the vibes are here now')
    cprint(url, 'red')
    cprint('------------------------------------------------------------------------------------------------------------------------', 'cyan')
#    await status_loop()
    await bot.change_presence(activity=d.Activity(type=d.ActivityType.watching, name='your vibes'))


#@bot.event
#async def on_message(message):
#    #Ignore messages sent by yourself
#    if message.author.id == bot.user.id:
#        return
#    await bot.process_commands(message)







bot.run(token)
