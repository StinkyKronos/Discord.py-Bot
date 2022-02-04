from PIL import Image
import discord
from discord.ext import commands
from io import BytesIO


class ImageManipulation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wanted(self, ctx, member: discord.Member = ''):
        if member == '':
            member = ctx.author

        wanted = Image.open('Images/Wanted.jpg')

        asset = member.avatar_url_as(size=256)
        data = BytesIO(await asset.read())

        pfp = Image.open(data)

        pfp = pfp.resize((255, 255))
        wanted.paste(pfp, (98, 200))
        wanted.save('Images/result_wanted.png')
        await ctx.send(file=discord.File('Images/result_wanted.png'))

    @commands.command()
    async def worthless(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        meme = Image.open('Images/meme.jpg')
        pfp_asset = member.avatar_url_as(size=128)
        data = BytesIO(await pfp_asset.read())
        pfp = Image.open(data)
        pfp.resize((100, 100))
        meme.paste(pfp, (160, 80))
        meme.save('Images/result_meme.png')

        await ctx.send(file=discord.File('Images/result_meme.png'))


def setup(bot):
    bot.add_cog(ImageManipulation(bot))
