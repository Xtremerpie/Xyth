from discord.ext import commands
from discord import app_commands
import discord

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="ping",
        description="Check bot latency"
    )
    async def ping(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            f"🏓 Pong! {round(self.bot.latency * 1000)}ms"
        )

    @app_commands.command(
        name="serverinfo",
        description="Shows server information"
    )
    async def serverinfo(self, interaction: discord.Interaction):

        guild = interaction.guild

        embed = discord.Embed(
            title=guild.name,
            description=f"Members: {guild.member_count}",
            color=discord.Color.blurple()
        )

        await interaction.response.send_message(
            embed=embed
        )

async def setup(bot):
    await bot.add_cog(Utility(bot))