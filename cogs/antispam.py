from discord.ext import commands
from collections import defaultdict
import time

class AntiSpam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_messages = defaultdict(list)

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        now = time.time()

        self.user_messages[message.author.id].append(now)

        recent = [
            msg for msg in self.user_messages[message.author.id]
            if now - msg < 5
        ]

        self.user_messages[message.author.id] = recent

        if len(recent) > 5:
            await message.channel.send(
                f"{message.author.mention} stop spamming."
            )

async def setup(bot):
    await bot.add_cog(AntiSpam(bot))