from discord.ext import commands
from discord import app_commands
import discord

class Welcome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.welcome_channels = {}

    # =====================================
    # SET WELCOME CHANNEL
    # =====================================

    @app_commands.command(
        name="setwelcomechannel",
        description="Set the welcome channel"
    )
    async def setwelcomechannel(
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

        self.welcome_channels[
            interaction.guild.id
        ] = channel.id

        embed = discord.Embed(
            title="✅ Welcome Channel Set",
            description=(
                f"Welcome messages will now appear in "
                f"{channel.mention}"
            ),
            color=discord.Color.green()
        )

        await interaction.response.send_message(
            embed=embed
        )

    # =====================================
    # MEMBER JOIN
    # =====================================

    @commands.Cog.listener()
    async def on_member_join(self, member):

        guild_id = member.guild.id

        channel_id = self.welcome_channels.get(guild_id)

        if not channel_id:
            return

        channel = self.bot.get_channel(channel_id)

        if not channel:
            return

        # =====================================
        # WELCOME EMBED
        # =====================================

        embed = discord.Embed(
            title="🌿 Welcome to the Server!",
            description=(
                f"Hey {member.mention} 👋\n\n"
                f"Welcome to **{member.guild.name}**\n"
                f"We're happy to have you here 🚀"
            ),
            color=discord.Color.blurple()
        )

        embed.set_thumbnail(
            url=member.display_avatar.url
        )

        embed.set_image(
            url="https://images.unsplash.com/photo-1506744038136-46273834b3fb"
        )

        embed.add_field(
            name="📚 Getting Started",
            value=(
                "• Read the rules\n"
                "• Introduce yourself\n"
                "• Explore channels\n"
                "• Use `/help` for commands"
            ),
            inline=False
        )

        embed.add_field(
            name="🤖 Useful Commands",
            value=(
                "`/ai` → Talk with AI\n"
                "`/level` → Check level\n"
                "`/ticket` → Create support ticket\n"
                "`/ping` → Check bot latency"
            ),
            inline=False
        )

        embed.add_field(
            name="👥 Member Count",
            value=f"{member.guild.member_count}",
            inline=True
        )

        embed.add_field(
            name="⭐ Your Role",
            value="New Member",
            inline=True
        )

        embed.set_footer(
            text=f"User ID: {member.id}"
        )

        await channel.send(
            content=f"🎉 Welcome {member.mention}!",
            embed=embed
        )

    # =====================================
    # MEMBER LEAVE
    # =====================================

    @commands.Cog.listener()
    async def on_member_remove(self, member):

        guild_id = member.guild.id

        channel_id = self.welcome_channels.get(guild_id)

        if not channel_id:
            return

        channel = self.bot.get_channel(channel_id)

        if not channel:
            return

        embed = discord.Embed(
            title="👋 Member Left",
            description=(
                f"**{member.name}** has left the server."
            ),
            color=discord.Color.red()
        )

        embed.set_thumbnail(
            url=member.display_avatar.url
        )

        embed.add_field(
            name="Current Members",
            value=f"{member.guild.member_count}",
            inline=True
        )

        await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Welcome(bot))