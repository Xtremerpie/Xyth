import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio

# =========================
# LOAD ENV
# =========================
load_dotenv()

TOKEN = os.getenv("TOKEN")

# =========================
# BOT INTENTS
# =========================
intents = discord.Intents.default()

intents.message_content = True
intents.members = True
intents.guilds = True
intents.messages = True
intents.voice_states = True

# =========================
# BOT SETUP
# =========================
bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None
)

# =========================
# EXTENSIONS / COGS
# =========================
extensions = [

    # CORE
    "cogs.utility",
    "cogs.fun",
    "cogs.moderation",

    # LEVELING
    "cogs.leveling",

    # AI
    "cogs.ai_chat",

    # AUTOMOD
    "cogs.antispam",
    "cogs.automod",

    # ECONOMY
    "cogs.economy",

    # LOGGING
    "cogs.logs",

    # WELCOME SYSTEM
    "cogs.welcome",

    # TICKETS
    "cogs.tickets",

    # NEW FEATURES
    "cogs.invites",
    "cogs.counter",
    "cogs.giveaway",
    "cogs.afk",
    "cogs.message_builder",
    "cogs.status",
    "cogs.polls"
]

# =========================
# EVENTS
# =========================
@bot.event
async def on_ready():

    print("=" * 40)
    print(f"{bot.user} is online!")
    print("=" * 40)

    try:
        synced = await bot.tree.sync()

        print(f"Synced {len(synced)} slash commands")

    except Exception as e:
        print(e)

# =========================
# LOAD COGS
# =========================
async def load_extensions():

    for extension in extensions:

        try:
            await bot.load_extension(extension)

            print(f"Loaded {extension}")

        except Exception as e:

            print(f"Failed {extension}: {e}")

# =========================
# MAIN
# =========================
async def main():

    async with bot:

        await load_extensions()

        await bot.start(TOKEN)

# =========================
# RUN BOT
# =========================
asyncio.run(main())