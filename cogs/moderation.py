from discord.ext import commands
from discord import app_commands
import discord

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="clear",
        description="Delete messages"
    )
    async def clear(
        self,
        interaction: discord.Interaction,
        amount: int
    ):

        if not interaction.user.guild_permissions.manage_messages:
            await interaction.response.send_message(
                "No permission.",
                ephemeral=True
            )
            return

        await interaction.channel.purge(limit=amount)

        await interaction.response.send_message(
            f"Deleted {amount} messages.",
            ephemeral=True
        )

    @app_commands.command(
        name="kick",
        description="Kick a member"
    )
    async def kick(
        self,
        interaction: discord.Interaction,
        member: discord.Member
    ):

        await member.kick()

        await interaction.response.send_message(
            f"Kicked {member}"
        )

async def setup(bot):
    await bot.add_cog(Moderation(bot))