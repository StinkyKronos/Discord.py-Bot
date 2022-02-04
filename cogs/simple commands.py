import discord
from discord.ext import commands
import random


class Simple(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        text = message.content.lower()
        if message.channel.id == 854426527147098113:
            return
        elif text.startswith(('hi', 'hey', 'hello', 'hlo', 'hai')):
            await message.reply(random.choice(("Hi there", "Greetings", "Hey", "What’s up?",
                                               "Good to see you", '<a:hello:850773688773246997>')))

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'My ping is {round(self.bot.latency * 1000)}ms')

    @commands.command()
    async def say(self, ctx, *, arg):
        await ctx.channel.purge(limit=1)
        if 'hemath' in arg:
            await ctx.send("Can't offend my owner")
        elif 'gay' in arg:
            await ctx.send('You are gay.')
        else:
            await ctx.send(arg)

    @commands.command()
    async def dm(self, ctx, member: discord.Member, *, msg):
        dm_embed = discord.Embed(title=msg, description=f'DM from {ctx.author}')
        await member.send(embed=dm_embed)
        embed = discord.Embed(title=f'Messaged {member}', description=msg)
        embed.set_footer(text=f'Requested by {ctx.author}')
        await ctx.send(embed=embed)
        await ctx.message.delete()
        return

    @dm.error
    async def dm_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(title='Error',
                                  description='You either mentioned a non-existing member or format was wrong',
                                  colour=0xf54242)
            embed.add_field(name='Format', value='!dm @StinkyKronos Hello', inline=False)
            await ctx.send(embed=embed)

    @commands.command()
    async def toss(self, ctx):
        choice = ('head', 'tail')
        bot_decision = random.choice(choice)
        embed_head = discord.Embed(title='**Head**')
        embed_head.set_image(url='https://i.ibb.co/qWfnH1Y/Head.png')
        embed_tail = discord.Embed(title='**Tail**')
        embed_tail.set_image(url='https://i.ibb.co/whTB4cj/Tail.png')
        if bot_decision == 'head':
            await ctx.send(embed=embed_head)
        if bot_decision == 'tail':
            await ctx.send(embed=embed_tail)

    @commands.command()
    async def join(self, ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        await ctx.send('**Joined**')

    @commands.command()
    async def dc(self, ctx):
        if ctx.voice_client:
            await ctx.guild.voice_client.disconnect()
            await ctx.send('**Disconnected**')


def setup(bot):
    bot.add_cog(Simple(bot))
