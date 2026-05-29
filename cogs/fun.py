from discord.ext import commands
from discord import app_commands
import discord
import random

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # =====================================
    # COINFLIP
    # =====================================

    @app_commands.command(
        name="coinflip",
        description="Flip a coin"
    )
    async def coinflip(
        self,
        interaction: discord.Interaction
    ):

        result = random.choice([
            "Heads",
            "Tails"
        ])

        embed = discord.Embed(
            title="🪙 Coin Flip",
            description=f"Result: **{result}**",
            color=discord.Color.gold()
        )

        await interaction.response.send_message(
            embed=embed
        )

    # =====================================
    # DICE
    # =====================================

    @app_commands.command(
        name="dice",
        description="Roll a dice"
    )
    async def dice(
        self,
        interaction: discord.Interaction
    ):

        result = random.randint(1, 6)

        embed = discord.Embed(
            title="🎲 Dice Roll",
            description=f"You rolled **{result}**",
            color=discord.Color.blue()
        )

        await interaction.response.send_message(
            embed=embed
        )

    # =====================================
    # 8BALL
    # =====================================

    @app_commands.command(
        name="8ball",
        description="Ask the magic 8ball"
    )
    async def eightball(
        self,
        interaction: discord.Interaction,
        question: str
    ):

        responses = [
            "Yes",
            "No",
            "Maybe",
            "Definitely",
            "Probably not",
            "100% Yes",
            "Ask again later"
        ]

        embed = discord.Embed(
            title="🎱 Magic 8Ball",
            description=(
                f"❓ {question}\n\n"
                f"🎱 {random.choice(responses)}"
            ),
            color=discord.Color.purple()
        )

        await interaction.response.send_message(
            embed=embed
        )

    # =====================================
    # HIGH LOW GAME
    # =====================================

    @app_commands.command(
        name="highlow",
        description="Guess a number between 1 and 10"
    )
    async def highlow(
        self,
        interaction: discord.Interaction,
        guess: int
    ):

        number = random.randint(1, 10)

        if guess == number:

            result = "🎉 Correct! You won!"

            color = discord.Color.green()

        else:

            result = f"❌ Wrong! Number was {number}"

            color = discord.Color.red()

        embed = discord.Embed(
            title="🎮 High Low Game",
            description=result,
            color=color
        )

        await interaction.response.send_message(
            embed=embed
        )

    # =====================================
    # TRUTH
    # =====================================

    @app_commands.command(
        name="truth",
        description="Get a truth question"
    )
    async def truth(
        self,
        interaction: discord.Interaction
    ):

        truths = [
            "What is your biggest fear?",
            "What is your most embarrassing moment?",
            "Who was your first crush?",
            "What secret have you never told anyone?",
            "What is your weirdest habit?"
        ]

        embed = discord.Embed(
            title="💬 Truth",
            description=random.choice(truths),
            color=discord.Color.orange()
        )

        await interaction.response.send_message(
            embed=embed
        )

    # =====================================
    # DARE
    # =====================================

    @app_commands.command(
        name="dare",
        description="Get a dare"
    )
    async def dare(
        self,
        interaction: discord.Interaction
    ):

        dares = [
            "Sing a song in VC.",
            "Change your nickname for 10 minutes.",
            "Send your last emoji.",
            "Type with only emojis for 5 minutes.",
            "Say something funny in general chat."
        ]

        embed = discord.Embed(
            title="🔥 Dare",
            description=random.choice(dares),
            color=discord.Color.red()
        )

        await interaction.response.send_message(
            embed=embed
        )

    # =====================================
    # TIC TAC TOE
    # =====================================

    @app_commands.command(
        name="tictactoe",
        description="Start a Tic Tac Toe game"
    )
    async def tictactoe(
        self,
        interaction: discord.Interaction,
        opponent: discord.Member
    ):

        board = (
            "⬜⬜⬜\n"
            "⬜⬜⬜\n"
            "⬜⬜⬜"
        )

        embed = discord.Embed(
            title="❌ Tic Tac Toe ⭕",
            description=(
                f"{interaction.user.mention} vs {opponent.mention}\n\n"
                f"{board}\n\n"
                f"Game system coming soon 🚀"
            ),
            color=discord.Color.blurple()
        )

        await interaction.response.send_message(
            embed=embed
        )

    # =====================================
    # MEME
    # =====================================

    @app_commands.command(
        name="meme",
        description="Get a random meme message"
    )
    async def meme(
        self,
        interaction: discord.Interaction
    ):

        memes = [
            "When code works first try 🤯",
            "Fix one bug, create ten more 💀",
            "Programmer sleep schedule.exe stopped working",
            "Turning coffee into code ☕",
            "Me: I'll sleep early today. Also me: coding at 3AM"
        ]

        embed = discord.Embed(
            title="😂 Meme",
            description=random.choice(memes),
            color=discord.Color.random()
        )

        await interaction.response.send_message(
            embed=embed
        )

async def setup(bot):
    await bot.add_cog(Fun(bot))