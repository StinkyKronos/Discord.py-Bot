import nextcord
from nextcord.ext import commands
import random


class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dice(self, ctx):
        dice = random.randint(1, 6)
        embed_1 = nextcord.Embed(title=f'Rolled a {dice}')
        embed_1.set_image(url='https://i.ibb.co/R67Z1NG/Dice1.jpg')
        embed_2 = nextcord.Embed(title=f'Rolled a {dice}')
        embed_2.set_image(url='https://i.ibb.co/cJkp7Nb/Dice2.jpg')
        embed_3 = nextcord.Embed(title=f'Rolled a {dice}')
        embed_3.set_image(url='https://i.ibb.co/HnnZX67/Dice3.jpg')
        embed_4 = nextcord.Embed(title=f'Rolled a {dice}')
        embed_4.set_image(url='https://i.ibb.co/XS8Trz8/Dice4.jpg')
        embed_5 = nextcord.Embed(title=f'Rolled a {dice}')
        embed_5.set_image(url='https://i.ibb.co/GJDRDj6/Dice5.jpg')
        embed_6 = nextcord.Embed(title=f'Rolled a {dice}')
        embed_6.set_image(url='https://i.ibb.co/mtWgTr1/Dice6.jpg')
        if dice == 1:
            await ctx.send(embed=embed_1)
        if dice == 2:
            await ctx.send(embed=embed_2)
        if dice == 3:
            await ctx.send(embed=embed_3)
        if dice == 4:
            await ctx.send(embed=embed_4)
        if dice == 5:
            await ctx.send(embed=embed_5)
        if dice == 6:
            await ctx.send(embed=embed_6)



def setup(bot):
    bot.add_cog(Dice(bot))
