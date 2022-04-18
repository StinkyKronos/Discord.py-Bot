from nextcord.ext import commands
import urllib.request
import re


class YT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def youtube(self, ctx, *, search):
        search_keyword = search.replace(' ', '+')
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        await ctx.send("https://www.youtube.com/watch?v=" + video_ids[0])


def setup(bot):
    bot.add_cog(YT(bot))