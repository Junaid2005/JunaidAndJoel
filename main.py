import discord
from discord.ext import commands
import yaml
import signal
import asyncio

from core.logger import logger
from databases.users import UserDB

bot = commands.Bot(command_prefix='-', intents=discord.Intents.all())


def safe_shutdown(signal, frame):
    logger.info("Graceful shutdown initiated...")
    loop = asyncio.get_event_loop()
    loop.create_task(shutdown())


async def shutdown():
    await bot.close()
    logger.info("Bot has been safely disconnected. Cleanup complete.")
    usersDb.close()


@bot.event
async def on_ready():
    logger.info(f"Logged in as {bot.user}!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.author.id not in users:
        usersDb.initUser(message.author.id)
        users.append(message.author.id)

    # that's how u send a msg
    # await message.channel.send(f"shut up you freak {message.author}")

    logger.info(f"{message.author.id}: {message.content}")


usersDb = UserDB()
users = usersDb.loadUsers()

signal.signal(signal.SIGINT, safe_shutdown)

with open("data/keys.yaml", "r") as file:
    config = yaml.safe_load(file)
botToken = config["discord"]["token"]
bot.run(botToken)