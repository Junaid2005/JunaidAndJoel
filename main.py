import discord
from discord.ext import commands
import yaml

with open("keys.yaml", "r") as file:
    config = yaml.safe_load(file)

botToken = config["discord"]["token"]
bot = commands.Bot(command_prefix='', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # thats how u send a msg
    # await message.channel.send(f"shut up you freak {message.author}")

    print(f"{message.author}: {message.content}")

bot.run(botToken)
