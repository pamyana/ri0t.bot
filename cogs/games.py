from random import randint, choice
import asyncio

import discord as d 
from discord import errors
from discord.ext import commands

from util import lists as l #this will be for the quiz command

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['slots'])
    async def spin(self, ctx):
        '''a slot machine that will be redone to include more features'''
        reel = [':cherries:', ':tangerine:', ':lemon:', ':pineapple:', ':apple:', ':green_apple:', ':grapes:', ':strawberry:']

        slot_a = reel[randint(0,7)]
        slot_b = reel[randint(0,7)]
        slot_c = reel[randint(0,7)]
        slot_d = reel[randint(0,7)]
        slot_e = reel[randint(0,7)]
        slot_a1 = reel[randint(0,7)]
        slot_b1 = reel[randint(0,7)]
        slot_c1 = reel[randint(0,7)]
        slot_d1 = reel[randint(0,7)]
        slot_e1 = reel[randint(0,7)]
        slot_a2 = reel[randint(0,7)]
        slot_b2 = reel[randint(0,7)]
        slot_c2 = reel[randint(0,7)]
        slot_d2 = reel[randint(0,7)]
        slot_e2 = reel[randint(0,7)]

        reels = [slot_a, slot_b, slot_c, slot_d, slot_e]
        reels1 = [slot_a1, slot_b1, slot_c1, slot_d1, slot_e1]
        reels2 = [slot_a2, slot_b2, slot_c2, slot_d2, slot_e2]

        reels = [slot_a, slot_b, slot_c, slot_d, slot_e]

        if slot_a == slot_b and slot_b == slot_c and slot_c == slot_d and slot_d == slot_e:
            result = 'JACKPOT'
        elif slot_a == slot_b and slot_b == slot_c and slot_c == slot_d or slot_b == slot_c and slot_c == slot_d and slot_d == slot_e:
            result = '4 in a row!'
        elif slot_a == slot_b and slot_b == slot_c and slot_d == slot_e:
            result = 'triple double, sweet'
        elif slot_a == slot_b and slot_c == slot_d and slot_d == slot_e:
            result = 'double triple, sweet'
        elif slot_a == slot_b and slot_b == slot_c or slot_b == slot_c and slot_c == slot_d or slot_c == slot_d and slot_d == slot_e:
            result = '3 in a row, pretty good'
        elif slot_a == slot_b and slot_c == slot_d or slot_b == slot_c and slot_d == slot_e or slot_a == slot_b and slot_d == slot_e:
            result = '2 pairs, nice'
        elif slot_a == slot_b or slot_b == slot_c or slot_c == slot_d or slot_d == slot_e:
            result = '2 in a row, not bad'
        else:
            result = 'you lose'

        embed = d.Embed(color=0xc64519)

        re = ' | '.join(reels1)
        re1 = ' | '.join(reels)
        re2 = ' | '.join(reels2)
        embed.add_field(name='ri0t slots', value='{}\n{} <-\n{}'.format(re, re1, re2))
        embed.set_footer(text='{}'.format(result))
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def roll(self, ctx, dice: str):
        '''roll a dice in NdN format'''
        try:
            rolls, limit = map(int, dice.split('d'))
        except ValueError:
            await ctx.send('NdN format plz thank')
            return
        result = ', '.join(str(randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    @commands.command(pass_context=True)
    async def rps(self, ctx, play: str):
        '''a rock paper scissors game'''
        _plays = ['rock', 'paper', 'scissors']
        comp = _plays[randint(0,2)]
        user = play.lower() 

        if user == comp:
            await ctx.send(comp+'\nwe tied, I guess')
        elif user == 'rock':
            if comp == 'paper':
                await ctx.send(comp+'\nI won, loser')
            else:
                await ctx.send(comp+'\nyou won lol')
        elif user == 'paper':
            if comp == 'scissors':
                await ctx.send(comp+'\nI won, loser')
            else:
                await ctx.send(comp+'\nyou won lol')
        elif user == 'scissors':
            if comp == 'rock':
                await ctx.send(comp+'\nI won, loser')
            else:
                await ctx.send(comp+'\nyou won lol')
        else:
            await ctx.send('that\'s not how you play rock paper scissors, dingus')

    @commands.command(pass_context=True)
    async def guess(self, ctx, gue: int):
        '''a guessing game'''
        ans = randint(1,10)
        ran = 'the range is 1 - 10, dude'

        if gue == ans:
            await ctx.send('**{}**, you guessed it lol'.format(ans))
        elif gue > 10:
            await ctx.send(ran)
        elif gue < 1:
            await ctx.send(ran)
        else:
            await ctx.send('**{}**, wrong number, loser'.format(ans))


def setup(bot):
    '''cog setup'''
    bot.add_cog(Games(bot))
    print('games ready')