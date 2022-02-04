import discord
from discord.ext import commands
import asyncio
from discord.ext.commands import MissingPermissions, has_permissions


class KickBan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        kick_embed = discord.Embed(title=f'Kicked from {ctx.guild.name}', description=f'{member.mention} was kicked.',
                                   color=0xf54242)
        kick_embed.add_field(name='Reason', value=reason)
        await ctx.send(embed=kick_embed)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to Ban or Kick members.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        ban_embed = discord.Embed(title=f'Banned from {ctx.guild.name}',
                                  description=f'{member.mention} was banned. <a:alert:861817910875389963>',
                                  color=0xf54242)
        ban_embed.add_field(name='Reason', value=reason)
        await ctx.send(embed=ban_embed)
        await member.send(embed=ban_embed)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to Ban or Kick members.")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, number=0):
        delete_embed = discord.Embed(title='Deleted', description=f'Deleted {number} messages')
        if number == 0:
            await ctx.send('Please use the format eg: !clear 10')

        else:
            await ctx.channel.purge(limit=number)
            bot_msg = await ctx.send(embed=delete_embed)
            await asyncio.sleep(5)
            await bot_msg.delete()

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have manage_messages permission")

    @commands.command()
    async def whois(self, ctx, member: discord.Member):
        join_date = member.joined_at.strftime('%A, %B %d, %Y')
        embed = discord.Embed(title=f'Info of {member}', description=f'Joined on {join_date}')
        pfp = member.avatar_url
        embed.set_thumbnail(url=pfp)
        embed.add_field(name='Username', value=str(member))
        date = member.created_at.strftime('%A, %B %d, %Y')
        embed.add_field(name='Account Created on', value=date)
        embed.set_footer(text=f'Requested by {ctx.author}')
        roles = []
        for role in member.roles:
            roles.append(role.mention)
        roles = roles[1:]
        roles = ", ".join(roles)
        embed.add_field(name='Roles', inline=False, value=roles)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(KickBan(bot))
