from discord.ext import commands
import discord

BAD_WORDS = [
    "sex",
    "porn",
    "fuck"
]

class AutoMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        content = message.content.lower()

        if any(word in content for word in BAD_WORDS):

            await message.delete()

            embed = discord.Embed(
                title="Auto Moderation",
                description=f"{message.author.mention}, that word is not allowed.",
                color=discord.Color.red()
            )

            await message.channel.send(embed=embed, delete_after=5)

async def setup(bot):
    await bot.add_cog(AutoMod(bot))