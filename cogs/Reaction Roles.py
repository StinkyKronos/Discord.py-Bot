import discord
from discord.ext import commands


class RR(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        msg_id = 851566591317114890
        if msg_id == payload.message_id:
            member = payload.member
            guild = member.guild
            emoji = payload.emoji.name
            if emoji == '1846_tik':
                await member.add_roles(discord.utils.get(guild.roles, name='Member'))

        msg_id2 = 851787854702837780
        if msg_id2 == payload.message_id:
            member = payload.member
            guild = member.guild
            emoji = payload.emoji.name
            if emoji == 'phasmo':
                await member.add_roles(discord.utils.get(guild.roles, name='Phasmophobia'))
            if emoji == 'csgo':
                await member.add_roles(discord.utils.get(guild.roles, name='CS : GO'))
            if emoji == 'Amongus_pog':
                await member.add_roles(discord.utils.get(guild.roles, name='Among Us'))
            if emoji == 'pubg':
                await member.add_roles(discord.utils.get(guild.roles, name='Pubg'))
            if emoji == 'MTA':
                await member.add_roles(discord.utils.get(guild.roles, name='MTA'))
            if emoji == 'fortnite':
                await member.add_roles(discord.utils.get(guild.roles, name='Fortnite'))
            if emoji == '6853_Valorant':
                await member.add_roles(discord.utils.get(guild.roles, name='Valorant'))
            if emoji == '1987_Minecraft':
                await member.add_roles(discord.utils.get(guild.roles, name='Minecraft'))


def setup(bot):
    bot.add_cog(RR(bot))
