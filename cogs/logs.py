from discord.ext import commands
import discord

class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):

        channel = discord.utils.get(
            message.guild.text_channels,
            name="logs"
        )

        if channel:
            embed = discord.Embed(
                title="Message Deleted",
                description=message.content,
                color=discord.Color.red()
            )

            await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Logs(bot))