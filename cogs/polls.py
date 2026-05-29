import discord
from discord.ext import commands
from discord import app_commands

class Polls(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="poll", description="Create poll")
    async def poll(
        self,
        interaction: discord.Interaction,
        question: str
    ):

        embed = discord.Embed(
            title="📊 Poll",
            description=question,
            color=discord.Color.blue()
        )

        message = await interaction.channel.send(embed=embed)

        await message.add_reaction("👍")
        await message.add_reaction("👎")

        await interaction.response.send_message(
            "✅ Poll created!",
            ephemeral=True
        )

async def setup(bot):
    await bot.add_cog(Polls(bot))