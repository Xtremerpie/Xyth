from discord.ext import commands
from discord import app_commands
import discord

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.balance_data = {}

    @app_commands.command(
        name="balance",
        description="Check your balance"
    )
    async def balance(
        self,
        interaction: discord.Interaction
    ):

        user = str(interaction.user.id)

        if user not in self.balance_data:
            self.balance_data[user] = 0

        await interaction.response.send_message(
            f"💰 Balance: ${self.balance_data[user]}"
        )

    @app_commands.command(
        name="daily",
        description="Claim daily reward"
    )
    async def daily(
        self,
        interaction: discord.Interaction
    ):

        user = str(interaction.user.id)

        if user not in self.balance_data:
            self.balance_data[user] = 0

        self.balance_data[user] += 100

        await interaction.response.send_message(
            "🎉 You received $100"
        )

async def setup(bot):
    await bot.add_cog(Economy(bot))