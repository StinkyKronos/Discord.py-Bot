import discord
from discord.ext import commands
import random


left = (" just left the server", " bye bye")


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        member_count = len(member.guild.members)
        emoji = '<a:kid:851405152313540639>'
        welcome_embed = discord.Embed(title=f'Welcome {member.name}',
                                      description=f'You are the {member_count}th member {emoji}')
        pfp = member.avatar_url_as(size=64)
        welcome_embed.set_thumbnail(url=pfp)
        welcome_channel = member.guild.system_channel
        await welcome_channel.send(embed=welcome_embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        welcome_channel = member.guild.system_channel
        await welcome_channel.send(f'{member.mention} {random.choice(left)}')


def setup(bot):
    bot.add_cog(Welcome(bot))
