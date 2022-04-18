import nextcord
from nextcord.ext import commands
import random

answers = ["It is certain",
           "It is decidedly so",
           "Without a doubt",
           "Yes, definitely",
           "You may rely on it",
           "As I see it, yes",
           "Most likely",
           "Outlook good",
           "Yes",
           "Signs point to yes",
           "Reply hazy try again",
           "Ask again later",
           "Better not tell you now",
           "Cannot predict now",
           "Concentrate and ask again",
           "Don't count on it",
           "My reply is no",
           "My sources say no",
           "Outlook not so good",
           "Very doubtful"]


class Eight(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball')
    async def eight_ball(self, ctx, *, question=''):
        if question == '':
            await ctx.send('Use format **!8ball <question>**')
        else:
            decision = random.choice(answers)
            embed = nextcord.Embed(title='__8Ball__')
            embed.add_field(name=f'{question}?', value=decision)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Eight(bot))
