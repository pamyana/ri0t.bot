'''
a cog utilizing lists of randomly selected responses 
'''

from random import choice
import asyncio

import discord as d 
from discord.ext import commands

from util import lists as l


class basicReplies(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot
        self.name = kwargs.get('username')
    
    @commands.command(pass_context=True)
    async def kill(self, ctx, *, member: d.Member = None):
        '''a command used to "kill" another member'''
        await ctx.trigger_typing()
        if member is None:
            message = choice(l.killNoMention)
            await ctx.send(message)
        
        elif member.id == 699160052015300649:
            message = choice(l.killSelf)
            await ctx.send(message)
        elif member.id == 184715297536606208 and member.id == ctx.message.author.id:
            await ctx.send('**NO**')
        elif member.id == 313168485591154688 and member.id == ctx.message.author.id:
            await ctx.send('I\'m not killing you dad lol')
        elif member.id == ctx.message.author.id:
            await ctx.send('who do I look like, Jack Kevorkian?\nno assisted suicide lol')
        elif member.id == 184715297536606208:
            await ctx.send('I\'m not going to hurt my mom, assface')
        elif member.id == 313168485591154688:
            message = choice(l.killDad)
            await ctx.send(message)
        
        else:
            kill_message = choice(l.killReply)
            await ctx.send(kill_message.format(member.display_name))


    @commands.command(pass_context=True)
    async def rip(self, ctx):
        '''a basic rip command'''
        await ctx.trigger_typing()
        _choice = choice(l.rip)
        await ctx.send(_choice)

def setup(bot):
    '''cog setup'''
    bot.add_cog(basicReplies(bot))
    print('basic list commands ready')
    