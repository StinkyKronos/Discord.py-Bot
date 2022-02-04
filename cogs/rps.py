import discord
from discord.ext import commands
import random
RPS_START = False
RPS_AUTHOR = None
human_decision = ''
channel = ''
reply = ''
msg = ''


class RPS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rps(self, ctx):
        global RPS_START, RPS_AUTHOR, channel, msg
        channel = ctx.channel
        embed = discord.Embed(title="**Rock Paper Scissor**")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('🪨')
        await msg.add_reaction('📰')
        await msg.add_reaction('✂')
        RPS_START = True
        RPS_AUTHOR = ctx.message.author.name

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        global RPS_START, RPS_AUTHOR, human_decision, channel, reply, msg
        if RPS_START is False or payload.member.name != RPS_AUTHOR or payload.member.bot:
            return
        elif payload.emoji.name == '🪨':
            human_decision = 'rock'
        elif payload.emoji.name == '📰':
            human_decision = 'paper'
        elif payload.emoji.name == '✂':
            human_decision = 'scissor'
        await msg.delete()

        rock_paper_scissors = ('rock', 'paper', 'scissor')
        bot_decision = (random.choice(rock_paper_scissors)).lower()

        if human_decision in ['rock', 'paper', 'scissor']:
            if human_decision == bot_decision:
                reply = 'tie'
            elif human_decision == 'rock' and bot_decision == 'paper':
                reply = 'lost'
            elif human_decision == 'paper' and bot_decision == 'rock':
                reply = 'win'
            elif human_decision == 'scissor' and bot_decision == 'paper':
                reply = 'win'
            elif human_decision == 'paper' and bot_decision == 'scissor':
                reply = 'lost'
            elif human_decision == 'stone' and bot_decision == 'scissor':
                reply = 'win'
            elif human_decision == 'scissor' and bot_decision == 'rock':
                reply = 'lost'

        embed_win = discord.Embed(title='**Victory**',
                                  description=f'I chose **{bot_decision}** and {RPS_AUTHOR} chose **{human_decision}**',
                                  color=0x42f557)
        embed_win.set_footer(text=payload.member)
        embed_lost = discord.Embed(title='**Lost**',
                                   description=
                                   f'I chose **{bot_decision}** and {RPS_AUTHOR} chose **{human_decision}**',
                                   color=0xf54242)
        embed_lost.set_footer(text=payload.member)
        embed_tie = discord.Embed(title='**Tie**',
                                  description=
                                  f'I chose **{bot_decision}** and {RPS_AUTHOR} chose **{human_decision}**',
                                  color=0xffcc00)
        embed_tie.set_footer(text=payload.member)

        if reply == 'tie':
            await channel.send(embed=embed_tie)
        if reply == 'win':
            await channel.send(embed=embed_win)
        if reply == 'lost':
            await channel.send(embed=embed_lost)


def setup(bot):
    bot.add_cog(RPS(bot))
