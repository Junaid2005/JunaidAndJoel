import discord
from discord.ext import commands
import yaml

with open("keys.yaml", "r") as file:
    config = yaml.safe_load(file)

botToken = config["discord"]["token"]
bot = commands.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print(f"{message.author}: {message.content}\n")

bot.run(botToken)
