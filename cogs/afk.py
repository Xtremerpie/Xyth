import discord
from discord.ext import commands
from discord import app_commands

afk_users = {}

class AFK(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="afk", description="Set AFK")
    async def afk(self, interaction: discord.Interaction, reason: str = "AFK"):

        afk_users[interaction.user.id] = reason

        await interaction.response.send_message(
            f"😴 You are now AFK: {reason}"
        )

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        if message.author.id in afk_users:
            del afk_users[message.author.id]

            await message.channel.send(
                f"👋 Welcome back {message.author.mention}"
            )

        for user in message.mentions:
            if user.id in afk_users:
                await message.channel.send(
                    f"{user.name} is AFK: {afk_users[user.id]}"
                )

async def setup(bot):
    await bot.add_cog(AFK(bot))