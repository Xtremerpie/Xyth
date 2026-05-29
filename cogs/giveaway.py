import discord
from discord.ext import commands
from discord import app_commands
import random
import asyncio

class Giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="gstart", description="Start giveaway")
    async def gstart(
        self,
        interaction: discord.Interaction,
        duration: int,
        prize: str
    ):

        embed = discord.Embed(
            title="🎉 GIVEAWAY 🎉",
            description=f"Prize: **{prize}**\nReact with 🎉",
            color=discord.Color.gold()
        )

        message = await interaction.channel.send(embed=embed)
        await message.add_reaction("🎉")

        await interaction.response.send_message("Giveaway started!", ephemeral=True)

        await asyncio.sleep(duration)

        message = await interaction.channel.fetch_message(message.id)

        users = []

        for reaction in message.reactions:
            if str(reaction.emoji) == "🎉":
                async for user in reaction.users():
                    if not user.bot:
                        users.append(user)

        if users:
            winner = random.choice(users)

            await interaction.channel.send(
                f"🏆 Winner: {winner.mention}"
            )

async def setup(bot):
    await bot.add_cog(Giveaway(bot))