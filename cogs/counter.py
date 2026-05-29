import discord
from discord.ext import commands, tasks
from discord import app_commands

class Counter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.update_channels.start()

    @tasks.loop(minutes=5)
    async def update_channels(self):
        for guild in self.bot.guilds:
            member_count = guild.member_count

            for channel in guild.voice_channels:
                if "Members:" in channel.name:
                    await channel.edit(name=f"Members: {member_count}")

    @app_commands.command(name="setupcounter", description="Create member counter")
    async def setupcounter(self, interaction: discord.Interaction):

        guild = interaction.guild

        await guild.create_voice_channel(
            name=f"Members: {guild.member_count}"
        )

        await interaction.response.send_message(
            "✅ Counter channel created!"
        )

async def setup(bot):
    await bot.add_cog(Counter(bot))