import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Help", color=0x00c6ff)
        embed.add_field(name='Commands:', value='''
        - **!rps**
        - **!toss**
        - **!youtube**
        - **!dm**
        - **!ping**
        - **!say**  
        - **!whois**
        - **!8ball**
        - **!dice**
        - **!wanted**
        - **!worthless**''')

        embed.add_field(name='!rps', value='Starts a game of Rock, Paper and Scissor.', inline=False)
        embed.add_field(name='!toss', value='Tosses a virtual coin.', inline=False)
        embed.add_field(name='!youtube <search term>', value='Searches youtube.', inline=False)
        embed.add_field(name='!dm <username/user_id> <Message to be sent>',
                        value="Dm's a user of choice. Can only be used by verified members.", inline=False)
        embed.add_field(name='!ping', value='Shows bots ping', inline=False)
        embed.add_field(name='!say <message to be repeated>', value='Repeats a Message you send', inline=False)
        embed.add_field(name='!whois <username/user_id>', value='Shows info on the user', inline=False)
        embed.add_field(name='!8ball <Question>', value='You know what it does', inline=False)
        embed.add_field(name='!Dice', value='Rolls a dice', inline=False)
        embed.add_field(name='!wanted <username>', value='Wanted Poster', inline=False)
        embed.add_field(name='!worthless <username>', value='A meme template', inline=False)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            embed = discord.Embed(title='Command not Found', description='Use !help to see usable commands',
                                  colour=0xf54242)
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(5)
            await msg.delete()
            await ctx.message.delete()


def setup(bot):
    bot.add_cog(Help(bot))
