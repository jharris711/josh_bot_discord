import os
import random
from dotenv import load_dotenv
import discord
from discord.ext import commands

# ----------------------------- Load dotenv vars ----------------------------- #
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

#client = discord.Client()
bot = commands.Bot(command_prefix='!')

class Bot(commands.Bot):
    

# ------------------------------- Bot is ready ------------------------------- #
@bot.event
async def on_ready():
    print(f'-> Bot has been logged in as {bot.user.name} ID:{bot.user.id}')
    print('----------------------------------------------------------------')
    print("Running...")


# ----------------------- When new member joins server ----------------------- #
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@bot.command(name='99')
async def nine_nine(ctx):
    """Responds with a random quote from Brooklyn 99"""
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)




bot.run(token)