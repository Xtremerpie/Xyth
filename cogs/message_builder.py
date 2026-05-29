import discord
from discord.ext import commands
from discord import app_commands


class MessageBuilder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # =====================================
    # CUSTOM EMBED BUILDER
    # =====================================

    import discord
from discord.ext import commands
from discord import app_commands


class MessageBuilder(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # =====================================
    # EMBED COMMAND
    # =====================================

    @app_commands.command(
        name="embed",
        description="Create a professional embed"
    )
    async def embed(
        self,
        interaction: discord.Interaction,
        channel: discord.TextChannel,
        title: str,
        description: str
    ):

        formatted_description = description.replace("\\n", "\n")

        embed = discord.Embed(
            title=title,
            description=formatted_description,
            color=discord.Color.blurple()
        )

        if interaction.guild.icon:
            embed.set_thumbnail(
                url=interaction.guild.icon.url
            )

        embed.set_footer(
            text=f"{interaction.guild.name}"
        )

        await channel.send(embed=embed)

        await interaction.response.send_message(
            f"✅ Embed sent to {channel.mention}",
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(MessageBuilder(bot))

    # =====================================
    # PROFESSIONAL RULES EMBED
    # =====================================

    @app_commands.command(
        name="rules",
        description="Send professional server rules"
    )
    async def rules(
        self,
        interaction: discord.Interaction,
        channel: discord.TextChannel
    ):

        embed = discord.Embed(
            title="🌌 Xyth Community Rules",
            description=(
                "**Welcome to the official Xyth Discord Server!**\n\n"
                "This community is built for creators, developers, gamers, "
                "and chill people who want to grow together.\n\n"
                "Please read all rules carefully before chatting."
            ),
            color=discord.Color.purple()
        )

        # SERVER ICON
        if interaction.guild.icon:
            embed.set_thumbnail(url=interaction.guild.icon.url)

        # RULES
        embed.add_field(
            name="📜 1 • Respect Everyone",
            value=(
                "• No harassment\n"
                "• No bullying\n"
                "• No hate speech\n"
                "• Respect all members"
            ),
            inline=False
        )

        embed.add_field(
            name="🚫 2 • No Spamming",
            value=(
                "• No message spam\n"
                "• No emoji spam\n"
                "• No mention spam\n"
                "• No flood messages"
            ),
            inline=False
        )

        embed.add_field(
            name="🔞 3 • No NSFW Content",
            value=(
                "NSFW or disturbing content is strictly prohibited.\n"
                "Including images, videos, links, profiles, or usernames."
            ),
            inline=False
        )

        embed.add_field(
            name="📢 4 • No Advertising",
            value=(
                "Do not advertise:\n"
                "• Servers\n"
                "• YouTube channels\n"
                "• Services\n"
                "without staff permission."
            ),
            inline=False
        )

        embed.add_field(
            name="💬 5 • Use Channels Correctly",
            value=(
                "Use the correct channels for:\n"
                "• Bot commands\n"
                "• Media sharing\n"
                "• Support tickets\n"
                "• General chat"
            ),
            inline=False
        )

        embed.add_field(
            name="⚔️ 6 • No Toxicity",
            value=(
                "Debates are okay.\n"
                "Personal attacks, drama, and toxic fights are not."
            ),
            inline=False
        )

        embed.add_field(
            name="🤖 7 • Bot Rules",
            value=(
                "• Do not abuse bot commands\n"
                "• No command spam\n"
                "• Do not attempt exploits"
            ),
            inline=False
        )

        embed.add_field(
            name="🎫 8 • Support Rules",
            value=(
                "When opening a ticket:\n"
                "• Explain clearly\n"
                "• Be patient\n"
                "• Avoid ping spam"
            ),
            inline=False
        )

        embed.add_field(
            name="⚠️ Punishments",
            value=(
                "Depending on severity:\n"
                "• Warning\n"
                "• Timeout\n"
                "• Kick\n"
                "• Ban"
            ),
            inline=False
        )

        embed.add_field(
            name="🌟 Final Message",
            value=(
                "**Build • Create • Learn • Grow 🚀**\n"
                "Thank you for being part of Xyth."
            ),
            inline=False
        )

        embed.set_footer(
            text="Xyth Moderation System"
        )

        await channel.send(embed=embed)

        await interaction.response.send_message(
            "✅ Professional rules embed sent!",
            ephemeral=True
        )

    # =====================================
    # SUPPORT MESSAGE
    # =====================================

    @app_commands.command(
        name="supportmsg",
        description="Create support/ticket message"
    )
    async def supportmsg(
        self,
        interaction: discord.Interaction,
        channel: discord.TextChannel
    ):

        embed = discord.Embed(
            title="🎫 Xyth Support Center",
            description=(
                "**Need help?**\n\n"
                "Use the command below to create a support ticket.\n\n"
                "`/ticket`\n\n"
                "Our support team will assist you as soon as possible."
            ),
            color=discord.Color.green()
        )

        embed.add_field(
            name="📌 Support Includes",
            value=(
                "• Bot Help\n"
                "• Reports\n"
                "• Partnership\n"
                "• Technical Support"
            ),
            inline=False
        )

        if interaction.guild.icon:
            embed.set_thumbnail(url=interaction.guild.icon.url)

        embed.set_footer(
            text="Xyth Ticket System"
        )

        await channel.send(embed=embed)

        await interaction.response.send_message(
            "✅ Support message sent!",
            ephemeral=True
        )

    # =====================================
    # ANNOUNCEMENT MESSAGE
    # =====================================

    @app_commands.command(
        name="announce",
        description="Send server announcement"
    )
    async def announce(
        self,
        interaction: discord.Interaction,
        channel: discord.TextChannel,
        message: str
    ):

        embed = discord.Embed(
            title="📢 Xyth Announcement",
            description=message,
            color=discord.Color.gold()
        )

        if interaction.guild.icon:
            embed.set_thumbnail(url=interaction.guild.icon.url)

        embed.set_footer(
            text=f"Announcement by {interaction.user}"
        )

        await channel.send("@everyone", embed=embed)

        await interaction.response.send_message(
            "✅ Announcement sent!",
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(MessageBuilder(bot))