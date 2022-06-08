import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv
from time import sleep


intents = nextcord.Intents.default()
intents.members = True

load_dotenv()
token = os.getenv("TOKEN")

# Prefix
bot = commands.Bot(command_prefix=["`", "slave ", "!! "], intents=intents)
bot.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
   
@bot.command()
async def reload(ctx):
    id = 762637497020317726

    if ctx.author.id == id:
        print("\n")
        reloadingEmbed = nextcord.Embed(title="Reloading...", color=0xFFFFFF)

        msg = await ctx.send(embed=reloadingEmbed)

        for extension in os.listdir("cogs"):
            if extension.endswith(".py"):
                bot.reload_extension(f"cogs.{extension[:-3]}")
                print(f"{extension} was reloaded")
        sleep(2)
        loadedEmbed = nextcord.Embed(title=" <a:Danceowo:984137073571266581> Reloaded!", color=0xFFFFFF)
        await msg.edit(embed=loadedEmbed)
    else:
        embed = nextcord.Embed(title="You dont have the permission to restart the bot.", color=0xFF0000)
        await ctx.send(embed=embed)

# token
bot.run(token)
