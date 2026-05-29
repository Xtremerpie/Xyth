from discord.ext import commands
from discord import app_commands
import discord
import math

class Leveling(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.user_xp = {}
        self.level_channels = {}

    # =========================
    # XP SYSTEM
    # =========================

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        user_id = str(message.author.id)

        if user_id not in self.user_xp:

            self.user_xp[user_id] = {
                "xp": 0,
                "level": 1
            }

        data = self.user_xp[user_id]

        data["xp"] += 15

        xp = data["xp"]

        new_level = int(math.sqrt(xp // 100)) + 1

        if new_level > data["level"]:

            data["level"] = new_level

            guild_id = message.guild.id

            channel_id = self.level_channels.get(guild_id)

            if channel_id:

                channel = self.bot.get_channel(channel_id)

            else:

                channel = message.channel

            embed = discord.Embed(
                title="🎉 LEVEL UP!",
                description=(
                    f"Congratulations {message.author.mention}\n\n"
                    f"You reached **Level {new_level}** 🚀"
                ),
                color=discord.Color.gold()
            )

            embed.set_thumbnail(
                url=message.author.display_avatar.url
            )

            embed.add_field(
                name="Current XP",
                value=f"{xp}",
                inline=True
            )

            embed.add_field(
                name="New Level",
                value=f"{new_level}",
                inline=True
            )

            embed.set_footer(
                text="Keep chatting to gain more XP!"
            )

            await channel.send(embed=embed)

    # =========================
    # LEVEL COMMAND
    # =========================

    @app_commands.command(
        name="level",
        description="Check your level and XP"
    )
    async def level(
        self,
        interaction: discord.Interaction
    ):

        user_id = str(interaction.user.id)

        if user_id not in self.user_xp:

            self.user_xp[user_id] = {
                "xp": 0,
                "level": 1
            }

        data = self.user_xp[user_id]

        embed = discord.Embed(
            title=f"{interaction.user.name}'s Profile",
            color=discord.Color.blurple()
        )

        embed.set_thumbnail(
            url=interaction.user.display_avatar.url
        )

        embed.add_field(
            name="⭐ Level",
            value=data["level"],
            inline=True
        )

        embed.add_field(
            name="⚡ XP",
            value=data["xp"],
            inline=True
        )

        embed.add_field(
            name="📈 Next Level XP",
            value=(data["level"] * 100),
            inline=False
        )

        await interaction.response.send_message(
            embed=embed
        )

    # =========================
    # SET LEVEL CHANNEL
    # =========================

    @app_commands.command(
        name="setlevelchannel",
        description="Set level-up announcement channel"
    )
    async def setlevelchannel(
        self,
        interaction: discord.Interaction,
        channel: discord.TextChannel
    ):

        if not interaction.user.guild_permissions.manage_channels:

            await interaction.response.send_message(
                "❌ You need Manage Channels permission.",
                ephemeral=True
            )

            return

        self.level_channels[
            interaction.guild.id
        ] = channel.id

        embed = discord.Embed(
            title="✅ Level Channel Set",
            description=(
                f"Level-up messages will now appear in "
                f"{channel.mention}"
            ),
            color=discord.Color.green()
        )

        await interaction.response.send_message(
            embed=embed
        )

async def setup(bot):
    await bot.add_cog(Leveling(bot))