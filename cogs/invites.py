import discord
from discord.ext import commands
from discord import app_commands

class Invites(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.invites = {}

    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            self.invites[guild.id] = await guild.invites()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        old_invites = self.invites[guild.id]
        new_invites = await guild.invites()

        for invite in new_invites:
            for old in old_invites:
                if invite.code == old.code and invite.uses > old.uses:
                    channel = discord.utils.get(guild.text_channels, name="general")
                    if channel:
                        await channel.send(
                            f"🎉 {member.mention} joined using invite from {invite.inviter.mention}"
                        )

        self.invites[guild.id] = new_invites

    @app_commands.command(name="invites", description="Check your invite count")
    async def invites(self, interaction: discord.Interaction):
        await interaction.response.send_message("Invite tracking enabled!")

async def setup(bot):
    await bot.add_cog(Invites(bot))