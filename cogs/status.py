import discord
from discord.ext import commands, tasks
import asyncio

STATUS_CHANNEL_NAME = "bot-status"


class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.status_message = None
        self.update_status.start()

    def cog_unload(self):
        self.update_status.cancel()

    @tasks.loop(seconds=30)
    async def update_status(self):

        await self.bot.wait_until_ready()

        for guild in self.bot.guilds:

            channel = discord.utils.get(
                guild.text_channels,
                name=STATUS_CHANNEL_NAME
            )

            if not channel:
                continue

            latency = round(self.bot.latency * 1000)

            embed = discord.Embed(
                title="🟢 Xyth Bot Status",
                description="Real-time bot monitoring system",
                color=discord.Color.green()
            )

            embed.add_field(
                name="🤖 Bot",
                value=f"{self.bot.user}",
                inline=True
            )

            embed.add_field(
                name="📡 Ping",
                value=f"{latency}ms",
                inline=True
            )

            embed.add_field(
                name="🌍 Servers",
                value=f"{len(self.bot.guilds)}",
                inline=True
            )

            embed.add_field(
                name="👥 Users",
                value=f"{len(self.bot.users)}",
                inline=True
            )

            embed.add_field(
                name="⚡ Status",
                value="Online",
                inline=True
            )

            embed.add_field(
                name="🛠️ System",
                value="All systems operational",
                inline=True
            )

            embed.set_footer(
                text="Updates every 30 seconds"
            )

            if self.bot.user.avatar:
                embed.set_thumbnail(
                    url=self.bot.user.avatar.url
                )

            try:

                # CHECK OLD MESSAGE
                if self.status_message:

                    await self.status_message.edit(
                        embed=embed
                    )

                else:

                    self.status_message = await channel.send(
                        embed=embed
                    )

            except:

                self.status_message = await channel.send(
                    embed=embed
                )


async def setup(bot):
    await bot.add_cog(Status(bot))