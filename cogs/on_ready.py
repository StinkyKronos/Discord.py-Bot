import nextcord
from nextcord.ext import commands
import asyncio


class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("|BOT IS UP AND RUNNING|")
        # while 1:
        #     await self.bot.change_presence(
        #         activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="Yo Momma!"))
        #     await asyncio.sleep(5)
        #     await self.bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name="!help"))
        #     await asyncio.sleep(5)


def setup(bot):
    bot.add_cog(Ready(bot))
