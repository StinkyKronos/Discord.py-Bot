import discord
from discord.ext import commands
import os
from dotenv import load_dotenv


intents = discord.Intents.default()
intents.members = True

load_dotenv()
token = os.getenv("TOKEN")

# Prefix
bot = commands.Bot(command_prefix='`', intents=intents)
bot.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


# token
bot.run(token)
